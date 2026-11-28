---
id: tw93
display_name: Tw93
x_username: HiTw93
x_url: https://x.com/HiTw93
x_user_id: "1521688129559613440"
other_identities: [https://github.com/tw93, https://tw93.fun, https://weekly.tw93.fun]
website: https://tw93.fun
organization: Independent developer (Mole, Pake, Kami, MiaoYan, Waza, Kaku)
role: Indie open-source developer / product maker (legal name not stated in sources read)
research_date: 2026-11-28
confidence: high
account_type: person
primary_domain: ai-engineering
secondary_domains: [startup-building, productivity]
board_eligibility: [ai-engineering, startup, automation]
status: verified
---

# Tw93 (@HiTw93)

## A. Identity
- Pseudonymous Chinese-speaking indie developer "Tw93"; X id 1521688129559613440, ~166K followers [S1]. Same identity on GitHub tw93 (X badge links both ways in READMEs) and blog tw93.fun [S2][S5][S14].
- Real name not given in sources read — profile uses the public handle. Posts mostly in Chinese, product launches in English.
- Confidence high (identity cross-linked across X/GitHub/blog).

## B. Expertise map
- **Primary:** AI-assisted engineering practice and agent skills (Waza; 21 AI coding practices; Claude Code architecture articles) [S3][S5][S8].
- **Secondary:** indie desktop product building and monetization: OSS CLI → paid native app (Mole, Pake) [S4][S6][S7].
- **Technical:** Rust/Tauri-style lightweight desktop apps (Pake vs Electron) [S12], macOS system tooling (Mole), multi-device agent test rigs [S9].
- **Projects:** Mole (~76K★), Pake (~64K★), Kami (~12.6K★), MiaoYan, Waza, Kaku [S2].
- **Communities:** Chinese dev community on X/blog; global OSS users (multi-language READMEs) [S5][S6].

## C. Core philosophy
- **2026-11-28.** He says an 8折 discount is a psychological burden because of people who paid the normal price, that he does not like marketing Mole, and that Black Friday was mainly because domestic users asked [S25] (https://x.com/HiTw93/status/2126202160740524186). The 8折 is his. It is not a new dollar price. The $15.20 line [S20] is not repeated. Most of the other 69 rows are food, music, a monitor question, and short replies. [observed statement]
- **2026-11-27.** The $15.20 figure returns as a Black Friday price for Mac and Windows, one purchase, with a 14-day refund he states [S20] (https://x.com/HiTw93/status/2125916971908866280). Mole buyers get a Pake code he says stacks to 0.72 of list [S21] (https://x.com/HiTw93/status/2125940244637942085). He says Mole is not a CleanMyMac substitute [S22] (https://x.com/HiTw93/status/2125957204780224700). He says the Mac open-source build stays free, and the App Store version at 88 covers Mac, iPhone, and iPad [S23] (https://x.com/HiTw93/status/2125768705309331769). A December duo plan for any 3 devices is a plan he prices around $29 [S24] (https://x.com/HiTw93/status/2125919328403161223). Prices are his. [observed statement]
- **2026-11-26.** Mole's paid app is on a stated sale: 20% off, $15.20 until December 1, once a year [S17] (https://x.com/HiTw93/status/2125598323327508840). That price is his. A Chinese update says installed CLIs can be uninstalled and that all his products add no telemetry and no extra interface access beyond activation binding [S18] (https://x.com/HiTw93/status/2125450228455383474). A reply says basic features ship on CLI and GUI together, and the GUI has many features the CLI does not [S19] (https://x.com/HiTw93/status/2125736229828518143). [observed statement]
- **2026-11-25.** He says Mole's AI cleanup now removes idle AI tools, dead hooks, finished worktrees, orphan conversations, and leftovers from uninstalled tools [S15] (https://x.com/HiTw93/status/2125172384202371402). In a reply he says he wants an editor with no AI, for reading code, readmes, and diffs [S16] (https://x.com/HiTw93/status/2125150540837650573). The second line is a reading tool, not a rejection of Mole. [observed statement]
- **Product:** "Anything added dilutes everything else" — refuse features that make software noisier [S2][S4].
- **AI coding:** describe goals/background, let the agent pick technical details; use best models; enforce rules with scripts, not prompts [S3].
- **Monetization:** keep the OSS CLI free; charge for the convenient desktop app [S4][S7].
- **Support/automation:** automate support only when the question repeats, the answer is stable and exceptions are known [S4].
- **Trust:** protect account reputation; avoid grey-market AI accounts [S11].

## D. Distilled knowledge
- **Tools, 2026-11-28.** No new Mole feature. The new line is discomfort with discounting and with marketing [S25]. The Mac build staying free [S23] is not withdrawn.
- **Tools, 2026-11-27.** Mole on Windows as well as Mac, at the same $15.20 he already posted [S20]. Pake stays a separate early-bird purchase [S21].
- **2026-11-26.** The no-telemetry line [S18] is a product constraint he states, next to activation binding. It does not replace the executable-check essay [S3]. A separate reply wonders whether a later period might judge by effect instead of reading code. That reply is hedged and is in `posts.jsonl`. It is not a reversal of [S3].
- **Tools, 2026-11-25.** Mole cleanup of AI-tool residue [S15]. A non-AI editor for code, readme, and diff is a wish in a reply [S16], not a shipped name in that post.
- **Principles**
  - Rules agents must follow should be enforced by check scripts that actually run [observed statement][S3].
  - Separate the coding agent from the reviewing agent; max 3 review rounds; second round only checks new changes [observed statement][S3].
  - If a fix fails 3 times, clear context and restate the problem with attempted fixes [observed statement][S3].
  - Every production bug/user issue gets a regression test the agent runs before release (and when switching models) [observed statement][S3].
  - One-way-door changes (delete, payment, release) require human eyes [observed statement][S3].
  - Parallel agents → separate worktrees; each commits only its own changes [observed statement][S3].
- **Business insights**
  - OSS CLI with large adoption → paid desktop app for non-terminal users (requests came from users' families) [demonstrated result][S4].
  - Growth by word of mouth, no paid marketing; refund rate <0.8% (self-reported) [demonstrated result, self-reported][S4].
  - Don't build ticketing/KB systems before the inbox actually breaks [observed statement][S4].
  - Pricing matters: a user said his price "read like a currency conversion" — localise pricing [observed statement][S4].
- **Safety design:** for cleaners, "not deleting" matters more than deleting; protect AI session folders (~/.claude/projects, ~/.codex/sessions) and model caches [observed statement][S4].
- **Tools:** Claude Code CLI (Opus, high effort) always on; old devices as test machines [S9][S10].
- **Mistakes warned about:** generic AI-looking UI (blue-purple gradients) [S13]; pasting secrets to agents ("treat as leaked, rotate") [S3].

## E. Implementation playbooks

### Playbook 1 — Agent-safe engineering loop (derived from [S3][S5])
- **Problem:** AI coding produces regressions and drifts from rules.
- **Preconditions:** repo, coding agent, CI.
- **Tools:** Claude Code/Codex, git worktrees, a verify script, Waza-style skills.
- **Steps:** 1) Agent explains planned changes and impact first. 2) Work in smallest shippable slices, commit often. 3) Agent writes/maintains a verify script; must pass before "done". 4) Separate reviewer agent, ≤3 rounds. 5) Commit message: what, how verified, how to roll back. 6) Each user bug → regression test.
- **Expected output:** fewer regressions; reusable project harness.
- **Cost:** agent subscription. **Time:** 1 day to set up. **Complexity:** medium.
- **Risks:** over-trusting agent review; script coverage gaps.
- **Success metric:** regressions per release; % releases needing rollback.

### Playbook 2 — Open-core desktop monetization (derived from [S4][S6][S7])
- **Problem:** popular free CLI with no income.
- **Preconditions:** OSS tool with real usage and recurring requests from non-technical users.
- **Tools:** native/Tauri app, license/payment provider (Lemon Squeezy/Paddle), email.
- **Steps:** 1) Wait until CLI semantics are stable. 2) Build GUI for non-terminal users; dogfood daily. 3) One-time price, early-bird. 4) Keep CLI free and updated. 5) Answer support manually until patterns stabilise; then automate.
- **Expected output:** paid tier without alienating OSS users.
- **Cost:** low; code signing fees. **Time:** weeks–months. **Complexity:** medium–high.
- **Risks:** needs an existing large user base; cross-platform signing/notarization effort.
- **Success metric:** conversion of CLI users, refund rate, support load.

### Playbook 3 — Repurpose old devices as agent test rigs (derived from [S9])
- Problem: testing across OSs/devices. Steps: wipe old laptops/phones, install target OSs, connect via SSH/remote, let agents run builds/tests there. Cost: ~$0. Complexity: low–medium. Metric: platforms covered per release.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 58 posts (58 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 214 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-28 refresh.** Appended 70 posts (70 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 284 rows. Window 2026-11-26T22:17:25Z to 2026-11-28T00:17:25.371Z, collected 2026-11-28T00:17:25.371Z.
- **2026-11-26 refresh.** Appended 36 posts (36 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 156 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z. Most new rows are short thank-you replies.
- **2026-11-25 refresh.** Appended 35 posts (35 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 120 rows.
- 14 sources (3 blog, 3 GitHub, 7 X posts, 1 profile). 85 X posts read (50 last 6 months, 20 6–24 months, 15 older).
- Top: [S3] 21 practices, [S4] Mole monetization story, [S5] Waza, [S2] repos.

## G. Strengths and weaknesses
- **Strong:** demonstrated OSS traction (multiple 60K+★ repos) and a documented path to paid revenue [S2][S4]; disciplined, safety-first engineering.
- **Limited evidence:** revenue numbers not disclosed (only refund rate) [S4]; much content is Chinese-language — some nuance may be lost in translation (our reading).
- **Limits:** desktop/macOS focus; playbooks assume an existing audience.
- **Conflicts:** promotes own paid apps (Pake desktop, Mole) [S7]; financial/investing posts are personal opinion (2025) — out of scope.
- Many X posts are lifestyle (concerts, gadgets) — low signal.

## H. Practical applications for Kishore
1. **Agents/automation:** copy the 21-practice loop (Playbook 1) into AGENTS.md for every repo; install Waza-like skills.
2. **Products/income:** open-core path — publish a genuinely useful Linux/DevOps CLI, grow stars, then sell a GUI/"pro" convenience layer (Playbook 2). Low capital, but slow.
3. **Productivity:** fewer tools; let one always-on agent CLI replace many apps [S10].
- **Board eligibility:** ai-engineering (agent practice depth), startup (OSS→paid demonstrated), automation (support automation threshold, agent rigs). Not creator (Chinese-language audience growth not analysed).

## I. Profile evolution
- **2026-11-24 baseline.**
- 2024: "#工程师学习" curated learning links, MiaoYan updates [posts 2024-05].
- 2025: investing talk for engineers, curating agent principles (12-Factor Agents) [posts 2025-07].
- 2026: shifted to shipping paid desktop apps (Mole Mac Aug, Windows Oct; Pake desktop Nov), agent-skills (Waza, Kami), AI-coding best-practice writing [S3][S4][S7].
- **2026-11-25.** Product focus stays Mole and small Mac/iOS apps (MiaoYan is also announced in this window as a plain-Markdown notebook; that post is in `posts.jsonl` and is not given a separate philosophy). The no-AI editor line is new relative to the baseline essay.
- **2026-11-26.** Before, the open-core split was CLI free and native app paid [S7], and Mole cleaned AI-tool residue [S15]. After, he posts a $15.20 sale [S17], a no-telemetry rule except activation [S18], and a GUI that carries features the CLI does not [S19]. Same product shape.
- **2026-11-27.** Before, Mole was a $15.20 sale and a no-telemetry line [S17][S18]. After, the same dollar figure is a Black Friday price that now names Windows [S20], the Mac CLI stays free [S23], and he refuses the CleanMyMac comparison [S22]. No reversal of the free-CLI / paid-app split [S7]. Voice in the replies is hands-on support: discount codes, refunds, and a promise to look at a 20 MB cleanup.
- **2026-11-28.** Before, the public price was $15.20 with the Mac open-source build free [S20][S23]. After, he says he does not like marketing Mole and that an 8折 is a burden relative to full-price buyers [S25]. The dollar price is not revised in this window.
