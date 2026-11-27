---
id: peter-steinberger
display_name: Peter Steinberger
x_username: steipete
x_url: https://x.com/steipete
x_user_id: "25401953"
other_identities: [https://github.com/steipete, https://steipete.me, https://github.com/openclaw/openclaw]
website: https://steipete.me
organization: OpenAI; OpenClaw (open-source project, moving to a foundation)
role: Works at OpenAI on agents (per his Feb 2026 post); creator of OpenClaw; previously founder of PSPDFKit
research_date: 2026-11-27
confidence: high
account_type: person
primary_domain: ai-engineering
secondary_domains: [automation, productivity]
board_eligibility: [master, ai-engineering, automation]
status: verified
---

# Peter Steinberger (@steipete)

## A. Identity
- Display name: Peter Steinberger; X @steipete (user id 25401953, since 2009), San Francisco; ~617k followers at research time [S1].
- GitHub @steipete: company OpenAI; "Previously: Founder of @PSPDFKit"; 228 public repos [S2].
- Joined OpenAI (announced 2026-02-15) "to work on bringing agents to everyone"; OpenClaw moves to a foundation and stays open source [S4].
- Creator of OpenClaw ("The AI that really does things"), created 2025-11-24, ~395k GitHub stars at research time [S3].
- Website: steipete.me (blog since 2012, iOS/macOS deep-dives, 2025-26 agentic-engineering posts).
- Confidence: high (X, GitHub and blog cross-link; first-party).

## B. Expertise map
- Primary: agentic software engineering / AI coding workflows (codex, Claude Code), agent harnesses [S5][S7][S10].
- Secondary: developer tooling and automation (CLIs, CI, menu-bar utilities), personal productivity with agents [S2][S11][S17].
- Technical specializations: Apple platforms (Swift/Obj-C, macOS internals; long blog history), TypeScript, Go for CLIs, agent orchestration at scale [S5].
- Business specializations: built and ran PSPDFKit for ~13 years (founder) [S2][S4]. No revenue figures collected.
- Products/projects: OpenClaw [S3]; CodexBar, agent-scripts, summarize, agent-rules, oracle, RepoBar, birdclaw, clawpatch [S2][S9].
- Communities: iOS/macOS dev community (historic), AI-coding/agent builders, OpenClaw open-source community.

## C. Core philosophy
- **2026-11-27.** Three replies. He calls the subject a spiritual fork of OpenClaw that contains a fork of Pi. The parent was not fetched, so the subject is unnamed [S26] (https://x.com/steipete/status/2126054806276161967). He says an option is feature-restricted MCP access and rate limited [S27] (https://x.com/steipete/status/2126034492737589310). He says an agent can use peekaboo to work around alerts [S28] (https://x.com/steipete/status/2125816651639910578). No steps. [observed statement]
- **2026-11-26.** He says Google finally built an MCP and is forbidding CLIs like gog unless you pay them more [S23] (https://x.com/steipete/status/2125654555262431248). He says he built gog so agents call the API, so a human-only reading would still leave him in breach [S24] (https://x.com/steipete/status/2125718925325529177). A year note says OC is in a great place in prosumer and enterprise, and that shipping reliable free open source is hard [S25] (https://x.com/steipete/status/2125422797304549672). OC is not spelled out in that post. [observed statement]
- AI: Treats models as primary authors of code; he says he rarely reads most generated code, focusing on architecture, dependencies and system design [S5]. Rejects "vibe coding" label [S15].
- Automation: Close the loop so agents can verify their own work (CLI-first, live tests); move toward agents that run loops on a codebase while humans "curate the automations" [S5][S13][S8].
- Software dev: Simplicity - commit to main, few worktrees, docs in-repo, short prompts with screenshots; pick boring, well-known dependencies the model knows [S5][S18].
- Ownership: Prefer your own harness over vendor-controlled ones [S10]; platform gatekeepers (Apple, Google Play review) are a recurring risk [S20].
- Entrepreneurship: Explicitly chose not to turn OpenClaw into a company; values building and reach over company-building [S4].
- Monetization: No evidence of him selling courses; his public work is open source. Commercial incentive is employment at OpenAI [S4].

## D. Distilled knowledge
- **Tools, 2026-11-27.** peekaboo, named as an alert workaround [S28]. OpenClaw and Pi, named as the contents of a fork [S26]. Restricted MCP access [S27] continues the platform-terms theme [S23].
- **Tools, 2026-11-26.** gog, his CLI, which he says is more efficient on calls than the MCP [reply in `posts.jsonl`, not a separate source]. Google's MCP, as the thing he says is now the paid path [S23]. The linked terms page was not fetched.
- **2026-11-25.** On OpenClaw he says random "openclaw is now x" posts are tiring and points at the git repo [S22] (https://x.com/steipete/status/2125066430857220265). On memory he describes an early spawn-and-fork in claw/node that he says is usually about 30x smaller [S21] (https://x.com/steipete/status/2125344148496769362). The 30x is his report. [observed statement]
- Principle: "Start with the model and a CLI first" - text interfaces let agents call and verify output [observed statement] [S5].
- Principle: Engineer codebases for agents, not for human navigation (obvious structure, docs/*.md, global AGENTS.md) [observed statement] [S6].
- Mental model: "Most software is boring" - data in, store, display; throughput is bounded by inference time and hard thinking [observed statement] [S5].
- Mental model: Tokens-as-abundant - ask how you'd build if tokens didn't matter (runs ~100 codex instances reviewing) [observed statement] [S7].
- Framework (autotriage gate): an issue/PR is auto-worked only if it (1) fits VISION.md, (2) is inferable from code with high confidence, (3) has a clear fix, (4) can be live-tested [observed statement] [S8].
- Framework (clawpatch): slice codebase into semantic features -> review each -> record explicit fix attempts with validation [observed statement] [S9].
- Tactic: Instead of plan mode, converse, let the model research, then say "build" or "write plan to docs/*.md and build this" [observed statement] [S5].
- Tactic: Cross-reference solved patterns in sibling repos ("look at ../vibetunnel and do the same") to save prompts [observed statement] [S5].
- Tactic: Let the agent choose which tests to run; cut CI and run full tests hourly [observed statement] [S11].
- Tactic: Route work by code ownership automatically (agent finds last author and pings them) [observed statement] [S12].
- Tools recommended: codex CLI/mac app, cmux, Svelte, Go for CLIs, Cloudflare sandboxes, cotypist [S17][S18][S5]. CodexBar (his) for usage/cost tracking [S2].
- Mistakes warned about: trusting paid hype for new agents [S14]; depending on vendor harnesses that change rules [S10]; over-engineered multi-agent task systems when the human is the bottleneck [S5].
- Demonstrated results: OpenClaw adoption (~395k stars) and multiple 2k-23k-star tool repos [demonstrated result] [S2][S3]. Note: stars show attention, not revenue.

## E. Implementation playbooks

### E1. CLI-first agent-verifiable tool (derived from [S5])
- Problem: Building tools/apps quickly with agents without manual QA.
- Preconditions: Coding agent (codex/Claude Code/etc.), a repo, a clear input->output.
- Tools: Coding agent CLI, Go or TypeScript, git.
- Steps: 1) Define the core as a CLI with text/JSON output. 2) Have the agent write it and run it on real inputs to verify. 3) Add docs/*.md + AGENTS.md describing structure. 4) Only after core works, add UI/extension. 5) Commit to main, iterate on feel.
- Expected output: Working CLI in hours, UI later.
- Cost: Model subscription/API (varies). Time: hours to 1-2 days. Complexity: low-medium.
- Risks: Unread code may hide security issues; mitigate with review pass (E2).
- Success metric: Agent can run and self-verify end-to-end without you.

### E2. Autotriage + review gate for repos (derived from [S8][S9])
- Problem: Issue/PR backlog consumes maintainer time.
- Preconditions: Repo with VISION.md, test suite or live-test path.
- Tools: Coding agent with skills, GitHub issues, a review tool (e.g. clawpatch-style slicing).
- Steps: 1) Write VISION.md. 2) Encode 4-gate rule (fits vision / inferable / clear fix / live-testable). 3) Agent labels and auto-works only passing items. 4) Run a second review pass over each change. 5) Human approves merge.
- Expected output: Small fixes resolved autonomously; human reviews only.
- Cost: tokens; Time: 1 day setup. Complexity: medium.
- Risks: Wrong fixes merged; keep human merge approval.
- Success metric: % of issues closed without human coding; regression rate.

### E3. Lean CI with agent-selected tests (derived from [S11])
- Problem: Slow/expensive CI.
- Steps: 1) Agent maps changed files to affected tests. 2) Run only those on PR. 3) Full suite on an hourly/nightly schedule. 4) Track escapes.
- Risks: Missed regressions; complexity medium. Success metric: CI minutes and wait time down, escaped-bug count flat.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 3 posts (3 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 113 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-26 refresh.** Appended 8 posts (8 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 110 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z.
- **2026-11-25 refresh.** Appended 3 posts (3 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 102 rows.
- 99 X posts read (49 recent 6 mo, 25 mid 2026-05, 25 from Oct-Nov 2024); 3 long-form fetched (steipete.me home, 2 posts) + GitHub API. 20 sources in sources.yaml.
- Top sources: [S5] workflow post, [S4] OpenAI/OpenClaw post, [S2] GitHub, [S8] autotriage, [S7] tokens-don't-matter.

## G. Strengths and weaknesses
- Strengths: Hands-on, high-volume builder; shares concrete configs and tools; demonstrated open-source traction [S2][S3][S5].
- Consistently right about: closing the verification loop, simplicity, owning tooling.
- Limited evidence: monetization/pricing for small products; his setup assumes high token budgets (~100 cloud agents) that Kishore can't replicate cheaply [S7].
- Conflicts of interest: OpenAI employee - his model comparisons (codex vs Opus) and model-capability claims [S16] favor his employer; also he sponsors/promotes friends' tools (e.g. Blacksmith CI).
- Risks of blindly following: "don't read the code" is dangerous for production/security-sensitive work; Mac-centric tooling.
- Many posts are reactive one-liners/politics/link shares - low signal for the knowledge base.

## H. Practical applications for Kishore
1. AI agents & automation: Adopt CLI-first + AGENTS.md + docs/ structure for every DISTILL script so any agent can run and verify them (direct fit for the DISTILL repo itself) [S5][S6].
2. DevOps: Apply the 4-gate autotriage and agent-selected-test CI to his own repos to cut maintenance time [S8][S11].
3. Software products: Small "developer usage/cost" utilities (CodexBar-like) show demand for agent-cost visibility tools - possible micro-product, but validate (stars ≠ revenue) [S2].
4. Productivity: Queue ideas into the agent instead of issue trackers; run 2-3 projects in parallel only when you can context-switch.
- Board eligibility: ai-engineering (core agentic-engineering practitioner), automation (agent loops, CI automation), master (strong perspective on build-vs-company, ownership of tooling). Not creator/startup: no monetization or audience-growth playbooks in evidence.

## I. Profile evolution
- 2026-11-24 baseline.
- Late 2024 (sample): Apple-platform commentary, gaming, politics; light AI interest ("Cursor really pushes the industry forward") [S19].
- 2025: "came back from retirement"; heavy Claude Code usage, then shift to codex after GPT-5 ("un-slops older crimes of Opus") [S5].
- Late 2025-Feb 2026: OpenClaw launches and explodes; joins OpenAI [S3][S4].
- 2026: scale experiments (~100 cloud agents), autotriage/review automation, agent-run projects with humans curating [S7][S8][S13]; growing emphasis on owning your harness [S10].
- **2026-11-25.** No change to the CLI-first or vibe-coding lines. The new notes are an implementation workaround and a request to trust the repo over rename rumors.
- **2026-11-26.** Before, the CLI-first essay [S5] and the Apple-agreement stop on OSS releases [S20] were the platform risks. After, a second platform move is in his words: Google's MCP terms against CLIs like gog [S23][S24]. The CLI-first line is not withdrawn.
- **2026-11-27.** No withdrawal of the CLI-first line [S5] or of the gog terms complaint [S23]. The new notes are a fork description whose subject is missing [S26], rate-limited MCP [S27], and peekaboo [S28].
