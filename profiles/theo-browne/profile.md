---
id: theo-browne
display_name: "Theo Browne (Theo - t3.gg)"
x_username: theo
x_url: https://x.com/theo
x_user_id: "786375418685165568"
other_identities: [https://t3.gg, https://github.com/t3dotgg, https://github.com/pingdotgg/t3code]
website: https://t3.gg
organization: T3 (t3.codes / t3.chat), Ping.gg
role: CEO (self-described "Full time CEO @t3dotcodes & @t3dotchat")
research_date: 2026-11-24
confidence: high
account_type: person
primary_domain: ai-engineering
secondary_domains: [content-creation, startup-building]
board_eligibility: [ai-engineering, creator, master]
status: verified
---

# Theo Browne (@theo)

## A. Identity
- Display name "Theo - t3.gg"; GitHub t3dotgg shows "Theo Browne", "CEO @ Ping.gg" [S1][S2]. X id 786375418685165568, ~443K followers, San Francisco [S1].
- Products: T3 Code (open-source agent control plane, ~76K GitHub stars), T3 Chat [S1][S3]. Also YouTuber/streamer and investor (self-described) [S1].
- Research date 2026-11-24. Confidence: high.

## B. Expertise map
- **Primary:** AI coding tools and agent harnesses — builds T3 Code, a multi-harness UI for Claude Code, Codex, Antigravity, etc. [S3][S4].
- **Secondary:** developer content (YouTube/X) and monetized audience [S1][S14]; TypeScript/web stack and SaaS plumbing [S6].
- **Technical:** harness architecture [S4], multi-model review loops [S5], agent PR automation [S5], Stripe integration pattern [S6].
- **Business:** dev-tool startup CEO; uses audience as distribution for own products [S3][S14].
- **Projects:** T3 Code [S3], T3 Chat [S1], create-t3-app (linked on t3.gg), UploadThing (named in [S6]), tstack [S5].

## C. Core philosophy
- **AI:** models differ in usability, not just capability — choose per role [S7][S8]. Pinned Nov-2026 view: open-weight models are far behind frontier [S17].
- **Software dev:** interface ≠ harness; good harnesses let users bring their own tools [S4]. Moving away from IDEs toward agent UIs [S18].
- **Product:** resisting feature bloat is hard and necessary [S15]; user feedback goes straight to agents for fixes [S16].
- **Careers:** provocative claim that stack-defined engineers are at risk [S9].

## D. Distilled knowledge
- **Principles**
  - Assign models to roles by strength (implementer / tester / copywriter) [observed statement][S7].
  - Benchmarks ≠ developer experience [observed statement][S8].
  - Keep a single source of truth for third-party state (Stripe → KV sync function) [observed statement][S6].
- **Frameworks**
  - Harness = tools + call syntax + parser + result return + tool list [observed statement][S4].
  - Council review: three models from different providers loop until agreement [observed statement][S5].
  - full-send: prove → review → file PR → babysit CI → merge, unattended [observed statement][S5].
- **Tactics**
  - Align the agent first with a "grill-me" questioning skill [observed statement][S12].
  - For iOS apps, give an agent a dedicated Mac with computer use + simulator [observed statement][S13].
  - Price AI subscriptions vs API-equivalent usage before choosing a plan [observed statement][S11].
- **Demonstrated results:** T3 Code at ~76K stars, multi-platform (desktop, iOS, Android, web) [demonstrated result][S3]; stripe-recommendations ~6.5K stars [S2].
- **Tools recommended:** T3 Code, Claude Code, Codex, Antigravity/Gemini, Linux for dev work (Aug 2026 post), Upstash/Redis KV [S3][S6].
- **Warnings:** Stripe webhook race conditions [S6]; all-or-nothing repo access [S10].

## E. Implementation playbooks

### Playbook 1 — Multi-model "council" review before merge (derived from [S5][S7])
- **Problem:** single-model code review misses bugs and shares the author model's blind spots.
- **Preconditions:** access to ≥2 model providers; repo with PR flow; `gh` CLI.
- **Tools:** tstack skills (council, sol-loop, babysit-pr) or equivalent scripts; Claude Code/Codex.
- **Steps:** 1) Implement with model A. 2) Send diff to models B and C for independent review. 3) Loop fixes until reviewers agree or 3 rounds. 4) File PR leading with the problem. 5) Babysit CI and fix real findings.
- **Expected output:** reviewed PRs with fewer regressions.
- **Cost:** 2–3 subscriptions or API spend. **Time:** setup 1–2 h. **Complexity:** medium.
- **Risks:** token cost; infinite review loops (cap rounds).
- **Success metric:** post-merge bug rate; % PRs merged without human edits.

### Playbook 2 — Stripe state sync without webhook split-brain (derived from [S6])
- **Problem:** subscription state drifting between Stripe and the app.
- **Preconditions:** TypeScript backend, auth, KV store.
- **Tools:** Stripe, Redis/Upstash (or any KV).
- **Steps:** 1) Create Stripe customer at checkout and map userId→customerId. 2) Write one `syncStripeDataToKV(customerId)` that fetches current state. 3) Call it on success redirect and on all relevant webhooks. 4) Read entitlement only from KV.
- **Expected output:** one consistent entitlement source.
- **Cost:** free. **Time:** 0.5–1 day. **Complexity:** low–medium.
- **Risks:** Stripe API rate limits; India-specific payment rules (consider Razorpay equivalents).
- **Success metric:** zero "paid but not subscribed" tickets.

### Playbook 3 — Feedback-to-agent loop (derived from [S16][S5])
- **Problem:** slow handling of user bug reports.
- **Steps:** 1) Ask users for repro steps + expected vs actual. 2) Paste/screenshot into agent with repo context. 3) Agent opens PR; council review; merge. 4) Reply publicly with fix.
- **Cost/Time:** minutes per issue once set up. **Complexity:** low. **Risk:** merging unreviewed agent code. **Metric:** median time-to-fix.

## F. Evidence summary
- 19 sources (13 X posts, 3 GitHub, 2 blog, 1 profile). 165 X posts read (100 in last 6 months, 28 in 6–24 months, 37 older), sampled in date windows (see status.json).
- Blog is sparse (most writing goes to X/YouTube) [S19]. Top sources: [S3] T3 Code, [S4] harness essay, [S5] tstack, [S6] Stripe guide, [S7] model roles.

## G. Strengths and weaknesses
- **Strong:** hands-on builder of agent tooling with large OSS adoption [S3]; clear explainer [S4].
- **Limited evidence:** business revenue of T3 products not disclosed in sources read; views are fast-changing and model-of-the-week heavy (many posts react to new model releases).
- **Risks of following blindly:** frequent hot takes/rage-bait self-acknowledged in posts (e.g. [S9]); strong preferences may shift monthly.
- **Conflicts of interest:** promotes T3 Code/T3 Chat (his products) and earns X creator payouts [S14]; YouTube sponsorships (t3.gg links "sponsors").
- **Differs from others:** says open weights are falling behind [S17], opposite of Alex Finn's 2026 open-weights enthusiasm (this batch).

## H. Practical applications for Kishore
1. **AI agents/automation:** adopt council review + PR babysitting (Playbook 1) for any side project to multiply output with little attention.
2. **Software products:** use Playbook 2 if selling SaaS; ship small dev tools around agent workflows (agent skills packs are popular — tstack ~4.3K stars).
3. **Content:** model "explain a confusing concept once, definitively" (harness essay) as an evergreen content format [S4].
- **Board eligibility:** ai-engineering (core), creator (proven developer-content distribution), master (product + distribution combo). Not automation-specialist nor startup (no disclosed business metrics).

## I. Profile evolution
- **2026-11-24 baseline.**
- 2023: web/TypeScript creator, Ping.gg, "turn off notifications" productivity [posts 2023-05].
- 2024: framework/web content, X revenue math [posts 2024-11].
- 2025: Stripe guide; T3 Chat.
- 2026: pivot to agent tooling — T3 Code, "You still use IDEs?" (May), Linux move (Aug), harness essay (Oct), multi-model roles and Gemini praise (Nov) [S3][S4][S7][S18]. Earlier skeptic of MCP, softened in Aug 2026 ("That might change now") [post 2087280199406903762].
