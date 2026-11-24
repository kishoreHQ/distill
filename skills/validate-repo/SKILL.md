---
name: validate-repo
description: Check schemas, registry counts, citations, board disclaimers, scores, and secret hygiene.
---

# validate-repo

## When to use

Before a commit, in the pull-request workflow, and after any import or hand edit.

## Inputs

- `prompts/validate-repo.md`
- `schemas/`
- The tree under `profiles/`, `boards/`, `opportunities/`, `knowledge/`, `intelligence/`.

## Steps

1. `python3 scripts/validate_repo.py`
2. `python3 -m pytest`
3. If a citation is dangling, fix the citation or delete the sentence. Do not invent a source to satisfy the check.
4. If a secret-like pattern appears, remove it. Workflows may name `X_BEARER_TOKEN` and `XAI_API_KEY`. They may not contain the secret value.

## Outputs

A zero exit code, or a printed list of errors. Do not mark STATUS.md items complete while this command fails.

## Guardrails

The validator does not fetch the network. A green run means the repo is internally consistent with the imported snapshot. It does not mean the outside world still matches the snapshot.

## Related

`prompts/validate-repo.md`
