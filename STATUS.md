# Status

Checked on 2026-11-24 by running the import, the generators, `scripts/validate_repo.py`, and `pytest` in this branch. If a row says implemented, those commands covered it. If a row says deferred, it is not done.

## Implemented

| Piece | Evidence |
|---|---|
| Research import of the 32 bundles plus converted `arnav-gupta` | `scripts/import_research_bundle.py`. Registry: 32 active, 1 excluded (`x-aravind`). |
| `x-aravind` kept, status `excluded`, `replaced_by: aravind-srinivas` | `profiles/registry.yaml` and `profiles/x-aravind/status.json` |
| Schemas and `validate_repo.py` | `schemas/`, `scripts/validate_repo.py` |
| Citation check | `scripts/check_sources.py`, called from the validator |
| Classification matrix for five domains | `scripts/build_matrix.py`, `knowledge/classification-matrix.md` |
| Scoring weights 25/20/15/15/10/10/5 and five hypotheses | `config/scoring.yaml`, `scripts/score_opportunities.py`, `opportunities/` |
| Five simulated boards with disclaimer, charter, and a 2026-11-24 deliberation | `boards/` |
| Knowledge seed: themes, tools, contrarian views | `knowledge/*.md` |
| Baseline daily briefing, eight sections, snapshot labelled | `intelligence/daily/2026-11-24.md` |
| Weekly review for the ISO week of that date | `intelligence/weekly/` |
| Offline refresh path when `X_BEARER_TOKEN` is absent | `scripts/refresh_profiles.py` |
| Bounded official-API refresh when the token is present | Same script. Not executed against the live API in this phase, because no token was used here. |
| Daily and weekly workflows, validate workflow | `.github/workflows/` |
| Nine skills and matching prompts | `skills/`, `prompts/` |
| Dashboard data file | `dashboard/data.json` with `"ui": "deferred"` |
| Pytest | `tests/test_phase1.py` |
| 2026-11-25 post append and re-distill | `posts.jsonl` rows from the supplied official X read, profile sections where those rows support a change, `scripts/validate_repo.py`, and `pytest`. |
| 2026-11-26 post append and re-distill | 493 new rows across 26 profiles from the supplied official X read, profile sections where those rows support a change, regenerated matrix, scores, dashboard, and `intelligence/daily/2026-11-26.md`. `scripts/validate_repo.py` and `pytest`. |
| 2026-11-27 post append and re-distill | 405 new rows across 28 profiles from a supplied official X read since 2026-11-25T22:16:21Z. Profile sections where those rows support a change. Swanand and Vatsal Sanghvi deepen passes returned no older posts and were not promoted. Regenerated matrix, scores, dashboard, and `intelligence/daily/2026-11-27.md`. `scripts/validate_repo.py` and `pytest`. |
| 2026-11-28 post append and re-distill | 314 new rows across 27 profiles from a supplied official X read from 2026-11-26T22:17:25Z to 2026-11-28T00:17:25.371Z. Profile sections where those rows support a change. julian-goldie was capped at 75 fetched posts. Deepen passes for x-wojakcodes and arnav-gupta returned no older posts and were not promoted. Opportunity totals were recomputed and did not change. Regenerated matrix, scores, dashboard, and `intelligence/daily/2026-11-28.md`. `scripts/validate_repo.py` and `pytest`. |

## Deferred

| Piece | Why it is not marked done |
|---|---|
| Dashboard UI | Only `dashboard/data.json` is generated. There is no page. |
| Model-written briefings | `XAI_API_KEY` is accepted and ignored. The briefing is a template over repo files. |
| Full timeline refresh | Daily refresh, when a token exists, asks for at most 10 recent posts for 3 people. It does not re-read history or rewrite essays. |
| Re-research of partial profiles | Swanand, Ojasvika, Suman, Vatsal, Kushal, and Wojak stay partial. The 2026-11-26 official read appended posts, including 25 older posts for Suman and an empty older read for Ojasvika. On 2026-11-27 a deepen pass for Swanand and Vatsal Sanghvi returned no older posts. On 2026-11-28 a deepen pass for x-wojakcodes and arnav-gupta returned no older posts. No browser pass was added. They were not promoted. |
| Arnav Gupta's 200 posts | The extra bundle did not include them. The 2026-11-25 refresh appended a later official-API sample. It is not that missing file. |
| A "master" board | The research spec names master eligibility. Phase 1 has the five domain boards only. |
| Live proof of the GitHub Actions cron | The workflow files are in the repo. They have not been observed firing on GitHub from this environment. |
| Linking Firstmate, Dr. Eggbot V2, or the Distill anyone bot | `docs/INTEGRATIONS.md` describes the roles. No code calls them. |

## Data gaps left visible

See `docs/LIMITATIONS_AND_CAVEATS.md`. The short list: chronological X samples rather than top posts, self-reported money, unresolved Railway-versus-Meta wording for Arnav Gupta, aggregator accounts that are not people, and `x-aravind` as the wrong handle.
