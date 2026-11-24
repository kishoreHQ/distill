# Prompt: daily-briefing

Write the daily briefing for `<date>` from the repo.

If `X_BEARER_TOKEN` is missing, say the briefing is the offline snapshot. If `XAI_API_KEY` is set, do not send profile text to a model in Phase 1.

Eight sections, in this order:

1. Top signals
2. Per-domain moves
3. Notable posts
4. Emerging tools
5. Opportunities
6. Board take
7. Risks and caveats
8. Next actions

Notable posts must be real rows in `posts.jsonl` with their URLs. The board section includes the simulated-board disclaimer. Opportunity totals come from `opportunities/scores.json`.

State that the research snapshot date is 2026-11-24 unless a newer import replaced it.
