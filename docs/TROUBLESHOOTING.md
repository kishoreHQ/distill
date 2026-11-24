# Troubleshooting

## `validate_repo` says a URL does not match

The board or opportunity file has a URL that is not character-for-character the `url` in that profile's `sources.yaml`. Copy it from the YAML. Do not "clean up" tracking or trailing characters unless you also change the ledger, and do not change the ledger if it is an imported quote of what was fetched.

## `dangling citation`

`[S12]` in a profile must exist in that folder's `sources.yaml`. `[pieter-levels S3]` in knowledge, boards, docs, or intelligence must exist in `profiles/pieter-levels/sources.yaml`. Arnav's ids look like `[arnav-gupta O-ENG-1]`.

## JSONL fails to parse

Read the file by splitting on `\n` only. U+2028 inside a tweet is a line separator. `str.splitlines()` breaks the record. Re-run `import_research_bundle.py` on the archive. It rewrites those separators.

## `posts.jsonl` count does not match `posts_read`

For the 32 research bundles, `posts_read` in `status.json` is the number of posts the researcher counted, and it matches the file after import. For `arnav-gupta`, `posts_read` is 200 from `sync.json` and the file is shorter. `posts_read_note` explains that. The registry field `posts_imported` matches the file, not the 200.

## Refresh did nothing

`X_BEARER_TOKEN` is unset, or the API returned a non-200. Read `intelligence/refresh-status.json`. The briefing still generates. That is the intended degrade path.

A 429 means the shared daily budget was hit. Do not loop. Wait for the next scheduled run. The script does not retry.

## Pytest cannot see the scripts

`pytest.ini` sets `pythonpath = scripts`. Run `python3 -m pytest` from the repo root after `pip install -r requirements.txt`.

## Workflow wants to commit and there is nothing to commit

The daily and weekly jobs check `git diff --cached --quiet` and exit 0 when the tree is unchanged. That is normal on a day when refresh added no posts and the briefing text is stable.

## Matrix primary looks wrong

Read `config/domains.yaml`. The research tag `automation` maps to AI engineering unless an override or a DevOps keyword moves it. Change the rule and re-run `build_matrix.py`. Do not edit `classification-matrix.md` by hand. The validator does not hash the markdown against the JSON beyond the presence of each active id, so a hand edit can drift. Treat the script as the writer.

## Secret scan failed on a post

A stored tweet can theoretically contain a string that looks like a token. If it is a real secret, remove the post text and note the redaction in the profile limitations. If it is a false positive, adjust `SECRET_RES` in `scripts/distilllib.py` narrowly and explain the change in the commit. Do not disable the scan.
