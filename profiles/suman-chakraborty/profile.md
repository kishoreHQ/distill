---
id: suman-chakraborty
display_name: Suman Chakraborty
x_username: itsmesumanc
x_url: https://x.com/itsmesumanc
x_user_id: "16391036"
other_identities: [https://www.linkedin.com/in/schakraborty007, http://topmate.io/suman_chakraborty007/]
website:
organization: Platform9 Systems
role: Solutions Architect (per X bio and KubeCon India 2026 speaker bio)
research_date: 2026-11-24
confidence: high
account_type: person
primary_domain: automation
secondary_domains: [ai-engineering]
board_eligibility: [automation]
status: partial
---

# Suman Chakraborty (@itsmesumanc)

## A. Identity
- X @itsmesumanc (id 16391036, since 2008), ~1.2k followers; Solutions Architect at Platform9, ex-VMware, ex-SAP [S1].
- Confirmed by CNCF KubeCon India 2026 schedule speaker bio [S2] and a third-party KubeCon India 2025 recap [S3]. LinkedIn (seen only via search snippet): Kolkata, ~16 yrs experience, ~42k followers [S4].
- Confidence: high on identity; content depth partial.

## B. Expertise map
- Primary: Kubernetes platform engineering / cloud-native operations (API server performance, multi-cluster add-ons, checkpointing, VMware migration) [S2][S3][S7][S8].
- Secondary: AI infrastructure governance (MCP certification, AI cost governance with agentgateway) [S4][S5].
- Credentials: CKA, CKS (renewed twice), MCPA [S5][S6].
- Communities: CNCF India (KubeCon India, KCD Delhi, Cloud Native Kolkata), conference speaker.

## C. Core philosophy
- Little opinion content on X; mostly event announcements, certifications, news shares, and some personal/national commentary. Operational philosophy inferred from talk abstracts: move beyond defaults, measure (audit logs, latency metrics) before tuning [S2]. Other areas: No evidence found.

## D. Distilled knowledge
- Technical method: Diagnose K8s API server bottlenecks with audit logs + apiserver_request_duration_seconds; use Priority & Fairness instead of max-requests-inflight; fix LIST storms via WatchList streaming and client caching [observed statement, talk abstract] [S2].
- Technical method: Container checkpointing (CRIU) for forensics and recovery [observed statement, via third-party recap] [S3].
- Emerging topic: AI cost visibility/governance across hosted LLM APIs + self-hosted models via a Kubernetes-native gateway (agentgateway) [observed statement, via snippet] [S4].
- Content signal: his highest-engagement X post shares a curated collection of real production Kubernetes issues [observed statement] [S9].
- Career signal: MCP now has a Linux Foundation certification (MCPA) [observed statement] [S5].

## E. Implementation playbooks
### E1. AI spend governance gateway (derived from [S4], our interpretation)
- Problem: Untracked LLM API spend across teams/agents (relevant to DISTILL's own model costs).
- Preconditions: Multiple LLM consumers; Kubernetes or a proxy host.
- Tools: An LLM gateway (agentgateway or similar), Prometheus/Grafana.
- Steps: 1) Route all model calls through one gateway. 2) Tag by team/agent. 3) Export token/cost metrics. 4) Set budgets/alerts.
- Cost: low (OSS). Time: 1-2 days. Complexity: medium.
- Risks: Gateway as single point of failure. Metric: % spend attributed; budget breaches caught.
### E2. API-server health clinic (derived from [S2])
- Steps: enable audit logs -> dashboard apiserver latency by verb/user agent -> identify noisy controllers -> configure APF FlowSchemas -> fix heavy LIST clients. Complexity: high; for large clusters only.

## F. Evidence summary
- 64 X posts (25 Mar-Nov 2026, 25 Jan-Feb 2026, 14 May 2025); 3 long-form/secondary (CNCF sched, Cast AI recap, LinkedIn snippet). 9 sources. LinkedIn (his main channel) not opened due to login wall.

## G. Strengths and weaknesses
- Strengths: credentialed, conference-vetted Kubernetes practitioner; India cloud-native community presence.
- Weaknesses for DISTILL: X is low-signal (low engagement, many event/news/personal posts); main content lives on LinkedIn.
- Conflicts: promotes employer's tools (vJailbreak/Platform9) [S8].
- No monetization/startup evidence.

## H. Practical applications for Kishore
- DevOps: Reference for advanced K8s operations and AI-infra governance; MCPA certificate is a cheap credential signal for an "AI agents + DevOps" positioning [S5].
- Community: KCD/KubeCon India speaking as a distribution channel for an Indian DevOps engineer.
- Board eligibility: automation (infra/platform ops). Not creator/startup/master (insufficient evidence).

## I. Profile evolution
- 2026-11-24 baseline. 2025: VMware-migration and K8s production content, KubeCon India 2025 checkpointing talk [S3][S8]. 2026: multi-cluster add-ons, API server performance, MCP certification and AI-cost governance - moving toward AI platform infrastructure [S2][S4][S5][S7].
