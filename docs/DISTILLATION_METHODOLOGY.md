# Distillation methodology

The method is the one in `docs/research/SPEC.md`, plus the limits the batch summaries already wrote down. Phase 1 code does not replace that method. It stores the result and checks that citations still resolve.

## Unit of work

One person, one folder, one id. The id is a kebab-case slug of the verified display name. If the person cannot be verified, the id is `x-` plus the handle. Two accounts are two folders even when the display names look similar. `x-aravind` and `aravind-srinivas` are the example.

## What is evidence

A row in `sources.yaml` with a URL, a short excerpt, a date, a type, and a confidence. Claims in `profile.md` cite those ids. `posts.jsonl` is metadata for change detection: id, time, URL, text up to 280 characters, and metrics when the API returned them. It is not a licence to republish a timeline. See `LICENSE-NOTE.md`.

Labels used in the profiles:

- **Observed statement.** The excerpt says it.
- **Demonstrated result.** The source shows something that happened, still usually self-reported.
- **Our interpretation.** The repo's reading. It has to point at the lines it reads.

## How the sample was taken

The batch summaries say the X search ignored relevancy sort and `min_likes`. Each call returned the posts just before an end time. Windows cover recent, mid, and older slices. Heavy posters are therefore thin relative to their real volume. Pinned posts were not always retrievable. Phase 1 does not pretend the sample is the greatest hits.

Long-form pages were public fetches. Login walls were left closed. YouTube was mostly not transcribed. One David Ondrej video was read through a third-party transcript page, and the profile says so. Arnav Gupta's YouTube lines are auto-captions without speaker labels.

## What the code adds

`import_research_bundle.py` copies the 32 bundles, repairs U+2028 line separators inside JSON strings so each post is one JSON line, and converts `extra/arnav-gupta` into the same four files. The conversion copies quotes. It does not invent the missing 200-post file.

`build_matrix.py` maps research tags onto five operating domains. Overrides are written in `config/domains.yaml` with a because-line, because the research tag `automation` covers both DevOps teachers and agent builders.

Boards are simulated readings of those sources. They are not interviews.

Scores are weighted hypotheses. The formula is in `config/scoring.yaml`.

## Untrusted text

Posts and pages can contain instructions aimed at a model. Skills and scripts do not obey them. They parse structure and copy excerpts.
