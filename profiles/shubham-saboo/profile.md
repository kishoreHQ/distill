---
id: shubham-saboo
display_name: Shubham Saboo
x_username: Saboo_Shubham_
x_url: https://x.com/Saboo_Shubham_
x_user_id: "1275333333724000257"
other_identities: [https://github.com/Shubhamsaboo, https://www.theunwindai.com]
website: https://www.theunwindai.com
organization: Google Cloud
role: Senior AI Product Manager (self-described on X and GitHub)
research_date: 2026-11-27
confidence: high
account_type: person
primary_domain: ai-engineering
secondary_domains: [automation, content-creation]
board_eligibility: [ai-engineering, automation, creator]
status: verified
---

# Shubham Saboo (@Saboo_Shubham_)

## A. Identity
- Shubham Saboo; X id 1275333333724000257, ~125K followers [S1]. GitHub Shubhamsaboo: "Senior AI PM @ Google Cloud" [S3]. Joined Google Cloud Sept 2025 to work on agents (Gemini, Vertex AI, ADK, A2A) [S5].
- Maintainer of awesome-llm-apps (~145.6K★) [S2]; co-runs Unwind AI newsletter [S4]. Bio: author of books on GPT-3 and neural search [S1] (books not verified here).
- Confidence high.

## B. Expertise map
- **Primary:** practical agent/RAG application patterns, curated as runnable templates [S2].
- **Secondary:** personal "agent company" automation (cron agents, Telegram control) [S6][S7]; AI content/curation distribution [S4][S13].
- **Technical:** multi-agent orchestration patterns (advisor/orchestrator/worker) [S9]; agent memory layers [S10]; Google ADK, A2A [S5][S12].
- **Business:** AI product management (hiring criteria) [S11]; open-source as distribution engine [S2].
- **Projects:** awesome-llm-apps, Unwind AI, Kaggle agents course (Google) [S2][S4][S12].

## C. Core philosophy
- **2026-11-27.** He announces a Gemini quota reset for all Antigravity users and points them at Gemini 4 Neon for the weekend [S16] (https://x.com/Saboo_Shubham_/status/2125853266030559661). An employer product notice. No new usage percentage. Most other rows are short replies. [observed statement]
- **2026-11-26.** He says Antigravity raised Gemini 4 Neon usage on the subscription by close to 75% in five days, by caching and harness improvements [S15] (https://x.com/Saboo_Shubham_/status/2125646788795523373). The percent is his. He also says Google Chrome released an open-source Modern Web Guidance skill for coding agents [S16] (https://x.com/Saboo_Shubham_/status/2125490308788162704). The other 15 rows are short replies. [observed statement]
- **AI:** agents must be self-improving; static agents "won't survive" [S8]. Mix models by role and cost [S9].
- **Automation:** a solo operator can run "0 human employees" with role-folders, markdown job descriptions and cron jobs [S6].
- **Content/OSS:** give away high-quality runnable templates ("Clone it, ship it, sell it") [S2].
- **Product:** good AI PMs pick the right problem, ship demos, explain failure modes [S11].

## D. Distilled knowledge
- **Tools, 2026-11-26.** Antigravity harness and cache, as the cause he names for the usage jump [S15]. Chrome's Modern Web Guidance skill [S16]. Both are employer-adjacent. They are not a personal stack recipe.
- **Tools, 2026-11-25.** He says Google Workspace MCP server and CLI are generally available, with DLP and human-in-the-loop controls [S14] (https://x.com/Saboo_Shubham_/status/2125298072188231810). Employer announcement. The other new row is a thank-you and is not used. [observed statement]
- **Frameworks**
  - Agent company as filesystem: each role = folder, each job description = .md, schedules = cron, review/retro loop per agent [observed statement][S6].
  - Advisor / orchestrator / worker model tiers (expensive model advises, mid model orchestrates, cheap fast model executes) [observed statement][S9].
  - Memory layers: session, semantic, procedural (self-written skills), episodic [observed statement — describing Google's product][S10].
- **Tactics:** control agents through messaging apps (Telegram) for 24/7 use [S7]; package workflows as installable agent skills [S9].
- **Demonstrated results:** awesome-llm-apps ~145.6K★ — a proven distribution asset [demonstrated result][S2]; launched free Kaggle course with Google [S12].
- **Content pattern:** "X just dropped / 100% open source / repo link" posts and numbered "10 use cases" threads [our interpretation from posts.jsonl].
- **Tools:** Google Antigravity, Gemini models, OpenClaw, Hermes Agent, ADK, Telegram [S5][S7].

## E. Implementation playbooks

### Playbook 1 — Solo "agent company" with role folders (derived from [S6][S7][S9])
- **Problem:** one person can't cover research, content, ops, support.
- **Preconditions:** an always-on box/VPS; an agent runtime (Hermes/OpenClaw/Claude Code); messaging bot.
- **Tools:** cron/systemd, agent runtime, Telegram bot, git for state.
- **Steps:** 1) Create `/agents/<role>/JOB.md` with goal, inputs, outputs, quality bar. 2) Schedule each role via cron. 3) Route outputs to Telegram for approval. 4) Weekly "retro" prompt where each agent reviews its logs and edits its JOB.md. 5) Tier models: cheap worker, expensive reviewer.
- **Expected output:** recurring deliverables (briefs, drafts, reports) with human approval only.
- **Cost:** VPS $5–20/mo + tokens. **Time:** 1–2 days. **Complexity:** medium.
- **Risks:** runaway token spend; unattended agents with credentials; quality drift — keep approvals.
- **Success metric:** hours saved/week; approval-without-edit rate.

### Playbook 2 — OSS template repo as distribution (derived from [S2][S4])
- **Problem:** no audience for products/newsletter.
- **Steps:** 1) Publish small, tested, runnable agent templates in one repo. 2) Each template gets a tutorial post/newsletter. 3) Cross-post short demos on X. 4) Add newsletter signup and sponsorship page once traffic exists.
- **Cost:** time only. **Time:** ongoing (weekly template). **Complexity:** medium. **Risks:** maintenance burden, model churn breaks templates. **Metric:** stars, newsletter subscribers, sponsor inquiries.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 19 posts (19 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 124 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-26 refresh.** Appended 17 posts (17 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 105 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z.
- **2026-11-25 refresh.** Appended 2 posts (2 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 88 rows.
- 13 sources (9 X posts, 2 GitHub, 1 newsletter, 1 profile). 86 X posts read (51 last 6 months, 20 6–24 mo, 15 older).
- Top: [S2] repo, [S6] agent company, [S9] model tiers, [S5] Google role.

## G. Strengths and weaknesses
- **Strong:** prolific, practical curation; huge OSS asset; insider view of Google agent stack.
- **Weak/limited:** many posts are hype-format reposts of others' tools ("INSANE", "Crazy") — the evidence that a featured tool works is usually not his own testing [our interpretation].
- **Conflicts of interest:** Google employee promoting Gemini/Antigravity heavily in late 2026 [S10]; newsletter sponsorships [S4].
- **Note:** some posts repeat others' claims (e.g. star counts of third-party repos) — don't treat as verified.

## H. Practical applications for Kishore
1. **Automation/AI agents:** Playbook 1 is directly buildable on Kishore's Linux skills — a VPS agent team for research briefs, content drafts, monitoring.
2. **Content/income:** Playbook 2 — a DevOps-agent template repo (e.g. "awesome-devops-agents") as an audience engine; monetize later via newsletter sponsors or consulting.
3. **Learning:** use awesome-llm-apps templates as starting code instead of building from scratch.
- **Board eligibility:** ai-engineering (agent patterns), automation (agent company), creator (OSS + newsletter distribution). Not startup (no disclosed revenue business).

## I. Profile evolution
- **2026-11-24 baseline.**
- 2024: Claude 3.5 Sonnet demos, free-course roundups, local LLMs [posts 2024-06].
- 2025: joined Google Cloud (Sept); ADK/A2A, Kaggle course, MCP tools curation [S5][S12].
- 2026: personal agent teams (OpenClaw→Hermes), self-learning agents, model tiering; late-2026 strongly Gemini/Antigravity focused [S6][S7][S8][S10].
- **2026-11-25.** Adds a named MCP surface with an explicit human-in-the-loop control [S14] on top of the cron-and-folder setup [S6]. Not a change of employer.
- **2026-11-26.** Before, Workspace MCP was generally available with a human-in-the-loop control [S14]. After, the harness itself is the usage story: caching and harness work, not a new model name, is what he credits for the 75% line [S15]. The employer conflict is unchanged.
- **2026-11-27.** No new harness percentage. The 75% line [S15] stands as his earlier claim. This window is a quota reset [S16].
