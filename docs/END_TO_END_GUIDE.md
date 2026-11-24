# End-to-end guide

Phase 1 is a git repo of markdown, YAML, JSON, and Python. A daily run reads that repo, optionally asks the X API for a few new posts, and writes a briefing. It does not require a hosted service.

## One-time setup

```bash
python3 -m pip install -r requirements.txt
```

The research archive is an input, not a committed file. To rebuild profiles from it:

```bash
python3 scripts/import_research_bundle.py --archive /path/to/distill-research-bundles.tgz
python3 scripts/build_matrix.py
python3 scripts/score_opportunities.py
python3 scripts/generate_daily_briefing.py --date 2026-11-24
python3 scripts/generate_weekly_review.py --date 2026-11-24
python3 scripts/generate_dashboard.py
python3 scripts/validate_repo.py
python3 -m pytest
```

After the first import, the profile folders are in git. CI does not need the archive.

## What a day looks like

1. `refresh_profiles.py` checks `X_BEARER_TOKEN`. Absent: it writes `intelligence/refresh-status.json` with `ran: false` and exits 0.
2. Present: it recent-searches three active people and appends unseen posts. Profile essays stay as they were.
3. `generate_daily_briefing.py` builds eight sections from the registry, the matrix, the scores, the boards, and the highest impression counts stored on posts.
4. `generate_dashboard.py` refreshes `dashboard/data.json`. The UI that would render it is not in this phase.
5. The daily workflow commits those outputs when they changed.

`XAI_API_KEY` is read only so the briefing can say the key was present and unused. Phase 1 does not send text to a model.

## Where to look

| Question | File |
|---|---|
| Who is in the corpus | `profiles/registry.yaml` |
| Which domain | `knowledge/classification-matrix.md` |
| What to try | `opportunities/scores.json` |
| What the simulated boards said | `boards/*/deliberations/2026-11-24.md` |
| What was true on import day | `intelligence/daily/2026-11-24.md` |
| What is not done | `STATUS.md` |

## Hard stops

- Do not merge `x-aravind` into `aravind-srinivas`.
- Do not drop the simulated-board disclaimer.
- Do not put a token, cookie, or `.env` in the repo.
- Do not treat a score as revenue.
