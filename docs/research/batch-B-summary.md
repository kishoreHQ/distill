# Batch B summary - DISTILL research (2026-11-24, IST)

Spec: SPEC.md v1. X API: 34 calls total (1 batch user lookup + 33 timeline searches, ≤25 posts/call). Pinned posts: the API returned pinned IDs but none were retrievable ("Not Found"). Long-form reads used public pages, the unauthenticated GitHub API and one web search. No login walls were bypassed, and no GitHub repo was touched.

| Handle | ID (folder) | Display name | account_type | Status | Posts read | Long-form | Primary / secondary domains | Board eligibility | Confidence | Key limitations |
|---|---|---|---|---|---|---|---|---|---|---|
| @steipete | peter-steinberger | Peter Steinberger | person | verified | 99 | 3 + GitHub API | ai-engineering / automation, productivity | master, ai-engineering, automation | high | OpenAI employee (bias in model comparisons); 2024 sample is pre-AI-pivot; no podcasts |
| @thedankoe | dan-koe | Dan Koe | person | verified | 96 | 3 | content-creation / productivity, startup-building | creator, master | high | Mostly aphorisms; sells guides/books and promotes Eden (ownership unverified); subscriber counts self-reported |
| @livingdevops | akhilesh-mishra | Akhilesh Mishra | person | verified | 66 | 2 + GitHub API | automation / content-creation, startup-building | automation, creator | high | Sells bootcamps (COI); Kestra post may be sponsored; old band only 16 posts |
| @GithubProjects | x-githubprojects | GitHub Projects Community | aggregator | verified (account) | 75 | 1 (Ko-fi) | ai-engineering (signal feed) / automation | none, signal feed only | medium | Anonymous operator, unofficial; no expertise; t.co links not resolved |
| @techyoutbe | kushal-gangil | Kushal Gangil (Tech Fusionist) | person | partial | 75 | 1 (Linktree; Gumroad empty) | content-creation / automation | creator | medium | Real name only from display name; ~63% of posts are image/link with little text; sponsored promos; originality unverified |
| @mischavdburg | mischa-van-den-burg | Mischa van den Burg | person | verified | 75 | 2 | content-creation / startup-building, automation | creator, startup | high | YouTube (main channel) not reviewed; salary and placement claims are marketing |
| @itsmesumanc | suman-chakraborty | Suman Chakraborty | person | partial | 64 | 3 (secondary: CNCF sched, Cast AI recap, LinkedIn snippet) | automation / ai-engineering | automation | high (identity); low (X signal) | X is low-signal; main channel LinkedIn is behind a login wall |
| @lennysan | lenny-rachitsky | Lenny Rachitsky | person | verified | 100 | 1 page + long X notes | startup-building / content-creation, productivity | startup, creator, master | high | Many insights come from guests (secondary); podcasts and paywalled posts not read |
| @vatsal_sanghvi | vatsal-sanghvi | Vatsal Sanghvi | person | partial | 71 | 1 (ugcpulse.app) | startup-building / content-creation, automation | startup, creator | medium | Account only since 2025-03; ugcpulse ownership unverified; many personal posts |
| @wojakcodes | x-wojakcodes | Wojak Codes (pseudonymous) | person (unverified) | partial | 75 | 0 (blog empty; GitHub has 0 repos) | ai-engineering / none | none | low | Pseudonymous; no code or products; mostly non-technical, provocative posts |

Totals: 10 handles, all exist and are public. 6 verified, 4 partial, 0 blocked. 796 posts read. 1 aggregator; 1 pseudonymous account.

## Standout practical insights for Kishore
1. **Automate only a motion you've already proven by hand** (Vatsal [S3], echoed by Lenny's "direction > throughput" [S5] and Atlassian's reverted all-builder teams). For DISTILL's opportunity engine: one channel and one manual experiment loop come first, and agents come after.
2. **Build CLI-first and agent-verifiable, with AGENTS.md and a docs/ folder** (Steinberger [S5][S6][S8]). Gate autonomous fixes with a 4-check rule: fits VISION.md, can be inferred from the code, has a clear fix, can be tested live. This applies directly to the DISTILL repo and to any small dev tool Kishore ships.
3. **Sell a point of view, not checklists, then package your working systems as a product.** Dan Koe's argument is that checklist content is cloneable by AI. Lenny ships frameworks as runnable skills, and Mischa uses content, then a quiz, then a stage report, then an offer. A low-time route for Kishore: an "AI agents for DevOps engineers" lens, with DISTILL skills as public lead magnets and a low-ticket guide like Kushal's ~$7.49 bundle to validate. Indian DevOps cohorts at ₹30k-60k (livingdevops) show demand, but live teaching costs a lot of time.

## Blockers / notes
- Pinned posts could not be fetched for any account (the API returns Not Found on pinned_tweet_id).
- Some long posts are truncated at 280 characters (note text was not returned). Affected: the steipete AI-spend post, Vatsal's viral-app anatomy, Kushal's infographic workflow, and Wojak's workflow.
- LinkedIn and YouTube were not opened (login wall or not attempted). Podcast transcripts were not fetched.
- The GitHub folder was renamed to x-githubprojects (canonical id for an account with no identifiable person).
- posts.jsonl records carry an extra `band` field (recent/mid/old) for change detection.
