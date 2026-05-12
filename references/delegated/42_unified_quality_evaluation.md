# Delegated 42 — Unified Quality Evaluation

## Purpose
Create one evaluation summary that combines the many specialized AutoAlbum gates into a single decision for the current scope. This is the AutoAlbum equivalent of AutoNovel's phase/chapter/full evaluator.

## Scope values

```text
foundation
track_pre_packet
track_packet_ready
track_post_render
album_pre_render
album_post_render
release_package
```

## Read
Use only artifacts relevant to the selected scope. Always read:

- `references/schemas/unified_eval.schema.json`
- `references/architecture/quality_loop_controller.md`
- `references/architecture/propagation_and_debt_rules.md`
- `state.json`
- `project_manifest.json`
- any scope-specific reviews/evals already produced

## Evaluation dimensions

Use the relevant subset:

```text
concept_strength
style_fidelity
album_canon_integrity
songcraft
hook_strength
prosody_performability
arrangement_energy
minimax_prompt_control
provider_validity
candidate_audio_quality
listener_appeal
album_cohesion
sequence_flow
technical_audio_qc
release_readiness
```

## Output
Write:

```text
reviews/unified_eval_<scope>_<timestamp>.json
reviews/unified_eval_<scope>_<timestamp>.md
```

Return valid `unified_eval.schema.json`.

## Decision values

```text
PASS
PASS_WITH_DEBTS
REVISE
REGENERATE
CUT_OR_REPLACE
ESCALATE
FAIL
```

## Required behavior

- Identify the weakest dimension.
- Identify the single next best action.
- Distinguish pre-render hypotheses from post-render evidence.
- Do not pass a stage with unresolved critical debts.
- Update `state.json`, `project_manifest.json`, and `results.tsv` after evaluation.
