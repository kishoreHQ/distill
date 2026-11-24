#!/usr/bin/env python3
"""Bounded X API refresh. Skips cleanly when X_BEARER_TOKEN is absent.

Uses the official recent-search endpoint only. Does not scrape, does not
bypass a login, and does not rewrite profile essays. On any HTTP failure it
records the status code and returns 0 so the offline briefing can still run.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

from distilllib import ROOT, SNAPSHOT_DATE, dump_json, load_yaml, read_posts, read_status

API_URL = "https://api.x.com/2/tweets/search/recent"
MAX_PROFILES = 3
MAX_RESULTS = 10


def select_profiles(registry: dict, on: date, limit: int = MAX_PROFILES) -> list[dict]:
    people = [
        row
        for row in registry["profiles"]
        if row["registry_status"] == "active" and row["account_type"] == "person"
    ]
    people.sort(key=lambda row: row["id"])
    if not people:
        return []
    start = on.timetuple().tm_yday % len(people)
    ordered = people[start:] + people[:start]
    return ordered[:limit]


def rows_from_payload(payload: dict, username: str) -> list[dict]:
    rows = []
    for item in payload.get("data") or []:
        metrics = item.get("public_metrics") or {}
        text = (item.get("text") or "").replace("\u2028", "\n")
        if len(text) > 280:
            text = text[:277] + "..."
        rows.append(
            {
                "id": str(item["id"]),
                "created_at": item.get("created_at") or "",
                "url": f"https://x.com/{username}/status/{item['id']}",
                "text": text,
                "metrics": {
                    "like_count": metrics.get("like_count"),
                    "retweet_count": metrics.get("retweet_count"),
                    "reply_count": metrics.get("reply_count"),
                    "quote_count": metrics.get("quote_count"),
                    "bookmark_count": metrics.get("bookmark_count"),
                    "impression_count": metrics.get("impression_count"),
                },
                "origin": "refresh",
                "band": "refresh",
            }
        )
    return rows


def fetch_recent(token: str, username: str, since_id: str | None) -> tuple[int, dict]:
    query = f"from:{username} -is:retweet"
    params = {
        "query": query,
        "max_results": str(MAX_RESULTS),
        "tweet.fields": "created_at,public_metrics,text",
    }
    if since_id and since_id.isdigit():
        params["since_id"] = since_id
    url = API_URL + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "User-Agent": "distill-phase1"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            body = json.loads(response.read().decode("utf-8"))
            return response.status, body
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:300]
        return exc.code, {"error": detail}


def append_posts(folder, rows: list[dict]) -> int:
    existing = {post["id"] for post in read_posts(folder)}
    fresh = [row for row in rows if row["id"] not in existing]
    if not fresh:
        return 0
    with (folder / "posts.jsonl").open("a", encoding="utf-8") as handle:
        for row in fresh:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(", ", ": ")) + "\n")
    return len(fresh)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--date", default=None)
    args = parser.parse_args()
    root = args.root
    on = date.fromisoformat(args.date) if args.date else datetime.now(timezone.utc).date()
    token = os.environ.get("X_BEARER_TOKEN") or ""
    status_path = root / "intelligence" / "refresh-status.json"
    status_path.parent.mkdir(parents=True, exist_ok=True)
    if not token:
        dump_json(
            {
                "ran": False,
                "date": on.isoformat(),
                "reason": "X_BEARER_TOKEN absent; live refresh skipped",
                "profiles": [],
            },
            status_path,
        )
        print("X_BEARER_TOKEN absent; skipping live refresh")
        return 0
    registry = load_yaml(root / "profiles" / "registry.yaml")
    chosen = select_profiles(registry, on)
    results = []
    for row in chosen:
        folder = root / row["path"]
        state = read_status(folder)
        code, payload = fetch_recent(token, row["x_username"], str(state.get("last_post_id") or ""))
        if code != 200:
            results.append({"id": row["id"], "http_status": code, "added": 0})
            print(f"refresh {row['id']} http {code}; continuing")
            continue
        added = append_posts(folder, rows_from_payload(payload, row["x_username"]))
        results.append({"id": row["id"], "http_status": 200, "added": added})
        print(f"refresh {row['id']} added {added}")
    dump_json(
        {
            "ran": True,
            "date": on.isoformat(),
            "snapshot_date": SNAPSHOT_DATE,
            "reason": "bounded recent search; profile essays were not rewritten",
            "profiles": results,
        },
        status_path,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
