---
id: pieter-levels
display_name: "@levelsio (Pieter Levels)"
x_username: levelsio
x_url: https://x.com/levelsio
x_user_id: "1577241403"
other_identities: [https://levels.io, https://github.com/levelsio, https://readmake.com]
website: https://levels.io
organization: Solo founder (Nomads.com, Remote OK, Photo AI, Interior AI, Hoodmaps)
role: Solo bootstrapped founder / developer
research_date: 2026-11-24
confidence: high
account_type: person
primary_domain: startup-building
secondary_domains: [automation, ai-engineering, productivity]
board_eligibility: [master, startup, automation]
status: verified
---

# Pieter Levels (@levelsio)

## A. Identity
- Display name on X: "@levelsio"; blog title identifies him as Pieter Levels [S2]. X user id 1577241403, joined 2013-07-08, ~995K followers at research time [S1].
- Website/blog: levels.io (191K email subscribers claimed on the page) [S2]. Book: MAKE (readmake.com, linked from bio) [S1].
- Organization/role: solo founder of Nomads.com, Remote OK, Hoodmaps, Photo AI, Interior AI, "all bootstrapped without funding" [S2].
- GitHub: levelsio — only 3 small public repos; the products are closed source [S17].
- Research date: 2026-11-24. Confidence: high (identity unambiguous, large first-party long-form archive).

## B. Expertise map
- **Primary:** bootstrapped solo SaaS / indie hacking — idea → ship → monetize with zero staff [S2][S4][S8].
- **Secondary:** ops automation with LLM cron "robots" [S4]; agentic coding on servers (Claude Code on VPS) [S5][S9][S13]; infra cost minimisation [S3].
- **Technical:** single-VPS deployments (Hetzner), Cloudflare (R2, tunnels, DNS via API), integrating third-party image/video models into consumer AI apps [S3][S15][S16].
- **Business:** validation with payment links before building [S11]; public revenue transparency ("build in public") [S1][S12]; high-margin, self-serve products [S4].
- **Products/projects:** Nomads.com, Remote OK, Photo AI, Interior AI, Hoodmaps (per blog) [S2]; Nov 2026 X AI-reply-spam block list [S14].
- **Communities:** indie hackers / build-in-public X, digital nomads.

## C. Core philosophy
- **Entrepreneurship:** ship many small bets; most fail (~5% hit rate) so volume matters [S8]. Projects should start as play without success pressure [S7].
- **Monetization:** charge early via simple payment links; validate before building out [S11]. Self-serve billing and refunds to avoid human support [S4].
- **Automation:** aim for "100% automation" with zero employees; scheduled LLM scripts replace roles such as moderation and sales [S4]. Every inbound email should be LLM-triaged [S10].
- **Software development:** extreme simplicity, edit-in-production; now lets the agent edit production on the VPS, while explicitly recommending staging for teams [S5][S9].
- **AI and markets (2026 view):** most SaaS cannot survive general AI from big labs; "riches in the niches" no longer a moat — and he says he is unsure even of survivors [S6].

## D. Distilled knowledge
- **Principles**
  - Ship more; expect ~95% of projects to fail [observed statement][S8].
  - Do not put success requirements on new projects; let them start as play [observed statement][S7].
  - 0 humans, 100% automation, 99% margin as the design target [observed statement][S4].
- **Mental models**
  - Hit-rate thinking: portfolio of many cheap bets over one big bet [our interpretation][S8].
  - "Costs slowly creep": periodic audits find large waste (infinite backup versioning, unused domains, over-provisioned plans) [demonstrated result, self-reported][S3].
  - Niche-SaaS moat erosion by general AI [observed statement][S6].
- **Frameworks / workflows**
  - Validation-first launch: Notion page + Stripe Payment Link at a fixed price; build only if people pay [demonstrated result][S11].
  - Worker-robot cron: LLM scripts on hourly/daily/weekly schedules doing moderation, sales, etc. [observed statement][S4].
  - Agent-on-server dev loop: SSH (even from phone) into VPS, run Claude Code, ship live in seconds; keep 3-2-1 backups [demonstrated result][S5][S13].
  - Agent-led cost audit: give the coding agent read access to vendor accounts/bills and ask it to find savings [demonstrated result, self-reported $34K/mo][S3].
- **Tools recommended:** Hetzner VPS, Cloudflare (R2 lifecycle rules, API token for agents, Tunnel), Claude Code, Stripe Billing Portal, Featurebase feedback board, Termius [S3][S4][S13][S16].
- **Mistakes warned about:** paying for expensive PaaS instead of VPS (blog headline, not fully read); infinite backup versioning; leaving old pricey model routes in place [S3]; open VPS ports (blog headlines) [S2].

## E. Implementation playbooks

### Playbook 1 — Payment-link validation for a micro product (derived from [S11][S8])
- **Problem:** building products nobody pays for.
- **Preconditions:** an idea for a niche list/board/tool; audience channel (X, community, newsletter).
- **Tools:** Notion or a static page, Stripe Payment Link (or Razorpay/Lemon Squeezy for India), X.
- **Steps:** 1) Write a one-page offer with a fixed price. 2) Attach a payment link. 3) Post it publicly with the "if validated I'll build it out" framing. 4) Count payments over 7–14 days. 5) Only then automate/build the real product.
- **Expected output:** go/no-go signal backed by money, not likes.
- **Cost:** ~$0 plus payment fees. **Time:** 2–4 hours. **Complexity:** low.
- **Risks:** small audience → false negatives; Levels' results benefit from ~1M followers (survivorship).
- **Success metric:** ≥N paid orders (set N before launch, e.g. 5) within 14 days.

### Playbook 2 — LLM "worker robots" on cron (derived from [S4][S10])
- **Problem:** recurring human ops (moderation, triage, follow-ups) consume founder time.
- **Preconditions:** a product with repetitive ops; API key for an LLM; a server.
- **Tools:** VPS + cron/systemd timers, LLM API, Stripe Billing Portal, email API.
- **Steps:** 1) List recurring tasks weekly. 2) For each, write a script: fetch inputs → LLM classify/act → log decision. 3) Schedule hourly/daily. 4) Add a human-review queue for low-confidence cases. 5) Make billing/refunds self-serve.
- **Expected output:** near-zero manual ops per week.
- **Cost:** VPS ~$5–20/mo + token spend. **Time:** 1–2 days per workflow. **Complexity:** medium.
- **Risks:** silent LLM errors (e.g. wrongly rejecting customers); needs logging and spot checks.
- **Success metric:** hours/week of manual ops before vs after; error rate on sampled decisions.

### Playbook 3 — Agent-led infra cost audit (derived from [S3])
- **Problem:** creeping SaaS/infra costs.
- **Preconditions:** list of vendors and invoices; read-only API tokens.
- **Tools:** Claude Code or similar agent, provider CLIs/APIs (Cloudflare, Hetzner, B2/S3).
- **Steps:** 1) Export last 3 months of bills. 2) Ask the agent to rank spend and propose savings (model routing, lifecycle policies, consolidation, unused domains/plans). 3) Apply changes one at a time with rollback notes. 4) Re-audit quarterly.
- **Expected output:** prioritized savings list and applied changes.
- **Cost:** agent subscription. **Time:** half a day. **Complexity:** low–medium.
- **Risks:** agent with write tokens can break production — start read-only.
- **Success metric:** monthly spend delta.

## F. Evidence summary
- 17 sources in sources.yaml (8 blog/website, 8 X posts, 1 GitHub). 116 X posts read (posts.jsonl) across 2023-02 → 2026-11.
- Top sources: [S3] cost audit, [S4] automation stack, [S5] VPS agent workflow, [S8] hit rate, [S6] SaaS-vs-AI view.

## G. Strengths and weaknesses
- **Strengths:** unusually long, public, quantitative record of solo bootstrapping; concrete, copyable ops patterns [S3][S4][S12].
- **Consistently right about:** simplicity, low cost, shipping speed, monetizing early.
- **Limited evidence:** revenue numbers are self-reported (bio, posts) and not independently verified here [S1][S12]. His distribution advantage (~1M followers, 191K email list) makes his launch results hard to replicate [S1][S2].
- **Approach limits:** edit-in-production with bypass permissions is risky; he himself says teams should use staging [S5][S9].
- **Conflicts of interest:** sells the book MAKE; runs an investment fund (levels.vc, blog link) [S2]; promotes his own products.
- **Disagreements:** his 2026 "SaaS can't survive AI" pessimism [S6] contrasts with builders still selling AI SaaS (e.g. David Ondrej, Alex Finn in this batch).
- Large share of X output is non-business (politics/Europe, travel, fitness) — low signal for this project.

## H. Practical applications for Kishore
1. **AI income:** run Playbook 1 for small paid utilities/boards aimed at Indian devs/DevOps; charge from day one.
2. **Automation/time:** Playbook 2 for any product Kishore runs; Playbook 3 on his own cloud bills (fits his Linux/DevOps skills).
3. **Products:** VPS-first, single-server deployments keep costs ~$5–50/mo — aligns with low-capital constraint.
4. **Caution:** his 2026 view [S6] argues against generic niche SaaS; prefer products with distribution, data or workflow lock-in.
- **Board eligibility:** master (long track record in solo leverage), startup (core expertise), automation (zero-employee ops). Not ai-engineering (uses AI tools but no AI-systems depth shown) nor creator (huge audience, but no teachable creator method was extracted here).

## I. Profile evolution
- **2026-11-24 baseline.**
- 2014 → 2021: "12 startups in 12 months", ship-many approach; ~5% hit rate post (2021) [S2][S8].
- 2023: riding image models (Photo AI) with public MRR posts; validation-first micro launches [S11][S12].
- 2024: formalized "0 humans, 100% automation" stack [S4].
- 2026: moved to agent-on-VPS coding, bypass permissions [S5][S9]; agent-led cost cutting [S3]; new pessimism that most SaaS can't survive AI [S6]; anti-AI-reply-spam campaign on X [S14].
