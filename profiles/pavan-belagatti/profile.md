---
id: "pavan-belagatti"
display_name: "Pavan Belagatti"
x_username: "Pavan_Belagatti"
x_url: "https://x.com/Pavan_Belagatti"
x_user_id: "2199002832"
other_identities: ["https://github.com/pavanbelagatti", "https://www.youtube.com/@pavanbelagatti", "https://linkedin.com/in/pavan-belagatti"]
website: "https://www.youtube.com/@pavanbelagatti"
organization: "Port (port.io)"
role: "Agentic Engineering Advocate / Developer Advocate"
research_date: 2026-11-27
confidence: "high"
account_type: "person"
primary_domain: "ai-engineering"
secondary_domains: ["automation", "content-creation"]
board_eligibility: ["ai-engineering", "automation"]
status: "verified"
---

# Pavan Belagatti (@Pavan_Belagatti)

## A. Identity
- **Name:** Pavan Belagatti ("Pavan Belagatti™🥑"). X bio: "AI Evangelist | Developer Advocate | Tech Content Creator"; links YouTube @pavanbelagatti. ~3.7k followers, ~11.8k posts (X API).
- **Organization/role:** Developer/"Agentic Engineering" Advocate at **Port** (port.io) — GitHub company field + bio [S15]; LinkedIn announcement Mar 2026 [S16] (snippet, medium). Prior DevRel roles (SingleStore, Harness, JFrog) per LinkedIn summary [S16]; SingleStore affiliation also visible in 2024 posts [S13].
- **Location:** Bengaluru (LinkedIn summary [S16]). **Confidence:** high.

## B. Expertise map
- **Primary:** agentic engineering for the SDLC — harness engineering, AI software factories, spec-driven development [S1][S2][S5].
- **Secondary:** RAG/vector DBs/LangChain/LangGraph tutorials (2024-25) [S12][S14]; DevOps/platform engineering; developer content (X Articles, DEV, DZone, YouTube) [S18].
- **Projects:** 225 public tutorial repos [S15]; "AI Software Factory" reference build [S2].
- **Communities:** Bengaluru AI meetups ("Build with AI"), DevRel/DevOps audiences.

## C. Core philosophy
- **2026-11-27.** He writes a learning curve: prompts, then context engineering, then specifications, skills, tools, memory, guardrails, and evaluations [S22] (https://x.com/Pavan_Belagatti/status/2125992897514488079). A reply the same day says he focuses on the specs first (https://x.com/Pavan_Belagatti/status/2125815961974628564). [observed statement]
- **2026-11-26.** He says arguing which model is better misses harness engineering [S20] (https://x.com/Pavan_Belagatti/status/2125628394385850699). He asks if we are becoming Markdown engineers and lists AGENTS.md, SKILL.md, spec.md, and plan.md [S21] (https://x.com/Pavan_Belagatti/status/2125617581155590527). A third post says review is the bottleneck after AI sped up writing, and points at a software factory. That third post is in `posts.jsonl` and continues [S2]. [observed statement]
- **2026-11-25.** Wording shift, same direction. Earlier excerpt opens with "DevOps is dead" and moves to agentic DevOps [S6]. On this date he posted "DevOps isn't dead; it's evolving into Agentic DevOps!" [S19] (https://x.com/Pavan_Belagatti/status/2125240504648597894). The profile already treated the dead line as a hook. This post says the non-dead version in the first sentence. [observed statement]
- **Software dev in the AI era:** generation is cheap; the bottleneck moved to context, verification, governance and delivery [S8][S17].
- **Agents:** need a harness — context layer (ownership, dependencies, rules), tools, guardrails, feedback, human gates [S1][S4]; don't do "one giant prompt", use graphs of steps [S3].
- **Humans stay in charge of risk:** "An agent should not decide what business risk is acceptable." [S18]; skeptical of fully autonomous SDLC [S7].
- **Careers:** devs should move to building agents/workflows, FDE-type roles [S9].

## D. Distilled knowledge
- **Tools, 2026-11-27.** The curve names specifications, skills, memory, guardrails, and evaluations as the layer after context [S22]. A second post says a single prompt is not enough for Cursor or Claude Code. That post is in `posts.jsonl` and is cut off.
1. **AI Software Factory** = stations (understand → change → check → review → ship) with clear handoffs and checks; one station is now an agent [S2][S18]. [observed statement + small personal build]
2. **Start small and measurable:** one recurring delivery problem, baseline metric; set up ownership/context/permissions before execution; verify independently of the producer; define recovery [S17]. [observed statement]
3. **Harness engineering layers:** context, tools, guardrails, feedback; example deploy gate driven by scorecards [S1]. [observed statement]
4. **Spec-Driven Development:** structured spec as source of truth for coding agents [S5]. [observed statement]
5. **Graph engineering:** explicit nodes/edges for agent workflows [S3]. [observed statement]
6. **Agents vs workflows** distinction (n8n demo) [S10]; **context engineering** over prompt engineering [S11]; **late chunking** for RAG [S12]. [observed statements]
- **Tools recommended:** GitHub Actions, Codex/Claude Code, Port (employer), LangGraph, n8n, SingleStore (former employer) [S2][S10][S13].
- **Mistakes he warns about:** single giant prompts [S3]; agents without context [S4]; treating code generation as the whole job [S8].

## E. Implementation playbooks
### E1. Minimal "issue → agent PR → human review" factory (derived from [S2][S17])
- **Problem:** babysitting coding agents step by step.
- **Preconditions:** GitHub repo with tests/CI; agent CLI with API key; a label convention.
- **Tools:** GitHub Issues + Actions, Codex CLI or Claude Code in a container runner, optional catalog (Port/Backstage or a YAML file).
- **Steps:** 1) label an issue `agent`; 2) Action spins an isolated container, passes issue + repo context + rules; 3) agent writes change + tests; 4) CI runs; 5) Action opens PR with summary; 6) human reviews/merges; 7) log time-to-PR and rework.
- **Expected output:** draft PRs for small issues. **Cost:** API tokens + Actions minutes (~$10-50/mo small repo). **Time:** 0.5-1 day. **Complexity:** medium.
- **Risks:** secrets exposure in runner; low-quality PRs; prompt injection via issue text. **Success metric:** % agent PRs merged with <15 min human edit; lead time.
### E2. Scorecard deployment gate (derived from [S1])
- **Problem:** agents/humans shipping to unhealthy or non-compliant services.
- **Steps:** define per-service scorecard (owner set, tests pass, no open P1 incident, SLO ok) → gate deploy job on scorecard → agent must cite gate result in PR.
- **Cost:** low. **Complexity:** medium. **Metric:** change-failure rate.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 4 posts (4 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 104 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-26 refresh.** Appended 3 posts (3 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 100 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z.
- **2026-11-25 refresh.** Appended 1 post (1 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 97 rows.
18 sources; 96 X posts (2024-05 → 2026-11). Top: [S2] factory build, [S1] harness guide, [S17] Port blog, [S18] DZone, [S15] GitHub.

## G. Strengths and weaknesses
- **Strong:** clear, practical explanations bridging DevOps and agents; consistent hands-on tutorials with repos [S15].
- **Limited evidence:** few production-scale results of his own; mostly tutorials and reference builds.
- **Conflicts of interest:** content is DevRel for his employer — 2026 posts promote Port/"context lake" framing [S2][S16]; 2024 posts favored SingleStore ("I might be biased") [S13]. Tool recommendations track employer.
- **Engagement:** low engagement per post (single-digit likes typical in 2026), so reach is not evidence of validation.
- **Provocative framings** ("DevOps is dead") [S6] are marketing hooks; his substantive position is "agentic DevOps augments DevOps" [S6][S7].

## H. Practical applications for Kishore
1. **Directly relevant skill bridge (DevOps → agentic engineering):** build E1 on Kishore's own repos (including DISTILL), then publish the build as content/portfolio — the FDE/agentic-platform niche he describes [S9].
2. **Service offering:** "agentic SDLC setup" for small teams (issue→PR factory + scorecard gates) as a consulting package; validate with 3 teams.
3. **Content:** explain-then-build tutorial format with a repo per post.
- **Board eligibility:** ai-engineering (harness/factory/RAG), automation (SDLC automation with human gates). Not creator (low engagement) or startup (no venture evidence).

## I. Profile evolution (2026-11-24 baseline)
- **2024:** RAG, vector DBs, LLM frameworks; SingleStore-centric [S13][S14].
- **2025:** agents vs workflows, MCP, context engineering, LangGraph, GraphRAG [S10][S11].
- **2026 (Port):** harness engineering, AI software factories, spec-driven dev, graph engineering, agentic DevOps, FDE careers [S1][S2][S3][S5][S6][S9].
- **2026-11-25.** Before: "Unpopular, but I think DevOps is dead" [S6]. After: "DevOps isn't dead; it's evolving into Agentic DevOps!" [S19]. The agentic-automation advice in the same post matches [S6][S7]. Low like count on the new post (the metrics are on the row). Reach is not validation.
- **2026-11-26.** No reversal of the 2026-11-24 sentence that DevOps is not dead and is evolving into agentic DevOps [S19]. The new posts repeat harness-over-model [S20] and markdown files as the agent interface [S21].
- **2026-11-27.** No reversal of harness-over-model [S20] or of agentic DevOps [S19]. The new sentence orders the work: prompt, context, then specs and guardrails [S22].
