# Limitations and caveats

These are limits of the 2026-11-24 snapshot and of Phase 1 code. They are also copied, in shorter form, into `knowledge/risks.yaml` and the daily briefing.

## The sample is not the whole account

Batch A, B, and C each say the search returned chronological slices. Theo, Levels, Julian Goldie, and other high-volume accounts are under-sampled relative to how much they post. Older bands are narrow. Some pinned posts returned "Not Found". Some long posts are truncated at 280 characters in `posts.jsonl`.

## Numbers are mostly self-reported

ARR, MRR, follower counts inside profile essays, placement rates, and refund rates came from the person or from their own site, unless a source is marked secondary. Phase 1 scripts do not re-verify them. Opportunity scores refuse to treat them as Kishore's expected income. The scoring notes say this per file.

Follower counts that appear inside an imported `profile.md` were written by the research bundles. This phase did not add new ones. Arnav Gupta's extra bundle had none, so his profile has none.

## Identity gaps

- `x-aravind` is excluded. The bio in that bundle disclaims its own accuracy.
- `x-wojakcodes` is a pseudonym with no products found. Research status partial. Not on a board.
- Swanand and Ojasvika have no surname in the sources. Ojasvika's product site was JS-rendered and only the title was stored. On 2026-11-26 an official read returned no post older than 2025-10-29. Her timeline looks exhausted. Status stays partial.
- Suman Chakraborty's useful sources are talk listings. His X sample is thin. A 2026-11-26 deepen read added 25 older posts, mostly tool links. Status stays partial.
- Arnav Gupta: a 2026-11-24 post speaks of Railway in the first person, including self-reported template payouts. The bundle README timeline that ends at Meta is still in the sources and is not retracted. YouTube lines still lack speaker labels. `sync.json` still says 200 posts were read; that file was not in the archive. `posts.jsonl` now has the original quotes plus the 2026-11-25 official-API sample, not those 200 rows.
- GitHub logins for some handles could not be tied to the person. The batches say those logins were not used. This phase does not retry that tie.

## Aggregators

`gittrend` (operated by @0xKingsKuan, per the profile) and `x-githubprojects` post other people's repositories. They are in the matrix as signal feeds. A high impression count on an aggregator post is not a person's reach.

## Ethics and terms

The Srinivas ledger includes a secondary source on crawler allegations against Perplexity. DISTILL does not copy that behaviour. `config/sources.yaml` forbids login-wall scraping and anti-bot bypasses. Tom Dörr's feed links dual-use security tools. The devtools board says those links are not build instructions.

## Conflicts of interest

Course sellers, community sellers, and vendor employees are identified on their profiles when the bundle identified them. Boards repeat the conflict next to the advice. That is not a claim about their motives beyond what they sell in public.

## What Phase 1 does not know

Anything posted after the snapshot, except rows a later refresh actually appended. Private conversations. Paywalled newsletters that were not fetched. Whether a sponsorship was paid when the bundle says the field was not requested. The dashboard has no UI.

## 2026-11-26 refresh

Rows appended that day come from an official public X read. The window is 2026-11-24T22:19:55Z to 2026-11-26T00:20Z. Suman Chakraborty also received 25 older posts. Those are mostly tool-link and event posts, so his research status stays partial. Ojasvika's older read returned no post before the repo's oldest row, 2025-10-29. Her official timeline looks exhausted, and her status stays partial. Julian Goldie and Theo Browne were capped at 100 rows. Post text in `posts.jsonl` is capped at 280 characters. Dollar figures, token counts, and the 75% harness line are the authors' own. Theo's telemetry sentences that day do not agree with each other. Arnav Gupta's missing 200-post file is still missing.

## 2026-11-25 refresh

Rows appended that day come from an official public X read. The window starts 2026-11-23T22:21:18Z. Two partial profiles also received older rows marked deepen. Theo's file was capped at 125 posts in the collection. Post text in `posts.jsonl` is capped at 280 characters. Dollar figures and token counts in that window are the authors' own.
