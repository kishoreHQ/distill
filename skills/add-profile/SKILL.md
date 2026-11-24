---
name: add-profile
description: Add one new person to the registry without touching anyone else's folder.
---

# add-profile

## When to use

Kishore names a new public account to follow. Not for fixing a mis-identified handle. A wrong handle stays in place and is marked excluded, the way `x-aravind` was kept.

## Inputs

- `prompts/add-profile.md`
- `docs/ADDING_NEW_PROFILES.md`
- Public sources only.

## Steps

1. Choose a kebab-case id from the verified display name. If you cannot verify the person, the id is `x-<handle>`.
2. Create `profiles/<id>/` only. Never write into an existing person's folder to "merge" accounts.
3. Fetch with the official API and public pages, inside the rate limits in `config/sources.yaml`. If the account is private, suspended, or missing, set status `blocked` or `partial` and stop.
4. Run the distill-profile skill.
5. Add the row to `profiles/registry.yaml` with `registry_status: active` only when the folder is real. Re-run the matrix, the dashboard, and `scripts/validate_repo.py`.

## Outputs

A new profile folder and a registry row. Tests must still pass.

## Guardrails

One person per profile. No credentials in the folder. No full post dumps beyond the metadata `posts.jsonl` and short excerpts in `sources.yaml`.

## Related

`prompts/add-profile.md`
