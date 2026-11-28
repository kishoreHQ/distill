---
id: mischa-van-den-burg
display_name: Mischa van den Burg
x_username: mischavdburg
x_url: https://x.com/mischavdburg
x_user_id: "1639653263778750465"
other_identities: [https://kubecraft.dev, https://roadmap.kubecraft.dev/]
website: https://kubecraft.dev
organization: KubeCraft (founder)
role: Founder, KubeCraft; DevOps/Kubernetes YouTuber (self-described 120K subs)
research_date: 2026-11-28
confidence: high
account_type: person
primary_domain: content-creation
secondary_domains: [startup-building, automation]
board_eligibility: [creator, startup]
status: verified
---

# Mischa van den Burg (@mischavdburg)

## A. Identity
- X @mischavdburg (id 1639653263778750465, since 2023-03), ~27.5k followers; bio claims 120K YouTube subs; founder of KubeCraft [S1].
- KubeCraft roadmap site names him founder [S3]. Based in the Netherlands (his post) [S4]. Former nurse; moved to tech at 32 (self-reported) [S7].
- Confidence: high.

## B. Expertise map
- Primary: DevOps career education business - YouTube -> lead magnet -> high-touch career program [S1][S2][S3].
- Secondary: Kubernetes/homelab/self-hosting practice (Talos, Rancher, Hetzner) [S8][S12]; solo info-business building [S5].
- Products: KubeCraft program (claims 1,000+ members); free roadmap quiz; earlier vim course [S2][S3][S5].
- Communities: career-switchers into DevOps, homelab community.

## C. Core philosophy
- **2026-11-28.** He says there are people who build things and people who rent access to things other people built, and that most people are on the renting side without having chosen it [S18] (https://x.com/mischavdburg/status/2126345312629362974). [observed statement]
- **2026-11-27.** He says terminal skill is rare and that people who have it file it under hobby [S17] (https://x.com/mischavdburg/status/2125983073896411286). A reply says Flux extends the Kubernetes API and that reconciliation loops are the way in (https://x.com/mischavdburg/status/2125957957552677313). That reply is cut off. Another reply says plenty of huge environments are still hands-on terminal work (https://x.com/mischavdburg/status/2126011485222519023). [observed statement]
- **2026-11-26.** He says again that GPG plus password-store is the way [S15] (https://x.com/mischavdburg/status/2125671342305607926). On agent isolation he says each project gets its own dev container and credentials, he mounts only the directories he wants, and the container runs rootless in its own network namespace [S16] (https://x.com/mischavdburg/status/2125485325027782841). He also writes that skill and pay are separate systems. That sentence is in `posts.jsonl`. [observed statement]
- Learning: Build (homelab, public projects) > tutorials/certs ("procrastination with documentation") [S6][S10].
- Career/AI: DevOps is AI-resilient because infra context is large and operational [S9]; uses paid AI subscriptions heavily [S11].
- Entrepreneurship: A deep technical skill (Kubernetes) + content -> own business beats employment income [S4].
- Infra: Self-host on cheap dedicated servers rather than cloud for his own business [S8].

## D. Distilled knowledge
- **Tools, 2026-11-28.** No new tool name. The build-versus-rent line [S18] is a stance, not a stack.
- **Tools, 2026-11-26.** GPG and password-store [S15]. Rootless per-project dev containers for agent credentials [S16]. A reply says he never runs the thing locally and always containerizes it. The reply does not name the binary in the stored text.
- **2026-11-25.** He says not to install the thing on the main machine, and to work in containers [S13] (https://x.com/mischavdburg/status/2125307048283808162). He describes a three-machine upgrade as a drain, reboot, and return, done with a button [S14] (https://x.com/mischavdburg/status/2125258178354962768), and contrasts that with being the load balancer yourself under Docker Compose. [observed statement]
- Funnel [observed statement]: YouTube authority -> free personalised quiz (6 questions, 6 stages) -> strategy-call application -> premium program [S2][S3].
- Positioning [observed statement]: sell outcome (job + salary) not knowledge; target IT pros "without starting over" [S2].
- Principle: Homelab on resume differentiates candidates [observed statement] [S10][S6].
- Business evolution [demonstrated result, self-reported]: low-ticket vim course -> career program as channel grew 10k->80k subs [S5].
- Infra method: multi-cluster self-hosting on Hetzner (9 servers, 6 clusters) for business workloads [observed statement] [S8].
- Content insight: hot-takes on industry news (Docker, NVIDIA) and career/salary posts get the most engagement in sample [demonstrated result - engagement].
- Caution: salary figures ($158K) are marketing claims; "results vary" disclaimer on his own site [S2][S3].

## E. Implementation playbooks
### E1. Quiz lead-magnet funnel for a technical audience (derived from [S2][S3])
- Problem: Converting content viewers into qualified buyers.
- Preconditions: Some audience (YouTube/X/LinkedIn) and a defined skill-progression model.
- Tools: Typeform/Tally (free), email tool, Calendly, landing page.
- Steps: 1) Define 4-6 progression stages for your niche (e.g., "DevOps engineer -> AI-agent platform engineer"). 2) Write 6 diagnostic questions. 3) Output a personalised stage report by email. 4) Offer a call or low-ticket product per stage. 5) Track stage distribution to shape content.
- Cost: ~₹0-2k/month. Time: 2-3 days setup. Complexity: low.
- Risks: Small audience -> few leads; avoid overstated outcome claims.
- Success metric: quiz completion rate, lead->call or lead->sale conversion.

### E2. Self-hosted business infra on Hetzner + Kubernetes (derived from [S8][S12])
- Problem: Cloud bills for side projects.
- Steps: rent dedicated server -> Talos/Rancher/k3s -> GitOps deploy -> backups offsite -> monitoring.
- Cost: low (dedicated servers are cheaper per GB RAM than cloud VMs; verify current prices). Time: 1-3 days. Complexity: medium-high.
- Risks: You own ops/on-call; backups essential. Metric: monthly infra cost, uptime.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 8 posts (8 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 105 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-28 refresh.** Appended 2 posts (2 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 107 rows. Window 2026-11-26T22:17:25Z to 2026-11-28T00:17:25.371Z, collected 2026-11-28T00:17:25.371Z.
- **2026-11-26 refresh.** Appended 14 posts (14 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 97 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z.
- **2026-11-25 refresh.** Appended 8 posts (8 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 83 rows.
- 75 X posts (25 Nov 2026, 25 Feb 2026, 25 Nov 2024); 2 long-form (kubecraft.dev, roadmap page). 12 sources. YouTube not reviewed.

## G. Strengths and weaknesses
- Strengths: clear, working education funnel; practitioner on self-hosted Kubernetes; transparent career story [S2][S5][S8].
- Limited evidence: no verified revenue or placement data; testimonials are curated.
- Conflicts of interest: career-fear/salary posts funnel into his paid program [S2]; "DevOps is AI-safe" also serves his business [S9].
- Risks: high-ticket coaching requires calls/coaching time - not low-maintenance.

## H. Practical applications for Kishore
1. Content/startup: Copy the funnel structure (content -> quiz -> stage report -> offer) for an "AI agents for DevOps engineers" niche [S2][S3].
2. DevOps/cost: Self-host DISTILL dashboards/agents on a cheap dedicated box or the existing box instead of paid cloud [S8].
3. Career narrative: build-in-public homelab/agent projects as proof-of-work [S6].
- Board eligibility: creator (YouTube + funnel), startup (productized education business). Not ai-engineering.

## I. Profile evolution
- 2026-11-24 baseline. Nov 2024: generic cloud/DevOps motivation, homelab-on-resume [S10]. Feb 2026: career/salary/anti-tutorial messaging, AI-proof framing, Claude Code mention. Nov 2026: business infra expansion (Hetzner), Talos->Rancher, AI subscription pricing commentary, NVIDIA/Docker news takes [S8][S11][S12].
- **2026-11-25.** The new cluster narrative is more specific than the baseline sample. It is still his telling of his own boxes.
- **2026-11-26.** The container-scope note [S16] is the new operational line. It agrees with keeping an agent off a shared credential. It is his homelab practice, not a product.
- **2026-11-27.** The terminal-as-rare-skill line [S17] is new wording. The Flux reply does not replace the rootless-container note [S16].
- **2026-11-28.** The container and credential notes are unchanged. The new sentence is build versus rent [S18].
