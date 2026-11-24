---
name: daily-briefing
description: Generate the eight-section daily briefing from repo files, offline if no API key is present.
---

# daily-briefing

## When to use

The daily workflow, or a request for "what changed" that must stay inside the imported corpus.

## Inputs

- Registry, matrix, scores, boards, `knowledge/tools.yaml`, `knowledge/risks.yaml`.
- `prompts/daily-briefing.md`
- Optional `X_BEARER_TOKEN` and `XAI_API_KEY`.

## Steps

1. If `X_BEARER_TOKEN` is set, `scripts/refresh_profiles.py` may append a few recent posts. If it is unset, skip refresh and say so.
2. If `XAI_API_KEY` is set, Phase 1 still does not send profile text to a model. Say that in the briefing.
3. Run `python3 scripts/generate_daily_briefing.py --date YYYY-MM-DD`.
4. Confirm the eight headings: Top signals, Per-domain moves, Notable posts, Emerging tools, Opportunities, Board take, Risks and caveats, Next actions.
5. The board section must carry the simulated-board disclaimer.

## Outputs

`intelligence/daily/<date>.md` and `.json`.

## Guardrails

The baseline file `intelligence/daily/2026-11-24.md` is the imported snapshot. A later file is still mostly that snapshot unless refresh appended rows. Do not describe unfetched posts.

## Related

`prompts/daily-briefing.md`
