#!/usr/bin/env python3
"""Build a daily briefing from files already in the repo.

Phase 1 does not call a model, even if XAI_API_KEY is set. Live post refresh
is a separate script. This generator only reads the snapshot plus whatever
refresh has already appended.
"""

from __future__ import annotations

import argparse
import os
from datetime import date
from pathlib import Path

from distilllib import (
    DISCLAIMER,
    OPPORTUNITY_DISCLAIMER,
    ROOT,
    SECTION_HEADINGS,
    SNAPSHOT_DATE,
    dump_json,
    load_json,
    load_yaml,
    profile_dirs,
    read_posts,
    read_profile,
    read_status,
)


def notable_posts(root: Path, limit: int = 5) -> list[dict]:
    rows = []
    for folder in profile_dirs(root):
        meta, _body = read_profile(folder)
        status = read_status(folder)
        if status.get("research_status") == "excluded":
            continue
        for post in read_posts(folder):
            metrics = post.get("metrics") or {}
            impressions = metrics.get("impression_count")
            if impressions is None:
                continue
            rows.append(
                {
                    "profile": meta["id"],
                    "display_name": meta["display_name"],
                    "account_type": meta["account_type"],
                    "url": post["url"],
                    "created_at": post.get("created_at") or "",
                    "impressions": int(impressions),
                    "text": (post.get("text") or "").replace("\n", " "),
                }
            )
    rows.sort(key=lambda row: (-row["impressions"], row["profile"], row["url"]))
    return rows[:limit]


def bullet(text: str) -> str:
    return text.strip().replace("\n", " ")


def build_sections(root: Path) -> dict[str, str]:
    matrix = load_json(root / "knowledge" / "classification-matrix.json")
    scores = load_json(root / "opportunities" / "scores.json")
    notes = load_yaml(root / "knowledge" / "domain-notes.yaml")
    tools = load_yaml(root / "knowledge" / "tools.yaml")
    risks = load_yaml(root / "knowledge" / "risks.yaml")
    registry = load_yaml(root / "profiles" / "registry.yaml")

    partial = [
        row["id"]
        for row in registry["profiles"]
        if row["registry_status"] == "active" and row["research_status"] == "partial"
    ]
    aggregators = [row["id"] for row in matrix["profiles"] if row["aggregator"]]
    posts = notable_posts(root)
    top = posts[0]
    best = scores["opportunities"][0]

    signals = [
        (
            f"Highest impression count stored in the snapshot is {top['impressions']} on "
            f"{top['display_name']} (`{top['profile']}`, {top['account_type']}), {top['created_at']}: {top['url']}. "
            "Impression fields are copied from the research bundle. They were not re-checked."
        ),
        (
            f"Highest scored hypothesis is `{best['id']}` at {best['total']} "
            f"({best['title']}). {OPPORTUNITY_DISCLAIMER}"
        ),
        (
            f"Active profiles: {registry['counts']['active']}. Excluded: {registry['counts']['excluded']} "
            f"(`x-aravind`, wrong account; `aravind-srinivas` is the account the batch A summary says replaced it). "
            f"Partial research status: {', '.join(partial) if partial else 'none'}."
        ),
        (
            "Aggregator feeds, not advisors: " + ", ".join(f"`{item}`" for item in aggregators) + "."
        ),
    ]
    if top["impressions"] >= 1_000_000:
        signals.append(
            "At least one stored impression count is above one million. Treat that as an API field from the snapshot, not as an audited reach number."
        )

    domain_lines = []
    titles = {item["id"]: item["title"] for item in matrix["domains"]}
    for note in notes:
        primary = [row["id"] for row in matrix["profiles"] if row["primary"] == note["domain"]]
        domain_lines.append(
            f"**{titles[note['domain']]}** ({len(primary)} primary): {bullet(note['text'])} "
            f"Primary ids: {', '.join(primary)}."
        )

    post_lines = []
    for row in posts:
        preview = row["text"][:180].replace("[", "(").replace("]", ")")
        flag = " Aggregator feed." if row["account_type"] == "aggregator" else ""
        post_lines.append(
            f"- `{row['profile']}` {row['created_at']} — {row['impressions']} impressions.{flag} {preview} {row['url']}"
        )

    tool_lines = []
    for tool in tools:
        cites = ", ".join(f"[{item['profile']} {item['source']}]" for item in tool["evidence"])
        tool_lines.append(f"- **{tool['name']}**. {bullet(tool['note'])} Evidence: {cites}.")

    opp_lines = []
    for row in scores["opportunities"]:
        bits = ", ".join(
            f"{name} {item['score']} (weight {item['weight']})"
            for name, item in row["breakdown"].items()
        )
        links = ", ".join(item["url"] for item in row["evidence"])
        opp_lines.append(
            f"- **{row['rank']}. {row['title']}** (`{row['id']}`) total {row['total']}. {bits}. Links: {links}"
        )

    board_lines = [DISCLAIMER, ""]
    for path in sorted((root / "boards").glob("*/board.yaml")):
        board = load_yaml(path)
        board_lines.append(
            f"**{board['title']}** (confidence {board['confidence']}): {bullet(board['synthesis'])}"
        )
    actions = []
    for path in sorted((root / "boards").glob("*/board.yaml")):
        board = load_yaml(path)
        actions.append(f"- {board['title']}: {bullet(board['recommended_next_action'])}")

    risk_lines = [f"- {item['text']}" for item in risks]

    return {
        "top_signals": "\n".join(f"- {bullet(line)}" for line in signals),
        "per_domain_moves": "\n\n".join(domain_lines),
        "notable_posts": "\n".join(post_lines) + "\n\nThese are the five highest `impression_count` values on active profiles in the imported posts. The sample is a set of date windows, not a ranking the authors chose.",
        "emerging_tools": "\n".join(tool_lines) + "\n\nNames appear because a cited source discusses them. A mention is not a recommendation to buy or install.",
        "opportunities": OPPORTUNITY_DISCLAIMER + "\n\n" + "\n".join(opp_lines),
        "board_take": "\n\n".join(board_lines),
        "risks_and_caveats": "\n".join(risk_lines),
        "next_actions": "\n".join(actions) + "\n\nDo not mark a research gap closed unless a later import actually contains the missing source.",
    }


def render_markdown(payload: dict) -> str:
    lines = [
        f"# DISTILL daily briefing — {payload['date']}",
        "",
        f"**Mode:** {payload['mode']}.",
        f"**Snapshot:** research bundles dated {payload['snapshot_date']}. This briefing is generated from files in the repo. It is not a live timeline.",
        "",
        payload["disclaimer"],
        "",
    ]
    if payload.get("xai_api_key_present"):
        lines.append(
            "XAI_API_KEY is set in the environment. Phase 1 does not send profile text to a model. The briefing stays on this template."
        )
        lines.append("")
    if payload.get("live_refresh_ran"):
        lines.append("A bounded X API refresh ran before this file was written. New rows, if any, are in `posts.jsonl` with `origin: refresh`. Profile essays were not rewritten.")
        lines.append("")
    else:
        lines.append("No live X refresh was applied for this file. Either `X_BEARER_TOKEN` was absent or refresh did not run.")
        lines.append("")
    for key, heading in SECTION_HEADINGS:
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(payload["sections"][key])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate(root: Path, on: date) -> dict:
    refresh = root / "intelligence" / "refresh-status.json"
    ran = False
    if refresh.exists():
        status = load_json(refresh)
        ran = bool(status.get("ran")) and status.get("date") == on.isoformat()
    sections = build_sections(root)
    payload = {
        "date": on.isoformat(),
        "mode": "offline-after-refresh" if ran else "offline-snapshot",
        "snapshot_date": SNAPSHOT_DATE,
        "disclaimer": DISCLAIMER + " " + OPPORTUNITY_DISCLAIMER,
        "xai_api_key_present": bool(os.environ.get("XAI_API_KEY")),
        "live_refresh_ran": ran,
        "sections": sections,
    }
    day_dir = root / "intelligence" / "daily"
    day_dir.mkdir(parents=True, exist_ok=True)
    dump_json(payload, day_dir / f"{on.isoformat()}.json")
    (day_dir / f"{on.isoformat()}.md").write_text(render_markdown(payload), encoding="utf-8")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--date", default=SNAPSHOT_DATE)
    args = parser.parse_args()
    on = date.fromisoformat(args.date)
    payload = generate(args.root, on)
    print(f"wrote intelligence/daily/{payload['date']}.md mode={payload['mode']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
