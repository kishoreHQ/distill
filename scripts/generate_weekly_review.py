#!/usr/bin/env python3
"""Weekly review from daily briefing files already in the repo."""

from __future__ import annotations

import argparse
from datetime import date, timedelta
from pathlib import Path

from distilllib import DISCLAIMER, OPPORTUNITY_DISCLAIMER, ROOT, SNAPSHOT_DATE, load_json


def week_dates(anchor: date) -> list[date]:
    monday = anchor - timedelta(days=anchor.weekday())
    return [monday + timedelta(days=offset) for offset in range(7)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--date", default=SNAPSHOT_DATE)
    args = parser.parse_args()
    anchor = date.fromisoformat(args.date)
    iso = anchor.isocalendar()
    label = f"{iso.year}-W{iso.week:02d}"
    found = []
    missing = []
    for day in week_dates(anchor):
        path = args.root / "intelligence" / "daily" / f"{day.isoformat()}.md"
        if path.exists():
            found.append(day.isoformat())
        else:
            missing.append(day.isoformat())
    scores = load_json(args.root / "opportunities" / "scores.json")
    ranking = "\n".join(
        f"- {row['rank']}. `{row['id']}` — {row['total']} — {row['title']}"
        for row in scores["opportunities"]
    )
    body = f"""# DISTILL weekly review — {label}

Week containing {anchor.isoformat()}. Generated from daily files in the repo. Snapshot date of the research import: {SNAPSHOT_DATE}.

{DISCLAIMER}

{OPPORTUNITY_DISCLAIMER}

## Dailies in this week

Present: {", ".join(found) if found else "none"}.

Missing: {", ".join(missing) if missing else "none"}.

A missing day means that briefing file was not generated. It does not mean nothing happened on X.

## What changed

Phase 1 has one imported snapshot ({SNAPSHOT_DATE}). This review does not claim day-over-day movement in follower counts, revenue, or posting. If a later daily was built after `scripts/refresh_profiles.py` appended posts, those rows are marked `origin: refresh` in `posts.jsonl` and the profile essays are still the snapshot.

## Opportunity ranking

{ranking}

## Carry forward

- Keep `x-aravind` excluded. Do not merge it into `aravind-srinivas`.
- Do not promote a self-reported ARR, MRR, or placement figure into a forecast.
- Re-run `scripts/validate_repo.py` after any import or hand edit.

## Next actions

Use the next-action lines in the latest daily briefing. They are simulated-board output, not instructions from the named people.
"""
    out = args.root / "intelligence" / "weekly" / f"{label}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out.relative_to(args.root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
