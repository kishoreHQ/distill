---
id: akhilesh-mishra
display_name: Akhilesh Mishra
x_username: livingdevops
x_url: https://x.com/livingdevops
x_user_id: "1623980420235948034"
other_identities: [https://livingdevops.com, https://github.com/akhileshmishrabiz, https://medium.com/@akhilesh-mishra, https://akhileshmishra.substack.com/, https://www.linkedin.com/in/akhilesh-mishra-0ab886124/]
website: https://livingdevops.com
organization: Living Devops (founder, self-described)
role: Founder/instructor, Living Devops; self-described AI Platform Engineer / DevOps lead (14+ yrs, self-reported)
research_date: 2026-11-27
confidence: high
account_type: person
primary_domain: automation
secondary_domains: [content-creation, startup-building]
board_eligibility: [automation, creator]
status: verified
---

# Akhilesh Mishra (@livingdevops)

## A. Identity
- X @livingdevops (id 1623980420235948034, since 2023), Noida, India; ~25.2k followers; bio "Founder, LivingDevOps | AI Platform Engineer | Tech Storyteller" [S1].
- livingdevops.com names him "Founder and CTO, Living Devops; Devops Lead with 14+ years in Cloud & Devops" (self-reported) and sells his bootcamps [S2]. Links to GitHub akhileshmishrabiz, Medium, Substack, LinkedIn [S2][S3].
- Posts say he is in his 3rd year as an AWS Community Builder (self-reported, May 2026) and took a 10-month break in 2026 after leaving a job [S12].
- Confidence: high (site, GitHub, X cross-link).

## B. Expertise map
- Primary: DevOps/platform engineering education - AWS, Kubernetes, Terraform, Linux, observability, DevSecOps; orchestration of infra automation [S2][S4].
- Secondary: technical content creation on X/LinkedIn/Medium; info-business (paid bootcamps) [S2][S11].
- Technical: EKS, Kubernetes networking/DNS, eBPF tooling, Terraform wrappers, Ansible, Kestra workflows, MLOps/AIOps (course topic) [S3][S4][S8].
- Business: cohort-based paid bootcamps priced ₹30k-₹60k for Indian + global learners [S2].
- Products: Living Devops bootcamps, Discord community, GitHub learning repos (Devops-zero-to-hero ~404 stars), toffee-terraform-wrapper [S2][S3].

## C. Core philosophy
- **2026-11-27.** He says the claim that there are no DevOps jobs is wrong, and that evidence suggests otherwise [S19] (https://x.com/livingdevops/status/2125955940793135450). The link was not fetched, so the evidence is not in this file. He says retraining is usually the wrong answer to a 2026 knowledge cutoff [S20] (https://x.com/livingdevops/status/2125817710928097683). The stored text stops before the method. He asks interviewers in India to turn cameras on and arrive on time [S21] (https://x.com/livingdevops/status/2125916727062225144). An interview answer starts with a Transit Gateway in a central account [S22] (https://x.com/livingdevops/status/2125873763292156063) and is cut off. Not a complete design. [observed statement]
- **2026-11-26.** He says a DevOps engineer who is only a bridge between Jira and Claude should be very scared, because AI is learning to operate tools [S17] (https://x.com/livingdevops/status/2125475523384254782). He also says to learn trade-off decisions for interviews in the AI age [S18] (https://x.com/livingdevops/status/2125433041120059653). [observed statement]
- Software/DevOps: DevOps = designing reliable systems, not knowing tools [S5]; teach troubleshooting over tool tours [S9].
- Automation: Most infra is already automated; the gap is orchestration (sequence, retries, approvals, audit) [S4].
- Cost/ops trade-off: Managed services are paid convenience against 2 AM toil [S6].
- AI: Skeptical of AI hype (NVIDIA "buy our chips" posts) while teaching MLOps/AIOps; notes AI inflating GitHub signals [S13].
- Monetization: Content -> community (Discord) -> paid live cohorts [S2].

## D. Distilled knowledge
- **Tools, 2026-11-27.** Transit Gateway, named as the start of a shared-egress interview answer [S22]. The rest of the design is not in the stored text.
- **2026-11-25.** Teaching focus stays Kubernetes troubleshooting. He says not to put Kubernetes on a resume without being able to explain production failures [S14] (https://x.com/livingdevops/status/2125231968195629225). He points at snowOps, a game per incident [S15] (https://x.com/livingdevops/status/2125270308353610233). On build versus buy for EKS observability he says "open source is free, so we build" fails the interview [S16] (https://x.com/livingdevops/status/2125357198700384277). [observed statement]
- Principle: Monitor the Four Golden Signals rather than many dashboards [observed statement] [S7].
- Principle: "Convenience is expensive" - pay for managed only when toil cost exceeds premium [observed statement] [S6].
- Framework: Orchestration control plane (workflow-as-code) over existing Terraform/Ansible/GitHub/ServiceNow, with approvals, retries per step, run history [observed statement] [S4].
- Technical method: ServiceNow request -> GitHub repo -> Terraform -> human approval -> Ansible -> Slack -> close ticket, in Kestra YAML [observed statement] [S4].
- Trend claim: sidecar -> eBPF (Cilium, Falco) in Kubernetes [observed statement, unverified trend] [S8].
- Content insight: compact fundamentals lists (Linux, DNS, K8s request path) get his highest engagement [demonstrated result - engagement only] [S11].
- Business insight: Indian live-cohort DevOps bootcamps at ₹30k-60k exist and run repeatedly (dates through Jan 2027) [demonstrated result - offering exists; enrollment/revenue not verified] [S2].
- Mistakes warned: copy-paste Terraform without understanding; hello-world Docker tutorials; tool memorization (see posts.jsonl 2025-05) [S9].

## E. Implementation playbooks

### E1. Self-service infra request orchestration (derived from [S4])
- Problem: "Set up a new microservice" requires many manual hand-offs across already-automated tools.
- Preconditions: Existing Terraform modules, Ansible roles, GitHub org, ticketing/Slack.
- Tools: Kestra (open source, self-hosted) or similar workflow engine; Terraform; Ansible; GitHub API; Slack.
- Steps: 1) List the end-to-end sequence. 2) Encode as workflow-as-code YAML in Git. 3) Add per-step retries and a manual approval gate before prod. 4) Trigger from ticket/webhook. 5) Notify + close ticket; keep run history.
- Expected output: One request -> fully provisioned service with audit trail.
- Cost: self-host compute (small VM). Time: 2-5 days. Complexity: medium.
- Risks: New platform to maintain; secrets handling.
- Success metric: lead time per request, manual touches per request.

### E2. DevOps education content -> cohort business (derived from [S2][S11])
- Problem: Monetizing DevOps expertise in India.
- Steps: 1) Post fundamentals explainers daily (Linux/K8s/DNS). 2) Build free GitHub learning repo. 3) Open Discord. 4) Launch weekend live cohort with real production projects; price in INR+USD.
- Cost: low; Time: high ongoing (live teaching 6 h/week per cohort). Complexity: medium.
- Risks: Time-intensive (conflicts with Kishore's low-time goal); crowded market.
- Success metric: enrollments per cohort, completion, referrals.

## F. Evidence summary
- **2026-11-27 refresh.** Appended 9 posts (9 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 92 rows. Window since 2026-11-25T22:16:21Z, collected 2026-11-27T00:19:13Z.
- **2026-11-26 refresh.** Appended 8 posts (8 daily, 0 deepen). 0 collected ids were already stored. `posts.jsonl` now has 83 rows. Window 2026-11-24T22:19:55Z → 2026-11-26T00:20Z. Several rows are short replies.
- **2026-11-25 refresh.** Appended 9 posts (9 in the daily window from 2026-11-23T22:21:18Z, 0 deepen). 1 collected ids were already stored. `posts.jsonl` now has 75 rows.
- 66 X posts (25 recent Nov 2026, 25 May 2026, 16 May 2025); 2 long-form (homepage, 1 blog) + GitHub API. 13 sources.
- Top: [S4], [S2], [S3], [S6], [S7].

## G. Strengths and weaknesses
- Strengths: Practical production DevOps framing; India-specific education business evidence; clear explanations [S2][S4][S11].
- Limited evidence: AI/agent engineering depth beyond course titles; trend claims (eBPF) without data.
- Conflicts of interest: Sells bootcamps - posts about skill gaps/job market funnel to paid courses [S2]; tool-focused blog posts (Kestra) may be sponsored - not confirmed.
- Risks: Live-cohort model is time-heavy; X engagement concentrated on fundamentals, not monetization proof.

## H. Practical applications for Kishore
1. DevOps/automation: Apply orchestration-layer thinking to DISTILL's daily pipeline (one workflow owning sequence, retries, approvals, run log) [S4].
2. Content: Fundamentals explainers are the highest-engagement DevOps format on X for Indian audiences - Kishore can pair them with an AI-agents angle [S11].
3. Income: Evidence that Indian learners pay ₹30k-60k for production-oriented DevOps cohorts; a lower-time variant would be async/recorded or AI-assisted labs [S2].
- Board eligibility: automation (infra orchestration practitioner), creator (DevOps content + education funnel in India). Not ai-engineering (insufficient evidence), not master.

## I. Profile evolution
- 2026-11-24 baseline.
- May 2025: DevOps career/bootcamp critique, launches Discord, EKS MCP server commentary [S9][S10].
- 2026: rebrands as "AI Platform Engineer", adds MLOps/AIOps courses, orchestration content, higher engagement on Linux fundamentals; career break [S1][S2][S4][S12].
- **2026-11-25.** Consistent with "DevOps is not a tool list" [S5]. snowOps is a new drill he is promoting. Bootcamp conflict of interest is unchanged.
- **2026-11-26.** Before, DevOps was not a tool list [S5] and bootcamps taught tools rather than troubleshooting [S9]. After, the tool in the warning is the coding agent itself: do not let the job be operating Claude from a ticket [S17]. The bootcamp he sells [S2] is still a conflict.
- **2026-11-27.** Before, the job line was not to be only a bridge from Jira to Claude [S17]. After, he asserts DevOps jobs exist [S19] without the linked evidence in this repo, and he teaches a cutoff question whose answer is truncated [S20]. No new bootcamp price.
