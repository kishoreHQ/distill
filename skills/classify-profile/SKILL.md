---
name: classify-profile
description: Assign one active profile to the five DISTILL domains using the rules in config/domains.yaml.
---

# classify-profile

## When to use

After a profile's front matter changes, or when the matrix looks wrong for one id.

## Inputs

- `config/domains.yaml`
- The profile front matter (research primary and secondary tags, role, organization, account type).
- `prompts/classify-profile.md`

## Steps

1. Map the research tags with `research_domain_map`. Do not invent a sixth domain.
2. Apply `primary_overrides` and the automation keyword rule only when the config names them. Write the because-line into the matrix note.
3. Add keyword secondaries only for the account types the rule allows. Aggregators do not get a "builder" secondary from a GitHub link in the bio.
4. Re-run `python3 scripts/build_matrix.py`. Do not hand-edit `knowledge/classification-matrix.md`.
5. If the person is `x-aravind`, do not classify them as active. They stay excluded.

## Outputs

Updated `knowledge/classification-matrix.md` and `.json`.

## Guardrails

Classification is not board consent. `board_eligibility` in the old spec is a hint. The five simulated boards are a separate, labelled fiction.

## Related

`prompts/classify-profile.md`
