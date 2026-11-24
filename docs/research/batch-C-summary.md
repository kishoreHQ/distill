# Batch C summary — DISTILL research (2026-11-24, IST)

| handle | id | display name | account_type | status | posts read | long-form sources | primary / secondary domains | board eligibility | confidence | key limitations |
|---|---|---|---|---|---|---|---|---|---|---|
| @Pavan_Belagatti | pavan-belagatti | Pavan Belagatti | person | verified | 96 | 5 | ai-engineering / automation, content-creation | ai-engineering, automation | high | LinkedIn data via search snippet only; No YouTube transcripts; Employer influence on recommendations |
| @tom_doerr | tom-dorr | Tom Dörr | person | verified | 120 | 4 | ai-engineering / automation, content-creation | ai-engineering, automation | high | Timeline is mostly automated repo summaries; very few first-party opinions; No verified employer/role; Older bands are narrow date samples (min_likes filter unreliable) |
| @JulianGoldieSEO | julian-goldie | Julian Goldie | person | verified | 141 | 3 | content-creation / automation, startup-building | creator, automation | medium | All traffic/income figures self-reported; Posting volume extremely high; samples cover narrow date windows (Aug 2025, May 2024); YouTube/Skool content not fetched (no transcripts) |
| @imJenal | jyotsna-gupta | Jyotsna Gupta | person | verified | 100 | 2 | software-engineering / developer-community | none | medium | Personal site outdated (Gojek era); X sample is mostly personal/humor; 2020-2023 sparse in search results; golangjobs.tech co-founder role from X bio only |
| @mckaywrigley | mckay-wrigley | Mckay Wrigley | person | verified | 89 | 4 | ai-engineering / content-creation, startup-building | ai-engineering, creator, startup, master | high | Only 13 original posts found in last 6 months (low volume or search coverage); Takeoff→MagicLearn rename from third-party source only; No podcast/YouTube transcripts fetched |
| @ironfisto | mukul-lohar | Mukul Lohar | person | verified | 65 | 4 | ai-engineering / security, automation | ai-engineering | medium | No 6-24mo X posts retrieved (search returned none for the window); ServiceNow current vs former conflicts between site and X bio; LiveShortly role not explicitly stated |
| @techie_piyush | piyush-sachdeva | Piyush Sachdeva | person | verified | 94 | 2 | startup-building / content-creation, automation | startup, creator, automation | high | No posts older than 2025-05 sampled; His X Article on first 50 customers returned no body text via API; YouTube not reviewed |
| @akshaymarch7 | akshay-saini | Akshay Saini | person | verified | 92 | 2 | content-creation / ai-engineering, startup-building | creator, startup | high | YouTube content not reviewed; Business revenue not public; Mid band sample is Dec 2025 only |
| @systemdesignone | neo-kim | Neo Kim | person | verified | 97 | 3 | content-creation / ai-engineering | creator | medium | Real-name/background beyond brand not verified; LinkedIn & Substack counts via search snippets; Sponsorship status of promo posts unknown (paid_partnership field not requested) |
| @kirat_tw | harkirat-singh | Harkirat Singh | person | verified | 96 | 5 | startup-building / content-creation, ai-engineering | startup, creator, master | high | Placement and raise figures self-reported; Podcast/YouTube read via search-index transcripts, not full videos; GitHub hkirat link to X not explicit |

Bundles: `profiles/<id>/` (profile.md, sources.yaml, posts.jsonl, status.json). Raw data and generators: `raw-C/` (people/*.py, build.py, mk.py).

## Standout practical insights for Kishore
1. **Micro-SaaS benchmark (Piyush Sachdeva / ReelDrop):** an Instagram DM-automation tool reached ~56 paid users and ~$694 MRR, with net ~$3.8k CAD by day 104. He documented the build in public and holds a day job. This is a realistic target for a DevOps-plus-agents side product. All figures are self-reported.
2. **Agentic DevOps as a service (Pavan Belagatti + Mukul Lohar):**
   - Pavan's issue → agent → PR "software factory" and harness-engineering pattern.
   - Mukul's point that agents need owner-attributable identity, not bearer tokens.
   - Together these make a consulting offer that fits Kishore's DevOps background: agent pipelines with scoped credentials, approval gates and audit trails.
3. **Low-maintenance content engines (Tom Dörr, Neo Kim):**
   - Tom: about 96% of his posts are an automated GitHub-repo summary feed.
   - Neo: recycles his top posts, uses roadmap/case-study formats, and funnels readers to a newsletter (about 257k subscribers) that readers can expense through company L&D budgets.
   - An agent-drafted DevOps/AI newsletter is cheap to start. Neo's and Julian's posts include sponsored or self-promotional content, so treat their tool endorsements with skepticism.

## Blockers / limitations
- **X search:** `min_likes` and relevancy sort were unreliable, so the older bands are narrow date-window samples rather than "best of" sets.
- **X rate limit and API errors:** the shared rate limit was hit once and there was one 503. Both were handled with pauses and retries. About 48 X calls were used in total, under the 90-call budget.
- **Outside sources:** no LinkedIn access beyond search snippets. YouTube and podcasts were read only through search-index transcripts. No Skool or paid content was read.
- **Missing items:**
  - Kirat's pinned post 2100036301181575341 was not found.
  - The body of Piyush's X Article came back empty.
  - Neo has no GitHub.
  - Mukul has no 2023-2025 X sample.
- **Self-reported numbers:** revenue, placement and subscriber figures are self-reported throughout.
- **No external writes:** no GitHub repos were touched and nothing was posted or sent. The only outputs are files on the box.
