---
id: "mukul-lohar"
display_name: "Mukul Lohar"
x_username: "ironfisto"
x_url: "https://x.com/ironfisto"
x_user_id: "990528957953986562"
other_identities: ["https://github.com/ironfisto", "https://lohar.me", "https://ironfisto.medium.com/"]
website: "https://lohar.me"
organization: "closed (founder); LiveShortly (building); ex-ServiceNow"
role: "Product security engineer / indie builder"
research_date: 2026-11-27
confidence: "medium"
account_type: "person"
primary_domain: "ai-engineering"
secondary_domains: ["security", "automation"]
board_eligibility: ["ai-engineering"]
status: "verified"
---

# Mukul Lohar (@ironfisto)

## A. Identity
- **Name:** Mukul Lohar (GitHub `ironfisto` name + blog lohar.me) [S7][S11]. X bio: "security | cryptography | db | h/os | llms · Ex Security - @ServiceNow @tokopedia · Building: [two links]"; Ahmedabad; ~1.5k followers.
- **Role conflict:** lohar.me lists ServiceNow "2023 — Present" [S7], while the X bio says "Ex Security - @ServiceNow" — treat ServiceNow as **likely former** (X bio is more recent).
- **Building:** closed (founder, per closed.sh) [S10]; LiveShortly (linked in bio; role not stated on site) [S9].
- **Confidence:** medium — identity is solid; the posting record is small and mostly casual.

## B. Expertise map
- **Primary:** application/product security (CVE author [S1][S8], bug bounty [S7]), now applied to AI-agent tooling.
- **Secondary:** developer tools for coding agents (session streaming [S9], permission alerts [S11]); AI-assisted CAD for mould design [S10].
- **Evidence:** CVE-2025-66021 (high severity) credited to ironfisto [S8].

## C. Core philosophy (inferred from products and long post)
- **2026-11-27.** He says he is playing with Google's Fuchsia OS [S12] (https://x.com/ironfisto/status/2125931480723698037). A reply says a Zircon deploy via WSL takes huge storage and 2 to 4 hours (https://x.com/ironfisto/status/2125952848559313305). A personal experiment. [observed statement]
- **Agent identity:** bearer tokens are the wrong identity primitive for agents; requests should be attributable to an owner [S2]. [observed statement]
- **Human-in-the-loop AI:** AI drafts, humans decide; numbers must have provenance; AI is never a source of truth for dimensions [S10]. [observed statement]
- **Observability of agents:** make agent sessions watchable/replayable [S9]. [our interpretation]

## D. Distilled knowledge
1. Agent-auth threat model: tokens get copied across laptops/CI/clouds, rarely expire, can't distinguish a leaked copy [S2]. [observed statement]
2. Provenance-first AI UX: each value tagged Measured/Rule/Catalogue/Calculated/Customer/You; approval gates per stage; reject separated from approve [S10]. [observed statement]
3. Small agent DX utilities are quick wins (sound on permission prompt) [S11]. [demonstrated result: shipped repo]
4. Vertical AI for a non-software niche (mould design) built by a security engineer [S4][S5][S10]. [our interpretation: domain-expert-led vertical agent]

## E. Implementation playbooks
### E1. Provenance-gated vertical agent (derived from [S10])
- **Problem:** professionals won't trust AI-generated numbers.
- **Preconditions:** a domain with deterministic tools (CAD kernel, solver, rulebook).
- **Tools:** LLM agent for orchestration only; deterministic solvers for values; audit log.
- **Steps:** 1) split workflow into stages; 2) agent proposes, deterministic tools compute; 3) tag every value with its source; 4) stop at rule violations with ranked fixes; 5) explicit sign-off before release.
- **Output:** auditable drafts. **Cost:** dev-heavy. **Time:** months. **Complexity:** high.
- **Risks:** niche adoption, liability. **Metric:** % stages approved without edits.
### E2. Agent identity hardening for DevOps (derived from [S2])
- **Steps:** inventory agent API keys in CI/laptops → short-lived scoped credentials (OIDC/workload identity) → per-agent identities with owner mapping → request signing where supported → alert on unknown agent traffic. **Cost:** low. **Complexity:** medium. **Metric:** % agent calls attributable to an owner.
### E3. Agent-session sharing (derived from [S9][S11])
- **Steps:** stream/record coding-agent sessions for team review and client demos; add notifications for permission prompts. **Cost:** free tier. **Risk:** leaking secrets in streamed terminals.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 2 posts (2 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 70 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-25 refresh.** Appended 3 posts (3 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 68 rows.
11 sources; 65 X posts (2022 and 2026 only; no 2023-2025 sample). Strongest: [S8] advisory, [S10] closed.sh, [S2] agent-identity post, [S7] site.

## G. Strengths and weaknesses
- **Strong:** verified security research; principled human-in-the-loop design.
- **Weak:** small audience; X is mostly casual/personal; products early (waitlist, small usage counters) [S9][S10].
- **Conflicts:** promotes own products [S3].

## H. Practical applications for Kishore
1. **E2** directly upgrades Kishore's DevOps practice: agent credentials as a security service offering.
2. **E1 pattern** for any automation he sells: deterministic tools compute, agent orchestrates, human approves.
3. **E3** for content: livestream/replay agent DevOps sessions as proof-of-work.
- **Board eligibility:** ai-engineering (security-minded agent design). Not creator/startup — products unproven, audience small.

## I. Profile evolution (2026-11-24 baseline)
- **2022:** security-engineer chatter (Burp, bug bounty) and casual posts.
- **2023-2025:** gap in our X sample; CVE published Nov 2025 [S8].
- **2026:** shift to building AI-agent tooling (LiveShortly, ping) and a vertical AI product (closed) [S9][S10][S11].
- **2026-11-25.** Three new rows: a birthday wish, a VFX line, and a bare link. The bearer-token argument [S2] is not updated. No section A–H change.
- **2026-11-27.** The bearer-token identity line [S2] is not revisited. Fuchsia [S12] is a side experiment, not a new principle.
