# Adding a new profile

Use the `add-profile` skill and `prompts/add-profile.md`. The short version is below.

## Id

Verified person: `jane-doe`. Unverified handle: `x-janedoe`. Never reuse an id. Never write into someone else's folder because the topics overlap.

A mistaken account stays in the tree with `research_status: excluded` and a `replaced_by` field, following `profiles/x-aravind`.

## Files

```
profiles/<id>/profile.md
profiles/<id>/sources.yaml
profiles/<id>/posts.jsonl
profiles/<id>/status.json
```

Front matter must validate against `schemas/profile-front-matter.schema.json`. Sections `## A.` through `## I.` are required. Every `[S1]` style citation in the essay must exist in `sources.yaml`.

`posts.jsonl` is one JSON object per line. Split on `\n` only. Do not use Python `splitlines()`, which also splits on U+2028 and will break otherwise valid rows. The importer already normalises U+2028 to a real newline inside the JSON string.

## Fetching

Official X API with `X_BEARER_TOKEN`, public GitHub, public web. Budgets are in `config/sources.yaml`. If the token is missing, you can still add a profile from documents the person published, and you set `research_status` to `partial` with that limitation written down.

Do not pass a login wall. If a site is JavaScript-only and you only retrieved the title, say that, as the Ojasvika profile does for projectminimi.com.

## After the folder exists

1. Add the person to `profiles/registry.yaml` or re-import if they came from a bundle.
2. `python3 scripts/build_matrix.py`
3. `python3 scripts/generate_dashboard.py`
4. `python3 scripts/validate_repo.py`
5. `python3 -m pytest`

Active count is not a target to hit. The Phase 1 tree has 32 active profiles because that is how many real folders survived the exclusion, including the converted Arnav Gupta folder. A 33rd active profile is fine when it is a real new person.

## Arnav Gupta is not the template for a thin import

His extra bundle had an evidence ledger and no post file. The converter kept the quotes and set status to partial. Do not point `posts_read` at a number you do not have a note for. His `posts_read` of 200 is copied from `state/sync.json`, and `posts_read_note` says the posts themselves were not in the archive.
