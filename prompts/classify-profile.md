# Prompt: classify-profile

Classify `<id>` into the five domains in `config/domains.yaml`.

Read the front matter. Apply `research_domain_map`, then overrides, then keyword secondaries. Aggregators stay signal feeds.

Return:

- primary domain id
- secondary domain ids with the rule name (`research:`, `keyword:`, `override`, `extra`)
- one sentence pointing at the front-matter field or source that justified an override

Do not add a domain because it would make a board more interesting. Re-run `scripts/build_matrix.py` rather than editing the matrix by hand.
