# Delegated Stage 53 — Regression and Invariant Check

## Goal

After any major revision, verify that the change did not silently damage earlier work.

## Read

- `foundation/album_canon.json`
- `state.json`
- `project_manifest.json`
- `references/architecture/propagation_and_debt_rules.md`
- `references/architecture/transactional_keep_discard_protocol.md`

## Required after

- sound signature change
- lyric voice change
- style lane change
- track order change
- hook rewrite
- prompt rewrite
- selected render replacement
- cut/merge/add track
- provider profile change
- release package update

## Check invariants

- project root remains valid
- canon has no contradictions
- all intentional callbacks remain registered
- no accidental duplicate title/hook phrases
- style request anchors are preserved unless explicitly changed
- tracks remain distinct from neighbors
- prompt and lyrics remain within provider limits
- valid MiniMax tags still used
- selected render IDs still match release metadata
- post-audio sequence still matches selected audio
- no unresolved critical propagation debts
- state and manifest paths resolve

## Outputs

```text
reviews/regression_checks/regression_<timestamp>.json
reviews/regression_checks/regression_<timestamp>.md
```

## Pass criteria

All critical invariants pass. Non-critical failures become propagation debts with owners and next actions.
