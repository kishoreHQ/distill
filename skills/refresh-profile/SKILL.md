---
name: refresh-profile
description: Update one profile's post metadata from the official X API, or skip when the token is absent.
---

# refresh-profile

## When to use

A scheduled refresh, or a request to see whether one account posted since `last_post_id`. Not for a first-time biography.

## Inputs

- `X_BEARER_TOKEN` in the environment, or the GitHub Actions secret of the same name.
- `prompts/refresh-profile.md`
- The profile's `status.json` `last_post_id`.

## Steps

1. If `X_BEARER_TOKEN` is unset, stop. Say the refresh was skipped. Do not scrape.
2. Call only the official recent-search endpoint, `from:<username> -is:retweet`, at most 10 results. The repo script is `scripts/refresh_profiles.py`, which rotates three people per day so the daily budget stays small.
3. Append new rows to `posts.jsonl` with `origin: refresh`. Do not rewrite the essay.
4. On HTTP 401, 403, or 429, record the status code and stop. Do not retry in a loop.
5. A refresh does not raise `research_status` to verified. New posts are unread until a person or the distill-profile skill actually reads them.

## Outputs

Appended `posts.jsonl` rows and `intelligence/refresh-status.json`.

## Guardrails

No login walls, no cookies, no token in the git diff. Do not treat API impression counts as audited reach. Do not refresh `x-aravind` into `aravind-srinivas`.

## Related

`prompts/refresh-profile.md`
