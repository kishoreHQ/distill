# Project discovery

Date: 2026-11-24. This note records what was in the repository before Phase 1 and what the import contained. It is the plan that was then implemented in this branch. Items that are not implemented are listed in `STATUS.md` and are not described as done here.

## What was already in the repo

The git tree had one file, `Readme.md`, whose entire body was:

```
distill repo
```

No profiles, workflows, schemas, or license. That one line is kept in the new `README.md` so the rename of the file does not drop the original note. There was no existing design to preserve beyond it.

## What the archive contained

The input archive was `distill-research-bundles.tgz` (uploaded on the VM as `distill-research-bundles_ffe2.tgz`). It matched `SPEC.md` v1 dated 2026-11-24.

- `SPEC.md`, `batch-A-summary.md`, `batch-B-summary.md`, `batch-C-summary.md`.
- 32 folders under `profiles/<id>/`, each with `profile.md`, `sources.yaml`, `posts.jsonl`, and `status.json`.
- `extra/arnav-gupta/` in a different shape: `PROFILE.json`, `skill/*.md`, `state/evidence.md`, `state/sync.json`.

The batches say the posts were read through the X API, plus public pages. They also say login walls were not bypassed. This phase treats those files as the source of truth and does not re-fetch them in order to "improve" a biography.

## Identity issues the batches already flagged

- `x-aravind` (`@aravind`) is the wrong account. Batch A says Kishore replaced it with `@AravSrinivas`. The bundle is kept. Registry status is `excluded`. `aravind-srinivas` is the active profile.
- `gittrend` and `x-githubprojects` are aggregators. They stay active as signal feeds and are not board members.
- `arnav-gupta` (`@championswimmer`) was not in the 32. The extra folder says 200 posts were read and stores 144 evidence quotes, not a `posts.jsonl`. The import converts it to the standard shape and records that gap. `PROFILE.json` says Railway. The skill README's timeline ends at Meta and notes a LinkedIn headline that says Railway. Both wordings are kept.

## Plan that this branch carries out

1. Layout in the README: `config/`, `schemas/`, `profiles/`, `boards/`, `knowledge/`, `intelligence/`, `opportunities/`, `skills/`, `prompts/`, `scripts/`, `tests/`, `docs/`, `dashboard/`.
2. Import script, idempotent, plus validators and pytest.
3. Five operating domains and a generated matrix. The research tags (`ai-engineering`, `automation`, and the rest) stay in front matter. The matrix maps them.
4. Five simulated boards with a disclaimer. No claim that anyone joined.
5. Five scored hypotheses. Weights 25/20/15/15/10/10/5.
6. One baseline daily briefing dated 2026-11-24, generated from the snapshot, plus a weekly file for that ISO week.
7. GitHub Actions: validate on pull request and push; daily at 23:30 UTC; weekly on Sunday at 23:30 UTC. Secrets are referenced by name. Missing secrets skip the live path.
8. Dashboard data file only. The UI is deferred.

## What was deliberately not in the plan

A live model rewrite of every profile, a browser pass on JS-rendered sites, LinkedIn behind login, and a dashboard UI. Batch notes already list those as undone. Phase 1 does not mark them done.
