---
id: david-ondrej
display_name: David Ondrej
x_username: DavidOndrej1
x_url: https://x.com/DavidOndrej1
x_user_id: "1648699406760255488"
other_identities: [https://github.com/davidondrej, https://www.youtube.com/@DavidOndrej, https://www.skool.com/new-society, https://www.cloudroom.dev]
website: https://www.cloudroom.dev
organization: Cloudroom
role: Founder (self-described "founder of Cloudroom" on GitHub)
research_date: 2026-11-26
confidence: high
account_type: person
primary_domain: ai-engineering
secondary_domains: [content-creation, startup-building]
board_eligibility: [ai-engineering, creator]
status: verified
---

# David Ondrej (@DavidOndrej1)

## A. Identity
- David Ondrej; X id 1648699406760255488, ~71K followers [S1]. GitHub davidondrej ("founder of Cloudroom", links cloudroom.dev — matches X) [S2].
- YouTube creator on AI coding (community page claims 400K+ subscribers, 600+ videos — self-reported) [S4]. Runs paid Skool community New Society ($37/mo) [S4].
- Confidence high (X ↔ GitHub ↔ website consistent).

## B. Expertise map
- **Primary:** agentic coding workflows and harnesses; builds Cloudroom (cloud sandboxes for any harness) [S2][S7].
- **Secondary:** AI-education content and paid community [S4][S6]; AI SaaS founding (claims $70K ARR in <1 month for Cloudroom, self-reported) [S4].
- **Technical:** multi-harness operation (Claude Code, Codex, Pi, OpenCode, Cursor) [S2][S10]; agent skills design (questioning, ADRs, prompt deepening) [S3].
- **Projects:** Cloudroom (~1.8K★), skills (~4.4K★), superbot (self-hosted assistant), autogit [S2][S3].

## C. Core philosophy
- **2026-11-26.** He markets an agent that is "100% abliterated", runs 24/7 on your own VPS, and never says no [S16] (https://x.com/DavidOndrej1/status/2125731090719506935). That is a product claim, and it cuts against a human gate. He also posts that faking GitHub stars is the lowest of lows [S17] (https://x.com/DavidOndrej1/status/2125512871153148056). That is his accusation in the T3 Code dispute. This repo does not adopt it as a fact about anyone else. Much of the window is short reactions and Cloudroom links. [observed statement]
- **2026-11-25.** He says Cloudroom is growing faster than ever and gives no number [S14] (https://x.com/DavidOndrej1/status/2125338006047654149). He calls something the most underrated model and does not name it in the text [S15] (https://x.com/DavidOndrej1/status/2125186109407724018). The highest-impression new post is a delivery anecdote, not a method, and is not distilled into a principle. [observed statement]
- **AI:** use multiple labs' models for diversity [S8]; don't be locked to one vendor — switch harness at limits [S10].
- **Software dev (provocative):** rewrite codebases when frontier models jump [S9] — treat as opinion, not a tested method.
- **Entrepreneurship/monetization:** distribution ≥50% of time; master one channel where your customer lives [S6].

## D. Distilled knowledge
- **2026-11-26.** Cloudroom remains the product he points at. A reply says he uses Antigravity every day inside Cloudroom. That reply is in `posts.jsonl` and is not a new architecture.
- **Principles**
  - "At least 50% of your time should be on distribution" [observed statement][S6].
  - Pick one acquisition channel matched to target customer (e.g. LinkedIn for lawyers) [observed statement][S6].
  - Model diversity across labs improves idea breadth [observed statement][S8].
- **Workflows**
  - Pre-build interrogation: 4 rounds × 4 questions to extract decisions, then plan (4x4 skill) [observed statement][S3].
  - Record decisions verbatim as ADRs during agent work [observed statement][S3].
  - Cloud sandboxes per agent session with own git branch; sessions move between laptop and cloud [observed statement][S2].
- **Tools:** Cloudroom, Claude Code, Codex, Pi, OpenCode, n8n (2025) [S2][S10][S13].
- **Demonstrated results:** OSS repos with thousands of stars [S2][S3]; ARR claims are self-reported only [S4].

## E. Implementation playbooks

### Playbook 1 — Decision-first agent build (derived from [S3])
- **Problem:** agents build the wrong thing from vague prompts.
- **Preconditions:** a coding agent that loads SKILL.md files.
- **Tools:** `npx skills add davidondrej/skills` (4x4, ask-then-build, adr-verbatim) or hand-written equivalents.
- **Steps:** 1) Before any build, agent asks 4 sets of 4 questions. 2) Agent writes plan + ADRs of your answers. 3) Hand plan to implementer agent. 4) Review against ADRs.
- **Expected output:** plan and decisions log; fewer rewrites.
- **Cost:** free. **Time:** 15–30 min per feature. **Complexity:** low.
- **Risks:** question fatigue on small tasks — use only for features.
- **Success metric:** rework rate per feature.

### Playbook 2 — Distribution-first AI SaaS launch (derived from [S6])
- **Problem:** builders spend all their time coding and get no users.
- **Steps:** 1) Define target customer and where they spend time. 2) Choose ONE channel. 3) Time-box: half of each week on content/DMs/calls. 4) Track leads per channel weekly.
- **Cost:** time. **Complexity:** low. **Risks:** slow feedback if channel is wrong; switch only after a set period. **Metric:** qualified conversations/week, paying users.

## F. Evidence summary
- **2026-11-26 refresh.** Appended 32 posts (32 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 159 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z.
- **2026-11-25 refresh.** Appended 41 posts (41 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 7 collected ids were already stored. `posts.jsonl` now has 127 rows.
- 13 sources (7 X posts, 2 GitHub, 2 website, 1 YouTube transcript, 1 secondary tracker). 86 X posts read (51 last 6 months, 20 6–24 mo, 15 older).
- Top: [S2] Cloudroom, [S3] skills, [S6] AI SaaS video, [S4] community claims.

## G. Strengths and weaknesses
- **Strong:** real shipped OSS agent infrastructure; practical skill library.
- **Limited evidence:** revenue and subscriber numbers are self-reported [S4]; a third-party tracker shows his community shrinking Aug→Nov 2026 [S5].
- **Risks:** hype-style takes ("AGI really is here", "rewrite your entire codebase") [S9]; some posts are off-topic culture-war content (seen in Nov 2026 sample).
- **Conflicts of interest:** sells a paid community promoted in videos [S4][S6]; discount/affiliate promos [S12]; promotes his own Cloudroom.

## H. Practical applications for Kishore
1. **AI agents:** adopt Playbook 1 skills (free, OSS) to reduce agent rework.
2. **Infra/DevOps opportunity:** Cloudroom validates demand for "cloud sandboxes for agents" — Kishore's DevOps skills fit self-hosted agent sandboxes/consulting for teams (evidence: product exists and claims fast ARR — unverified).
3. **Startup:** distribution-first rule (Playbook 2) for any product he ships.
- **Board eligibility:** ai-engineering (harness tooling), creator (large YouTube education business, self-reported). Not startup (revenue unverified), not master.

## I. Profile evolution
- **2026-11-24 baseline.**
- 2024: generalist AI commentary (Gemini, Ilya, "uneducated" about AI/Bitcoin) [posts 2024-05].
- 2025: Claude Code tutorials, n8n, AI-millionaires content [S11][S13].
- 2026: founder of Cloudroom (Oct launch); multi-harness, multi-model stance; sharp criticism of Anthropic pricing/speed in mid-2026 [S7][S10].
- **2026-11-25.** No new distribution rule. One self-reported growth line without a figure [S14]. Many of the 48 collected rows were replies or were already stored.
- **2026-11-26.** Distribution and the paid community were already the focus [S6][S5]. The new product sentence is an agent that never refuses [S16]. No shift away from selling the audience a tool. The star-faking line [S17] is recorded as his words only.
