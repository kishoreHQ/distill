# Prompt: add-profile

Add one person.

Handle: `<handle>`
Proposed id: `<id>`

Confirm the account is the person intended. If it is not, keep any mistaken bundle and mark it excluded. Do not delete it and do not merge it into the right person.

Create only `profiles/<id>/`. Use public pages and the official API. Respect `config/sources.yaml` rate limits. If a fetch fails, record the failure in `status.json` and stop.

No credentials in the folder. Short excerpts only. Then run classify-profile and validate-repo.
