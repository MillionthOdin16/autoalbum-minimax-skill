# Delegated Task: Track Preproduction Brief

## Objective
Create a concise, musically grounded preproduction brief that bridges planning, lyrics, style, arrangement, and MiniMax prompt compilation.

## Read
- `references/agent_training/musical_expertise_bootcamp.md`
- `references/agent_training/production_mix_mastering_primer.md`
- `references/agent_training/minimax_control_cookbook.md`
- `tracks/tr_NN/brief.md`
- `tracks/tr_NN/style_card.json`
- `tracks/tr_NN/hook_lab.json`
- `tracks/tr_NN/arrangement_energy_review.json`
- `tracks/tr_NN/prosody_review.json`

## Output
Write:

```text
tracks/tr_NN/preproduction_brief.json
tracks/tr_NN/preproduction_brief.md
```

JSON must follow `references/schemas/preproduction_brief.schema.json`.

## Required sections
- song identity in one sentence
- album role
- hook contract
- style fingerprint controls
- vocal delivery
- groove/drum/bass plan
- harmony/melody/topline plan
- arrangement/tension plan
- production/mix-space plan
- MiniMax prompt priorities
- what to omit from the prompt
- likely MiniMax failure modes

## Rule
Do not compile `prompt_minimax.txt` until the preproduction brief exists and is coherent.
