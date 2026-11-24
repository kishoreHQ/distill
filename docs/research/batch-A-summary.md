# Batch A summary — 11 handles (researched 2026-11-24, IST)

Spec: SPEC.md v1. Bundles are in `profiles/<id>/` (profile.md, sources.yaml, posts.jsonl, status.json). Raw API pulls and fetched pages are in `raw-A/` (with `raw-A/lf/` for long-form text).
X API usage for this batch: **55 calls**: 46 in the original pass (1 batch user lookup, 1 batch pinned-post lookup, 44 timeline/search) plus 9 for the @AravSrinivas replacement (1 user lookup, 1 pinned post, 7 searches). That is under the ~90 budget, and the per-minute limit was never exceeded.

| handle | id | display name | account_type | status | posts read | long-form sources | primary / secondary domains | board eligibility | confidence | key limitations |
|---|---|---|---|---|---|---|---|---|---|---|
| @theo | theo-browne | Theo Browne (Theo - t3.gg) | person | verified | 165 | 5 (t3.gg, harness essay, tstack, stripe-recs, T3 Code README) | ai-engineering / content-creation, startup-building | ai-engineering, creator, master | high | YouTube not transcribed; very high post volume, so the sample is thin; T3 revenue undisclosed |
| @AravSrinivas (replaces @aravind) | aravind-srinivas | Aravind Srinivas | person | verified | 130 | 3 (Lex Fridman #434 transcript, Berkeley Engineering profile, IIT Madras alumni page) + Wikipedia (secondary) | ai-engineering / startup-building, productivity | ai-engineering, startup, master | high | Recent X is mostly product promotion; $1B ARR and share figures self-reported; perplexity.ai blog/research returned 403 (not bypassed); ethics flags: fake academic Twitter accounts (self-admitted), crawler/copyright allegations |
| ~~@aravind~~ | x-aravind | Aravind | person | **excluded** (was unverified) | 68 | 0 | – | none | low | Wrong handle; user replaced with @AravSrinivas on 2026-11-24. Bundle kept, not used |
| @Saboo_Shubham_ | shubham-saboo | Shubham Saboo | person | verified | 86 | 3 (awesome-llm-apps README, GitHub, Unwind AI) | ai-engineering / automation, content-creation | ai-engineering, automation, creator | high | Many posts amplify third-party tools; Google-employer bias; books not read |
| @Ozacle23 | ojasvika | Ojasvika (Oz) | person | partial | 76 | 1 (product site, title only, JS-rendered) | startup-building / content-creation | startup (low weight) | medium | No surname; early-stage; traction self-reported; sample only goes back to Oct 2025 |
| @HiTw93 | tw93 | Tw93 | person | verified | 85 | 5 (21-practices article, Mole OSS→paid article, blog index, Waza, Pake) | ai-engineering / startup-building, productivity | ai-engineering, startup, automation | high | Pseudonymous; long-form in Chinese; revenue undisclosed |
| @GitTrend0x | gittrend | GitTrend | **aggregator** | verified (as aggregator) | 66 | 1 (linked Claudebot repo) | ai-engineering (signal feed only) | none | medium | Run by @0xKingsKuan; ex-crypto account; promotes crypto signal/audit services; possibly automated |
| @heynavtoor | nav-toor | Nav Toor | person (creator) | verified | 69 | 1 (third-party sponsorship listing) | content-creation / – | creator (format case study) | medium | No website or long-form; sponsored posts; no first-party expertise |
| @_swanand | swanand | Swanand | person | partial | 86 | 1 (superlinear.tech) | automation / ai-engineering, startup-building | automation | medium | No surname; X mostly off-topic; company metrics are marketing claims |
| @DavidOndrej1 | david-ondrej | David Ondrej | person | verified | 86 | 5 (Cloudroom README, skills README, YouTube transcript via Rosetta, Skool page, Skool tracker) | ai-engineering / content-creation, startup-building | ai-engineering, creator | high | ARR/subscriber claims self-reported; tracker shows his community shrinking |
| @AlexFinn | alex-finn | Alex Finn | person | verified | 85 | 3 (alexfinn.ai post, Skool about/plans, Skool profile via search) | content-creation / startup-building, automation | creator, startup | high (identity) / medium (metrics) | $300K ARR and funding are self-reported; hype claims; no verified GitHub |
| @levelsio | pieter-levels | @levelsio (Pieter Levels) | person | verified | 116 | 8 (levels.io home + 7 posts) | startup-building / automation, ai-engineering, productivity | master, startup, automation | high | Revenue self-reported; his distribution is hard to replicate; podcasts not processed |

Totals: 11 active handles + 1 excluded. 9 verified (counting the aggregator as verified-as-aggregator), 2 partial, 0 blocked; @aravind excluded. 1,050 X posts read for active profiles (1,118 including the excluded bundle). 36 long-form fetches.
Domain distribution (primary): ai-engineering 6 (theo, saboo, tw93, ondrej, srinivas, gittrend-feed), startup-building 2 (levels, oz), content-creation 2 (finn, nav), automation 1 (swanand).

## Method notes (affects every profile)
- The X search ignored `sort_order: relevancy` and `min_likes:`. Every call returned the 25 posts just before `end_time`. Samples are therefore chronological slices in 3–7 date windows per person (last few days, ~mid-2026, ~mid-2025, ~mid-2024 or older), not "top posts". For heavy posters (theo, levelsio) each slice covers only 2–5 days.
- Pinned posts were fetched for every active account that has one (11 of 11; the excluded @aravind has none).
- GitHub data came from the public API. The `swanand` and `alexfinn` GitHub logins could not be tied to these people, so they were not used.
- No YouTube or podcast transcripts were processed directly. One David Ondrej video was read via a third-party transcript page.
- Fetched pages were treated as untrusted data. No embedded instructions were encountered or followed.

## Standout practical insights for Kishore
1. **Zero-employee ops with LLM cron "robots" plus agent-run cost audits (levelsio).** Scheduled LLM scripts handle moderation, sales and email triage, with self-serve billing and refunds. A Claude Code audit of his vendor bills cut about $34K/mo by rerouting GPU models, consolidating on Hetzner, adding backup lifecycle rules and pruning domains. These figures are self-reported. This fits Kishore's Linux/DevOps skills directly: the first product could be "agent cost and infra audits" for small SaaS teams in India.
2. **Open-core path from free CLI to paid desktop app (Tw93).** Tw93 has several open-source repos with 60K+ stars. For Mole he kept the free CLI and sold a GUI for users who don't work in the terminal. He says it grew by word of mouth with no paid marketing and a refund rate under 0.8% (self-reported). He answered support by hand and only automated once a question repeated, its answer was stable and the exceptions were known. Low capital and low maintenance, but slow. It suits a DevOps CLI built by Kishore.
3. **Distribution comes before product (Alex Finn's reply ladder + David Ondrej's "≥50% of time on distribution, one channel").**
   - Do 2 posts a day plus 10–20 real replies in one niche, and log the audience's recurring pains. Build for the most common pain after 8–12 weeks.
   - Do the replies by hand. levelsio now publicly block-lists accounts that post AI-generated replies.
   - Separately, Theo and Tw93 both show that agent quality depends on enforcement more than prompts: multi-model review, verify scripts and regression tests for every bug.

## Addendum 2026-11-24 14:45 IST: @AravSrinivas insights
4. **Pick an "AI-complete" niche with strict grounding (Srinivas).** Build something that improves automatically as models improve, and answer only from retrieved sources with citations. For Kishore, that means a cited answer engine for Linux, DevOps or incident runbooks. Validate with organic, unprompted usage and treat daily complaints as a roadmap signal.
5. **Make DISTILL's own agents safer: council + safe-fetch (Srinivas).** Reconcile high-stakes outputs across 2–3 models with a chair model, and score fetched pages for prompt injection before an agent reads them. This applies directly because DISTILL ingests untrusted web text. Avoid Perplexity's contested scraping practices; they conflict with DISTILL's source-permission rule.

## Blockers / flags for the parent
- **@aravind resolved:** Kishore confirmed the intended account is @AravSrinivas. New bundle is `profiles/aravind-srinivas/`. `x-aravind` is marked `research_status: "excluded"` in status.json, with a note at the top of profile.md. It is kept, not deleted. Its front-matter `status` stays `unverified` because SPEC v1 has no "excluded" value.
- **@GitTrend0x is an aggregator.** Use it only as a feed and keep it off every board. The daily-trend format is easy to rebuild in-house as part of the intelligence pipeline (playbook in its profile).
- **Weak first-party evidence:** Swanand, Ojasvika and Nav Toor are thin. A browser pass would help: projectminimi.com is JS-rendered, and talks or podcasts may exist. They stay partial or low-weight for now.
- Nothing was written to any GitHub repo. All output is box-only.
