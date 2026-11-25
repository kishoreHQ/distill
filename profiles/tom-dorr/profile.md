---
id: "tom-dorr"
display_name: "Tom D\u00f6rr"
x_username: "tom_doerr"
x_url: "https://x.com/tom_doerr"
x_user_id: "1326180756310331399"
other_identities: ["https://github.com/tom-doerr", "https://tom-doerr.github.io/repo_posts/"]
website: "https://tom-doerr.github.io/repo_posts/"
organization: ""
role: ""
research_date: 2026-11-25
confidence: "high"
account_type: "person"
primary_domain: "ai-engineering"
secondary_domains: ["automation", "content-creation"]
board_eligibility: ["ai-engineering", "automation"]
status: "verified"
---

# Tom Dörr (@tom_doerr)

> **Account character:** a real, identifiable developer whose X timeline is now ~96% an **automated, curated GitHub-repo feed** (one-line summary + link). Treat it primarily as a **signal feed** for new open-source AI/agent/self-hosting tools, plus a thin layer of his own engineering observations. Do not infer a broad "philosophy" from repo summaries he did not write as opinions.

## A. Identity
- **Name:** Tom Dörr. X bio: posts about "GitHub repos, DSPy, and agents | Subscribe for top posts | DM to share your AI project". ~222k followers, ~58k posts; joined 2020-11 (X API).
- **Verified links:** GitHub `tom-doerr` lists twitter_username `tom_doerr` [S15]; X profile URL points to `tom-doerr.github.io/repo_posts` [S17].
- **Organization/role:** No evidence found (GitHub company field empty). Location not stated.
- **Confidence:** high for identity; medium for "who he is professionally" (not researched beyond GitHub).

## B. Expertise map
- **Primary:** open-source AI tooling discovery/curation; early LLM-in-the-terminal tooling (zsh_codex, 1.7k★, 2021) [S15].
- **Secondary:** DSPy (awesome-dspy, simpledspy, dspy-tweet-optimizer) [S15][S18]; automation of his own publishing pipeline [S16]; self-hosting/homelab (Proxmox) [S10].
- **Products/projects:** zsh_codex, codex-readme, codex.fish, chatgpt_commit_message_hook, repo_posts site, agent [S15].
- **Communities:** AI developer X, DSPy users, self-hosters.

## C. Core philosophy (only where supported)
- **AI/dev workflow:** speed of iteration > maximum reasoning ("lower-effort reasoning is often the best reasoning ... you can iterate so much faster") [S6]; interested in agents orchestrating other agents [S7][S8].
- **Automation:** practices what he curates — his feed and site are machine-run (scheduled workflows, embeddings for related posts) [S16]; X posts in Aug 2025 sample landed every ~30 minutes [S9]. [observed; automation of posting is our interpretation from timestamps]
- **Monetization:** X subscriptions ("Subscribe for top posts") and priority DMs for subscribers (bio). Earlier asked publicly how to monetize a service with hundreds of daily requests [S12].

## D. Distilled knowledge
1. **Curation-as-a-product** — a fully automated "repo summary → post → static site + RSS" pipeline can build a 200k+ audience [S16][S17]. [demonstrated result: follower count + repo stars; causal link is our interpretation]
2. **High-bookmark signal = utility tools for agents** — the most-bookmarked recent posts are agent skills/MCP add-ons (ffmpeg skill 3k bookmarks [S2], meeting recorder [S1]). [observed metrics]
3. **Prefer fast, cheap reasoning loops** for coding [S6]. [observed statement]
4. **Agent-to-agent orchestration works** (Claude driving Codex; Claude Code instances messaging) [S7][S8]. [observed statement]
5. **Cost-arbitrage thinking on GPUs** (Replicate 10x Lambda per minute in 2023) [S11]. [observed statement; prices dated]
6. **Recurring themes in curated repos (Q3-Q4 2026):** agent memory without vector DBs [S13][S14], harness engineering [S3], self-hosted alternatives, security/OSINT tools. [our interpretation of the sample]
- **Warning:** several curated repos are dual-use (bot-check bypass [S4], WiFi deauth [S5]). Do not adopt them without checking legality/ToS.

## E. Implementation playbooks
### E1. Automated niche "repo radar" feed (derived from [S16][S17][S9])
- **Problem:** build distribution with near-zero daily time.
- **Preconditions:** a niche (e.g. DevOps+AI tools for Indian engineers); GitHub API access; LLM API.
- **Tools:** GitHub search/trending API, small LLM for 1-sentence summaries, screenshot tool, Jekyll/GitHub Pages, RSS, X API (scheduled posts).
- **Steps:** 1) daily query trending/new repos by topic; 2) dedupe + quality filter (stars velocity, README quality, license); 3) LLM writes a one-line, verb-first summary ("Converts…", "Runs…"); 4) publish to static site + RSS; 5) schedule 3-8 posts/day; 6) weekly "top bookmarked" digest for paid subscribers.
- **Expected output:** daily feed + searchable archive. **Cost:** ~$5-30/mo. **Time:** 1-2 days to build, ~15 min/week to monitor. **Complexity:** medium.
- **Risks:** X automation rules and API cost; promoting malicious/dual-use repos; commoditized niche.
- **Success metric:** follower growth/week, bookmarks per post, subscriber conversions.
### E2. Use the feed as a tool-scouting input for DISTILL (derived from [S1][S2][S13][S14])
- **Problem:** finding useful new agent tooling early.
- **Steps:** ingest his posts' repo links → tag (memory, MCP, browser, self-host) → weekly shortlist of 3 to trial → record outcome in `knowledge/tools/`.
- **Cost:** ~0. **Risk:** survivorship/hype bias; dual-use tools. **Metric:** trials that become part of Kishore's stack.

## F. Evidence summary
- **2026-11-25 refresh.** Appended 1 posts (1 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 121 rows.
18 sources (120 X posts read; only 5 of them lack a link, i.e. are original commentary). Top: [S16] repo_posts README, [S15] GitHub, [S2] highest-bookmark sample, [S6] own opinion, [S9] cadence sample.

## G. Strengths and weaknesses
- **Strong:** breadth of open-source discovery; early on LLM CLI tooling [S15]; reliable automation.
- **Limited evidence:** almost no long-form opinions; no verified role, company, or business results.
- **Risks of following blindly:** curation ≠ endorsement or testing; some repos are dual-use or immature [S4][S5].
- **Incentives:** paid X subscriptions and DM prioritization for subscribers (bio); repo authors pitch him to get featured.

## H. Practical applications for Kishore
1. **Automation/AI income:** replicate E1 for a narrower niche Kishore owns (DevOps/platform + AI agents, India-focused) — this is the most low-maintenance content model observed in this batch.
2. **Tool intelligence:** wire @tom_doerr into DISTILL's daily scan as a "tools signal" source (E2), not as an advisor.
- **Board eligibility:** ai-engineering (tool scouting, DSPy, agent orchestration observations), automation (demonstrated automated publishing pipeline). Not master/startup/creator-advisor: insufficient first-party reasoning.

## I. Profile evolution (2026-11-24 baseline)
- **2021-2023:** built LLM-in-terminal tools (zsh_codex, codex-readme) and posted personal experiments (GPT-4 configuring Proxmox [S10], GPU cost comparisons [S11]).
- **2025:** repo_posts created Feb 2025 [S16]; Aug 2025 feed posting every ~30 min [S9].
- **2026:** feed slowed to every few hours with longer summaries; focus shifted to agent skills, MCP servers, harness engineering, self-hosting [S2][S3][S13].
- **2026-11-25.** One reply distinguishing utility from explanation in someone else's argument. It does not change the repo-feed or reasoning notes. No section A–H change.
