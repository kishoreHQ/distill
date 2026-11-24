---
name: weekly-review
description: Summarise the week's daily briefings and the current opportunity ranking without inventing deltas.
---

# weekly-review

## When to use

Sunday's workflow, or a request for a week-in-review.

## Inputs

- Daily files under `intelligence/daily/` for the ISO week.
- `opportunities/scores.json`
- `prompts/weekly-review.md`

## Steps

1. List which days have a briefing and which do not. A missing file is a missing file, not a quiet news day.
2. Run `python3 scripts/generate_weekly_review.py --date YYYY-MM-DD`.
3. If the only material is the 2026-11-24 snapshot, say there is no measured day-over-day change.
4. Repeat the simulated-board disclaimer and the opportunity disclaimer.

## Outputs

`intelligence/weekly/<iso-week>.md`.

## Guardrails

Do not compute follower growth or revenue growth from impression fields. Do not mark the week "complete" as a research pass.

## Related

`prompts/weekly-review.md`
