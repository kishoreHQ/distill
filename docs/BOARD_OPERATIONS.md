# Board operations

The five boards are simulated. The sentence below is required in `board.yaml` and in every deliberation file. `scripts/validate_repo.py` checks for it.

> SIMULATED ADVISORY BOARD. The real people named here have not joined this board, have not been contacted, and have not endorsed DISTILL, Kishore, or any recommendation in this file. Positions below are paraphrases of their public posts and pages, with citations. They are not quotes of private advice.

## Seats

| Board | Members in the 2026-11-24 deliberation |
|---|---|
| `ai-engineering-agents` | aravind-srinivas, peter-steinberger, theo-browne, shubham-saboo, mckay-wrigley |
| `developer-tools-oss` | tw93, peter-steinberger, theo-browne, tom-dorr, david-ondrej |
| `indie-hacking` | pieter-levels, piyush-sachdeva, alex-finn, lenny-rachitsky, vatsal-sanghvi |
| `creator-economy` | dan-koe, david-ondrej, alex-finn, akshay-saini, harkirat-singh |
| `careers-cloud-devops` | akhilesh-mishra, suman-chakraborty, pavan-belagatti, mukul-lohar, arnav-gupta |

A person can sit on more than one board. Aggregators do not sit. `x-aravind` does not sit. `x-wojakcodes` does not sit. The batch notes call that account low-evidence.

Nav Toor is discussed on the creator board as a non-member, because batch A calls the account a sponsored format case study.

The research spec's `master` eligibility is not a sixth board. It is recorded on the profile when the bundle set it. A cross-cutting master board is not implemented.

## Deliberation shape

1. Disclaimer
2. Question
3. Positions, one per member, each with a URL that matches `sources.yaml`
4. Disagreements
5. Synthesis
6. Recommended next action
7. Confidence (`high`, `medium`, or `low`)

Confidence on the 2026-11-24 set is medium because the sample is a snapshot and several numbers are self-reported, even when the quotes themselves are first-party.

## Conflicts of interest

If the profile says the person sells a course, a community, or their employer's product, the deliberation says that next to the advice. Steinberger's OpenAI employment, Saboo's Google Cloud role, Belagatti's Port role, and the various schools are examples already written down. Do not delete those sentences to make the synthesis cleaner.

## Updating

Add `boards/<id>/deliberations/<date>.md`. Point `board.yaml` `deliberation` at it if this file should be the one validators check for URLs. Keep old files. Run `validate-repo`.
