# Prompt: validate-repo

Check this repo. Do not fetch the network.

Run:

```
python3 scripts/validate_repo.py
python3 -m pytest
```

Report the exit codes. If validation fails, list the errors and fix only the ones that are broken citations, schema mismatches, or missing disclaimers. Do not invent a source to make a citation pass. Do not weaken a test to hide a real mismatch.

Confirm:

- 32 active profiles and `x-aravind` excluded
- `aravind-srinivas` and `arnav-gupta` active
- five boards contain the simulated-board disclaimer
- opportunity weights sum to 100
- no token material in the tree
