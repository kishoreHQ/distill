# Prompt: refresh-profile

Refresh post metadata for `<id>`.

If `X_BEARER_TOKEN` is absent, reply that live refresh was skipped and do not invent posts.

If it is present:

- Use the official X API only.
- Query `from:<username> -is:retweet`.
- At most 10 posts.
- Append unseen ids to `posts.jsonl` with `"origin": "refresh"`.
- Do not rewrite `profile.md`.
- Do not print the token.
- On 401, 403, or 429, record the code and stop.

Do not raise research_status. New rows are unread.
