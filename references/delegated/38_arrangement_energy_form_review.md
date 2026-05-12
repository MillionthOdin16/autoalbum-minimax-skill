# Delegated Task: Arrangement, Energy, and Form Review

## Objective
Verify that the track has a professional musical shape before MiniMax packet compilation.

## Read
- `references/agent_training/arrangement_form_energy_manual.md`
- `references/agent_training/harmony_melody_groove_primer.md`
- `references/agent_training/production_mix_mastering_primer.md`
- `tracks/tr_NN/brief.md`
- `tracks/tr_NN/style_card.json`
- `tracks/tr_NN/hook_lab.json`
- `tracks/tr_NN/lyrics_working.md`

## Analyze
- section map
- section energy levels
- groove and bass behavior
- hook entrance
- bridge/break purpose
- contrast from adjacent tracks
- MiniMax supported structure tags
- tension/release mechanism
- whether the arrangement matches the requested style

## Output
Write:

```text
tracks/tr_NN/arrangement_energy_review.json
tracks/tr_NN/arrangement_energy_review.md
```

JSON must follow `references/schemas/arrangement_energy_review.schema.json`.

## Pass criteria
- section_energy_map_complete == true
- hook_entrance_strategy_score >= 8.0
- arrangement_contrast_score >= 7.5
- style_form_fit_score >= 8.0
- no unresolved structure/tag blockers
