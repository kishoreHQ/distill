---
id: "mckay-wrigley"
display_name: "Mckay Wrigley"
x_username: "mckaywrigley"
x_url: "https://x.com/mckaywrigley"
x_user_id: "2786431437"
other_identities: ["https://github.com/mckaywrigley", "https://www.mckaywrigley.com"]
website: "https://www.mckaywrigley.com"
organization: "Takeoff AI (renamed MagicLearn per third-party source)"
role: "Founder"
research_date: "2026-11-24"
confidence: "high"
account_type: "person"
primary_domain: "ai-engineering"
secondary_domains: ["content-creation", "startup-building"]
board_eligibility: ["ai-engineering", "creator", "startup", "master"]
status: "verified"
---

# Mckay Wrigley (@mckaywrigley)

## A. Identity
- **Name:** Mckay Wrigley. X bio: "I build & teach AI stuff." Location field: "The Simulation". Account created 2014-09-26; ~230k followers, ~20k posts (X API, 2026-11-24).
- **Verified links:** GitHub `mckaywrigley` lists twitter_username `mckaywrigley` and company "Takeoff AI" [S21]; personal site says "Founder of Takeoff AI" [S22].
- **Organization/role:** Founder, Takeoff AI [S21][S22]. A third-party profile says Takeoff was renamed **MagicLearn** in Feb 2026 [S23] (secondary, medium confidence; not confirmed on his own site, which still says Takeoff).
- **Origin story (self-reported):** learned to code ~2019, raised $20k from initial customers in July 2020 [S1]; got GPT-3 beta access in July 2020 and went full-time on AI [S2].
- **Research date:** 2026-11-24. **Confidence:** high (identity cross-linked X↔GitHub↔site).

## B. Expertise map
- **Primary:** AI-assisted software building and teaching it (Cursor, Claude Code, Codex, agent SDKs) [S5][S6][S7][S12].
- **Secondary:** AI education business (paid courses) [S23][S24]; AI-product/open-source builder (Chatbot UI) [S3][S21]; AI trend commentary.
- **Technical:** full-stack JS/Next.js templates (mckays-app-template, 1.9k stars) [S21]; chat UIs; multi-agent coding workflows [S13]; MCP [S14].
- **Business:** building audience via fast "first look" demos of new model capabilities [S4], converting it into a course subscription business [S24].
- **Products/projects:** Chatbot UI (33k★), ai-code-translator (4.1k★), paul-graham-gpt (2.6k★), clarity-ai (Perplexity clone) [S21]; Takeoff/MagicLearn courses [S23].
- **Communities:** AI builders/vibe-coders, Cursor/Claude Code users.

## C. Core philosophy
- **AI:** maximalist / "AGI-pilled" optimist; believes capability is compounding fast and most people underestimate it [S10][S20]. Strong pro-Anthropic sentiment in 2026 posts (also political commentary; excluded from distillation).
- **Software dev:** humans move to directing agents; quality comes from giving agents context (comments, rules, specs) [S5][S6]; multi-agent/swarm execution beats single agent [S13].
- **Entrepreneurship:** don't fight the labs on their own turf [S9]; build on top of new primitives early (MCP apps, agent-SDK apps) [S12][S14].
- **Monetization:** education + open-source credibility; early-customer pre-sales (raised $20k from customers before building out) [S1].

## D. Distilled knowledge
1. **Ship demos the day a capability lands** — his biggest posts are concrete capability demos (whiteboard→code, 29k likes) [S4]. [demonstrated result: engagement metrics]
2. **Document code for the AI reader** — "adding comments *everywhere*" to boost codegen [S5]. [observed statement]
3. **Use persistent rules/system prompts as leverage** — tutor-mode rules for beginners [S6]; "You are AGI-pilled." for agents [S15]. [observed statement; efficacy anecdotal]
4. **Parallelize agents** — swarm/task systems claimed 2.5x faster and better [S13]. [observed statement, single anecdote]
5. **Route/blend models** — expects routing across "jagged" models to beat single-model use [S16]; personally switched primary coding model within 3 months [S11]. [observed statement]
6. **Avoid head-on competition with labs** (talent, model access, speed asymmetry) [S9]. [observed statement]
7. **Build on new agent primitives** (Agent SDK apps, MCP apps) before they become crowded [S12][S14]. [observed statement]
8. **Mistake to avoid (implicit):** rubber-stamping agent diffs ("approve" 9,646 times without reading) [S17]. [our interpretation: he jokes about it; we treat it as a risk]
- **Tools recommended (2024-2026):** Cursor, Claude Code (tasks/swarm), Codex app, Claude Agent SDK, Claude Design, MCP [S5][S12][S13][S14][S11].

## E. Implementation playbooks
### E1. "Capability-day demo" content loop (derived from [S4][S7])
- **Problem:** growing an AI-builder audience without long-form production.
- **Preconditions:** access to new model/tool releases; screen recorder.
- **Tools:** model of the week, Cursor/Claude Code, OBS, X.
- **Steps:** 1) on release day pick ONE concrete task a viewer already has (photo→code, ticket→Slack bot); 2) record a <2 min real run; 3) post with one-line claim + video + repo link; 4) follow with a "how to set it up in <15 min" post; 5) collect replies as next-demo ideas.
- **Expected output:** 2-3 demo posts/week, a public repo per demo.
- **Cost:** ~$0-20/mo model spend. **Time:** 1-2 h/demo. **Complexity:** low.
- **Risks:** hype-chasing; demos that don't generalize; platform reach volatility.
- **Success metric:** bookmarks/likes ratio, repo stars, email/course signups per demo.
### E2. AI-friendly codebase hygiene (derived from [S5][S6][S15])
- **Problem:** agents produce wrong or off-pattern code.
- **Preconditions:** a repo you maintain; an agentic IDE.
- **Tools:** Cursor rules / CLAUDE.md / AGENTS.md.
- **Steps:** 1) have the agent add intent comments to core modules; 2) write a rules file (stack, conventions, "explain changes"); 3) add a system-prompt line raising agent ambition; 4) review diffs, never blind-approve [S17].
- **Expected output:** fewer correction cycles. **Cost:** ~0. **Time:** 1-3 h setup. **Complexity:** low.
- **Risks:** stale comments mislead agents. **Success metric:** % of agent PRs merged without manual rewrite.
### E3. Parallel agent "swarm" for feature work (derived from [S13][S11])
- **Problem:** serial single-agent work is slow.
- **Preconditions:** tasks decomposable into independent units; tests.
- **Tools:** Claude Code tasks/subagents or Codex; tmux.
- **Steps:** 1) write a task list with acceptance tests; 2) spawn one agent per independent task; 3) one reviewer agent + human merge gate; 4) measure wall-clock vs single agent.
- **Cost:** higher token spend (he reports 3-4x usage growth [S20]). **Complexity:** medium.
- **Risks:** merge conflicts, token cost, silent quality loss. **Success metric:** wall-clock time per feature at equal defect rate.

## F. Evidence summary
24 sources in `sources.yaml` (89 X posts read; 4 non-X). Top sources: [S21] GitHub, [S1] pinned origin post, [S4] top demo, [S13] swarm claim, [S9] labs warning.

## G. Strengths and weaknesses
- **Strengths:** early and practical on AI coding tools; proven open-source traction (Chatbot UI 33k★) [S21]; teaches beginners effectively; strong demo instinct.
- **Weaknesses / limits:** many claims are anecdotal (single runs, "2.5x faster") [S13]; frequent hype language and timeline predictions (e.g., "6-12 months" [S10], "3-6 months" in 2024 [S8]) that should be scored, not trusted; low posting volume in last 6 months (13 original posts found since 2026-05-24).
- **Conflicts of interest:** sells AI-coding courses (Takeoff/MagicLearn) [S23][S24] — tool enthusiasm drives course demand. Public partisan/political posting in 2026 (not distilled).
- **Differs from others:** more maximalist than pragmatic voices (e.g. Pavan Belagatti's governance-first "software factory" framing).

## H. Practical applications for Kishore
1. **AI income (content → product):** copy E1 for an Indian DevOps/AI audience: "capability-day" demos applied to DevOps tasks (k8s, Terraform), funnel to a low-price course or template.
2. **Agents/automation:** adopt E2 + E3 in Kishore's own repos (DISTILL itself) — rules files + parallel agents with a human merge gate.
3. **Products:** templates/starter kits sell (mckays-app-template 1.9k★ is a lead magnet) [S21] — a "DevOps-ready AI app template" is a low-maintenance asset.
4. **Avoid:** building generic chat UIs or model wrappers that labs will ship [S9].
- **Board eligibility:** ai-engineering (hands-on AI coding practice), creator (demo-driven audience growth), startup (customer pre-sales, edu business), master (frontier-capability outlook; weight as optimistic outlier).

## I. Profile evolution (2026-11-24 baseline)
- **2020:** non-coder → founder raising from customers [S1].
- **2023:** GPT-4V/ChatGPT Vision demos, Chatbot UI open source [S4][S3].
- **2024:** Cursor workflows & o1; agents "toys to tools" [S5][S8]; AI+crypto thesis [S19].
- **2026:** Claude Code/Codex multi-agent, Agent SDK apps, MCP apps, model routing; coding model preference flipped Claude→GPT within 3 months [S11]; increasingly AGI-timeline focused [S10][S20].
- **Change to track:** whether course business (MagicLearn) and AgentShare become primary focus; prediction accuracy.
