# Prompt: score-opportunity

Score this hypothesis. It is a hypothesis.

<hypothesis>

Use the weights in `config/scoring.yaml`:

- market_pull 25
- evidence_strength 20
- fit_with_kishore_skills 15
- time_to_value 15
- competition_gap 10
- monetization_clarity 10
- risk_inverse 5

Each score is an integer 0–10. Fit may use only `config/operator.yaml`. Every evidence item needs `profile`, `source`, and the URL copied from that source.

Include the opportunity disclaimer from `scripts/distilllib.py`. Do not state an income figure for Kishore. Author revenue stays labelled as that author's self-report.

Then run `python3 scripts/score_opportunities.py`.
