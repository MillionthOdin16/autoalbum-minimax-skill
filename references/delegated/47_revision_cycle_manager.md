# Delegated 47 — Revision Cycle Manager

## Purpose
Manage revision loops so the agent improves quality without endless churn. This is AutoAlbum's plateau-aware revision controller.

## Read
- `references/architecture/quality_loop_controller.md`
- `references/schemas/revision_cycle.schema.json`
- latest unified evaluations
- `results.tsv`
- `state.json`
- open propagation debts

## Write

```text
reviews/revision_cycle_<cycle_num>.json
reviews/revision_cycle_<cycle_num>.md
```

## Tasks

1. Identify the weakest dimension.
2. Identify the smallest high-leverage action.
3. Check whether similar attempts already failed.
4. Decide whether to revise, regenerate, cut, replace, resequence, accept with justification, or escalate.
5. Update state, results, debts, and manifest.

## Plateau rule

If the same dimension fails to improve after three targeted attempts or score movement remains within +/- 0.2 across three attempts, stop repeating that approach. Choose a structural alternative:

```text
CUT_TRACK
REPLACE_TRACK
CHANGE_HOOK
CHANGE_STYLE_LANE
SIMPLIFY_PROMPT
REWRITE_LYRICS
RESEQUENCE
ADD_INTERLUDE
ACCEPT_WITH_JUSTIFICATION
ESCALATE_TO_HUMAN
```

## Output decision

Return one of:

```text
CONTINUE_CURRENT_LOOP
CHANGE_STRATEGY
CUT_OR_REPLACE
READY_TO_ADVANCE
ESCALATE
```
