#!/usr/bin/env python3
"""Write dashboard/data.json. The UI that would read it is deferred."""

from __future__ import annotations

import argparse
from pathlib import Path

from distilllib import ROOT, SNAPSHOT_DATE, dump_json, load_json, load_yaml, read_posts, read_profile, read_status, profile_dirs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root
    registry = load_yaml(root / "profiles" / "registry.yaml")
    matrix = load_json(root / "knowledge" / "classification-matrix.json")
    scores = load_json(root / "opportunities" / "scores.json")
    by_id = {row["id"]: row for row in matrix["profiles"]}
    profiles = []
    for row in registry["profiles"]:
        classified = by_id.get(row["id"])
        profiles.append(
            {
                "id": row["id"],
                "display_name": row["display_name"],
                "x_username": row["x_username"],
                "registry_status": row["registry_status"],
                "research_status": row["research_status"],
                "account_type": row["account_type"],
                "posts_imported": row["posts_imported"],
                "primary_domain": None if classified is None else classified["primary"],
            }
        )
    notable = []
    for folder in profile_dirs(root):
        meta, _body = read_profile(folder)
        if read_status(folder).get("research_status") == "excluded":
            continue
        for post in read_posts(folder):
            metrics = post.get("metrics") or {}
            impressions = metrics.get("impression_count")
            if impressions is None:
                continue
            notable.append(
                {
                    "profile": meta["id"],
                    "url": post["url"],
                    "impressions": int(impressions),
                    "created_at": post.get("created_at"),
                }
            )
    notable.sort(key=lambda row: -row["impressions"])
    boards = []
    for path in sorted((root / "boards").glob("*/board.yaml")):
        board = load_yaml(path)
        boards.append(
            {
                "id": board["id"],
                "title": board["title"],
                "members": [member["profile_id"] for member in board["members"]],
                "confidence": board["confidence"],
            }
        )
    payload = {
        "ui": "deferred",
        "snapshot_date": SNAPSHOT_DATE,
        "note": "Data only. No dashboard UI is implemented in Phase 1.",
        "counts": registry["counts"],
        "domains": matrix["domains"],
        "profiles": profiles,
        "opportunities": [
            {"id": row["id"], "title": row["title"], "total": row["total"], "rank": row["rank"]}
            for row in scores["opportunities"]
        ],
        "boards": boards,
        "notable_posts": notable[:10],
    }
    dump_json(payload, root / "dashboard" / "data.json")
    print(f"dashboard profiles={len(profiles)} notable={len(payload['notable_posts'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
