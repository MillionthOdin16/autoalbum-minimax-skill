# Results TSV Spec

`<project_slug>/results.tsv` is an optional flat ledger for quick human inspection. It does not replace `state.json`, `project_manifest.json`, or `ops/render_log.jsonl`.

Required header:

```tsv
timestamp	stage	track_number	artifact_id	variant_id	score_type	score	status	decision	path	notes
```

Rules:

- Append only; never rewrite historical rows.
- Use `track_number` blank for album-level events.
- Use `score_type` values such as `songcraft`, `style_fidelity`, `minimax_packet`, `render_candidate`, `sequence`, `aandr`.
- Link the canonical artifact path in `path`.
- Keep machine state in `state.json`; use this TSV only as a quick scoreboard.
