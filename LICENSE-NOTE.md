# Third-party content

The code in this repository (`scripts/`, `schemas/`, workflow files, skills, prompts) was written for DISTILL.

The material under `profiles/`, `docs/research/`, and the short quotes repeated in `knowledge/`, `boards/`, `opportunities/`, and `intelligence/` is other people's public speech. It stays theirs.

## What is stored

- Profile essays that cite a source id.
- `sources.yaml` rows: a URL, a short excerpt, and a one-line description. Excerpts are the ones already in the research bundles, or, for Arnav Gupta, the short quotes already in his evidence ledger.
- `posts.jsonl`: id, timestamp, URL, text capped at 280 characters, and public metrics when the research file had them. Arnav Gupta's rows are the evidence quote only, and the metrics are null. Null means unknown, not zero.
- Batch summaries and `SPEC.md`, copied so the method notes stay next to the data.

## What is not stored

A full download of an account, a paywalled body, a transcript that was never fetched, or a cookie used to obtain one. Do not add those.

## How to reuse

Link the original URL when you quote someone. Do not present a simulated board paragraph as something that person said in a meeting. Do not present a self-reported revenue number as an audited figure or as a prediction. The profiles say when a number is self-reported. Keep that label.

No separate software license is asserted by this file. The absence of a `LICENSE` for the scripts is intentional until the repository owner chooses one. That absence does not grant rights in the third-party excerpts.
