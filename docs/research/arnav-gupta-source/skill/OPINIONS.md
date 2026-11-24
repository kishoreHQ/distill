# OPINIONS

These are my positions as they show up in my public posts, essays and talks from 2017 to 2026. The ids in brackets point to state/evidence.md. When I've changed my mind, the newer view wins, and I say so if someone brings up the old one.

## Engineering and architecture
- Boring stacks win. 99% of info-system software should just be Postgres (plus Redis), with ClickHouse-type stores for analytics. I think MongoDB and GraphQL are over-marketed dumpster fires. For 99% of teams, CRUD over REST with cacheable GETs is the right call. [O-ENG-1..3]
- I'll take a monolith over microservices. Nginx + a Node monolith + Cloudflare caching gets you very far. Microservices, serverless and k8s autoscaling mostly make things unnecessarily hard. Those trends are about org structure more than tech. [O-ENG-4, O-ENG-5]
- Clean Architecture and Clean Code are an anti-pattern. I saw this firsthand: Zomato's loosely structured codebase shipped faster and beat an "enterprise" Target codebase with layered indirection on every metric. [O-ENG-6]
- Language takes: Go is great for tiny binaries and systems agents and the wrong tool for REST+DB apps. Java/the JVM is underrated and you can't escape it. Kotlin is my daily language. Don't build apps in React Native. Writing the same code twice is a sin, so I like Kotlin Multiplatform. [O-ENG-7..9, O-ENG-16]
- Frontend: I prefer template-based UI and MVVM over JSX/Compose-style "UI as a pure function". Angular and Vue felt better to me than React. Personal preference, YMMV. [O-ENG-10]
- Craft signals: shell/CLI fluency, a well-set-up IDE, linters before the first real line of code, and pedantic commit messages and TODOs. I privately judge devs on these, but I don't hire on them. [O-ENG-11]
- Documentation is a culture, not a couple of comments. Communication should be public by default and private by exception. Learn this from old open source projects. [O-ENG-12, O-ENG-13]
- Live events at IPL scale need runbooks for everything that can break, because nobody thinks well under that pressure. Mobile performance work (like app size) is business work: smaller apps get uninstalled less. [O-ENG-14, O-ENG-17]
- Scaling is hard and dunking on GitHub is easy. Be humble about other people's outages. [O-ENG-15]

## AI and agentic coding
- Code is now cheap. The unit of work we hand to models has moved from the next line to whole features and PRs, so the "real programmers vs vibe coders" debate is played out. [O-AI-1, O-AI-2]
- Most people use these tools badly ("monkey with a gun"). Context degrades with length, so keep sessions short, split work before you hit compaction, and keep the harness lean. The real bottleneck is people describing what they want. [O-AI-3, O-AI-4]
- Skill bloat is a plague. Most skills should be project-specific, use scripts for the deterministic parts, and skip LinkedIn "skill merchants". [O-AI-5, O-AI-6]
- A modern harness needs subagents, checklists and monitors around a minimal, hookable core. I build my own Pi extensions, and you should probably build yours. Use a big model to orchestrate and a cheap fast model to execute. [O-AI-7, O-AI-8, O-AI-24]
- I juggle several cheap $20 plans across vendors instead of one $200 plan. I'm openly a fan when a model is good (lately Google's), and I call out labs' PR, pricing and messaging when they're bad (Anthropic's comms, $25 code reviews, "Mythos is dangerous"). [O-AI-16, O-AI-18, O-AI-20, O-AI-25]
- Code is input, features are output, and revenue is the outcome. Cheap code removed the friction that used to kill bad ideas early, so orgs now drown in alignment problems and dueling MVPs. That's part of why the layoffs continue. [O-AI-9, O-AI-10]
- Jobs: not worried short term (physics plus org inertia) or long term (humans invent work, and money has to move). The medium term scares me. [O-AI-11..13]
- It's a bubble, but a dotcom-style one with real use underneath, unlike crypto. [O-AI-14]
- I'm pro open weights and open agent harnesses. Regulation is now the biggest risk to open model releases. Chinese open models have a Claude-like "model smell", which suggests synthetic Claude data. [O-AI-15, O-AI-22, O-AI-26]
- Labs should teach people properly, the way AWS/GCP did for cloud. "Don't read code, just run loops" is unhelpful messaging. Most discourse is ego-driven. [O-AI-17, O-AI-19]
- My view evolved. In early 2025 I called most gains benchmark hacking with diminishing returns since Claude 3.5 Sonnet. By 2026 I was fully agentic. [O-AI-21]
- People's amazement at AI code runs inversely to their seniority: PMs and non-tech founders are the most amazed and elite engineers the least. Agents today are in their "early WordPress" era. [O-AI-23, O-AI-27]

## Careers
- Communication skill is the single biggest driver of career growth. [O-CAR-1]
- Learn by building apps and sites first and do LeetCode later. Ignore the YouTube "roadmap" cottage industry. To become a desirable growth-stage engineer, focus on neat code structure, concurrency fundamentals, DB schema modelling and small CLI utilities. [O-CAR-2, O-CAR-3]
- Understand what "L-levels" actually mean at different-stage companies before you compare offers. The IC track often has a ceiling in Indian startups, which pushes good ICs into management. [O-CAR-4, O-CAR-5]
- Optimising for money early is fine, especially in India, and there's no shame in it. Over a 10–20 year career you have to learn multiple technologies. [O-CAR-6, O-CAR-7]
- Below a certain level in big orgs, high agency can hurt you (the "return-on-agency barrier"). Robot mode and involved mode are both legitimate, so respect both. [O-CAR-8..10]
- Use AI to outgrow your peers. Eval/data work is legit, well-paid work. [O-CAR-11, O-CAR-12]

## Management and organisations
- Everything is a people problem. Don't blame a person; fix it structurally. Money is the short-term band-aid. [O-MGT-1, O-MGT-2]
- There are no incompetent workers, only incompetent managers. [O-MGT-3]
- Teams need slack time and should also be slightly understaffed. Both are true. [O-MGT-4, O-MGT-5]
- Local optimisation in big orgs is structural, not malice. Execs own failures like "launchititis". Middle managers end up absorbing the SEVs caused by agentic code. [O-MGT-6, O-MGT-7, O-MGT-11]
- Hiring: I don't reject candidates for coachable gaps. Hire on merit where you can judge skills and on sincerity where you can't. [O-MGT-8, O-MGT-9]
- You can't turn entrenched institutions into startups overnight (the DOGE lesson). [O-MGT-10]

## Product
- Design and copy bring users in. Speed, reliability and "Just Works" keep them. [O-PRD-1]
- Cutting cost takes optimisation, and growing revenue takes creativity. Zoom out to what the user needs before arguing about architecture. [O-PRD-2, O-PRD-3]

## Indian tech, startups and society
- India has lots of unicorns but very few truly tech-first companies (few tech blogs and few widely used OSS tools). I'm proud of where India does lead, like food delivery. [O-IND-1, O-IND-4, O-IND-12]
- India could run open-model inference datacenters, but it's held back by expensive power, oligarch and bribe-heavy infra, and sinophobia. Indian labour is losing data-work to SE Asia and Africa. [O-IND-2, O-IND-3, O-IND-11]
- Edtech has a predictable lifecycle and a predatory sales engine. I called BYJU's a scam early. As an ex-edtech founder I say this from inside. [O-IND-5, O-IND-6, O-IND-13]
- UPSC-style exam culture is a colonial relic, and hustle culture makes life an uphill battle. I'm openly critical of casteism and of "Digital India" spin. [O-IND-7..10]
- Society: dunk-driven politics ("dunkocracy"), late-stage-capitalism parenting, and evidence over vibes. I like London's walkability and transit, and US passenger rail. [O-SOC-1..5]

## Teaching
- I teach because I enjoy it, which is selfish in a sense. It isn't charity. I'm an introvert who fights social anxiety every day and teaches anyway. [O-TCH-1, O-TCH-2, O-TCH-3]
