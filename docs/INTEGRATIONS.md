# Integrations

Phase 1 does not call Kishore's other bots. This note is so an agent working in this repo does not confuse the roles. None of these bots are implemented in this repository.

## Dr. Eggbot V2

Dr. Eggbot V2 designs single-job bots. A single-job bot does one narrow task and finishes. DISTILL skills are written so a bot of that kind can run one of them: distill one profile, score one opportunity, validate the repo. A skill file is the contract. Eggbot is not a board member and is not a profile in `profiles/`.

## Firstmate

Firstmate is Kishore's coordinator agent. The intended hand-off is: Firstmate decides which DISTILL skill to run, and DISTILL returns files in this repo (a profile, a briefing, a score). Firstmate should not merge people, should not drop the simulated-board disclaimer, and should treat `STATUS.md` as the list of what this repo can actually do. If Firstmate asks for a live model rewrite of every profile, that work is not implemented here yet.

## The Distill anyone bot

The Distill anyone bot does per-person distills. It maps to the `distill-profile` and `add-profile` skills. One invocation, one id, one folder. The output should match `schemas/`. It should refuse a request to blend two accounts into one voice. Arnav Gupta's extra bundle was a distill of that general kind, stored in a different file layout. `import_research_bundle.py` is the converter for that layout. A future anyone-bot export should prefer the standard four files so the converter is unnecessary.

## X and GitHub

The only external systems the workflows know how to call are the X API, via `X_BEARER_TOKEN`, and git itself. GitHub is also a public source in `config/sources.yaml`, used by the original research and not re-queried by Phase 1 scripts. There is no Slack, Linear, or email integration in this repo.

## Dashboard

`dashboard/data.json` is the integration point for a future UI. The file is generated. The UI is deferred. Do not add a front-end framework in a drive-by change. A consumer should treat `ui: deferred` as the signal that there is no page to open.
