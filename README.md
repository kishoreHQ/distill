# DISTILL

This repository started as a one-line note, `distill repo`. It is now Phase 1 of DISTILL: a git-native operating system for multi-person knowledge distillation, a daily intelligence briefing, and simulated advisory boards.

The store is markdown, YAML, JSON, and Python. GitHub Actions validates pull requests and can write a daily briefing. There is no application server in this phase.

People in `profiles/` were distilled from public posts and pages. The research bundles are the source of truth. This repo does not invent biographies, quotes, or follower counts. `x-aravind` is kept and marked excluded because it was the wrong account. `aravind-srinivas` is the account the research replaced it with.

Advisory boards under `boards/` are simulated. The named people have not joined, have not been contacted, and have not endorsed anything here.

## Layout

| Path | Role |
|---|---|
| `config/` | Domains, scoring weights, allowed sources, schedule |
| `schemas/` | JSON Schema for profiles, sources, posts, status, boards, opportunities, briefings |
| `profiles/` | Registry plus one folder per person |
| `boards/` | Five simulated boards |
| `knowledge/` | Matrix, themes, tools, disagreements |
| `intelligence/daily/` and `intelligence/weekly/` | Generated briefings |
| `opportunities/` | Scored hypotheses |
| `skills/` and `prompts/` | Portable instructions for an agent |
| `scripts/` | Import, validate, matrix, score, briefings |
| `tests/` | Pytest |
| `docs/` | Guides, including the original research spec under `docs/research/` |
| `dashboard/data.json` | Data for a UI that is not built yet |

## Commands

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate_repo.py
python3 -m pytest
```

Rebuilding from the research archive (the archive itself is not committed):

```bash
python3 scripts/import_research_bundle.py --archive /path/to/distill-research-bundles.tgz
python3 scripts/build_matrix.py
python3 scripts/score_opportunities.py
python3 scripts/generate_daily_briefing.py --date 2026-11-24
python3 scripts/generate_weekly_review.py --date 2026-11-24
python3 scripts/generate_dashboard.py
```

## Status

`STATUS.md` lists what is implemented and what is only planned. Do not treat a heading in this README as a finished product unless that file says the check has been run.

## Agents

`AGENTS.md` is the instruction file for any automated worker in this repo.

## Third-party text

`LICENSE-NOTE.md` covers excerpts and post metadata. Short quotes are stored with links. Full timelines are not.
