# Automation guide

Workflows live in `.github/workflows/`. They install `requirements.txt` and run the scripts. They do not embed secret values.

## validate.yml

On pull requests and pushes to `main`. Runs `scripts/validate_repo.py` and `pytest`. No API token is required. A failure means the tree disagrees with itself.

## daily.yml

Cron `30 23 * * *`, which is 23:30 UTC and 05:00 IST. Also `workflow_dispatch`.

Order:

1. `scripts/refresh_profiles.py` with `X_BEARER_TOKEN` and `XAI_API_KEY` from Actions secrets.
2. `scripts/generate_daily_briefing.py` for the UTC date.
3. `scripts/generate_dashboard.py`.
4. Commit and push if `intelligence/` or `dashboard/data.json` or `profiles/` changed.

When the secrets are empty, step 1 exits 0 and step 2 writes an offline briefing. The job should still go green.

The refresh, when the token exists, calls the official recent-search endpoint for three active people and at most 10 posts each. That is under the budgets in `config/sources.yaml`. It does not page through history. A non-200 response is logged and does not fail the briefing.

Phase 1 does not call an XAI model even if `XAI_API_KEY` is present. The briefing text says so. Wiring a model is deferred. See `STATUS.md`.

## weekly.yml

Cron `30 23 * * 0` (Sunday 23:30 UTC). Runs `generate_weekly_review.py` and commits `intelligence/weekly/` when it changes.

## Local equivalents

```bash
python3 scripts/refresh_profiles.py
python3 scripts/generate_daily_briefing.py --date 2026-11-24
python3 scripts/generate_weekly_review.py --date 2026-11-24
python3 scripts/generate_dashboard.py
```

Unset the token if you want to confirm the skip path:

```bash
env -u X_BEARER_TOKEN python3 scripts/refresh_profiles.py
```

## Commit identity

The workflows set a local git user named `distill-bot` only inside the Action, so the commit is not attributed to a random developer. That name is not a person in the profiles.
