---
name: score-opportunity
description: Score one opportunity hypothesis with the seven weights in config/scoring.yaml.
---

# score-opportunity

## When to use

A new hypothesis has evidence links, or a weight in `config/scoring.yaml` changed.

## Inputs

- `config/scoring.yaml` and `config/operator.yaml`
- `prompts/score-opportunity.md`
- At least one `profiles/<id>/sources.yaml` row per evidence link.

## Steps

1. Write the hypothesis as a hypothesis. Status stays `hypothesis`.
2. Score each dimension as an integer from 0 to 10. The note must say what evidence you used. A single blog post is not a market study, so market pull stays modest.
3. Fit uses only the operator context in `config/operator.yaml`. Do not invent a résumé.
4. Run `python3 scripts/score_opportunities.py`. Total is the sum of `(score / 10) * weight`. Weights are 25, 20, 15, 15, 10, 10, and 5.
5. Put the standard opportunity disclaimer on the file. Scores are not income.

## Outputs

`opportunities/<id>.yaml` and a regenerated `opportunities/scores.json`.

## Guardrails

No artificial income claims. If the only evidence is a creator promising passive income, do not open an opportunity. Link the source and move on.

## Related

`prompts/score-opportunity.md`
