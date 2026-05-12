# Delegated Task: Hook, Title, and Chorus Lab

## Objective
Develop a strong listener-memory target before writing full lyrics. This prevents songs from becoming lyrical essays without replay value.

## Read
- `references/agent_training/hook_chorus_lab.md`
- `references/agent_training/songwriting_lyric_field_guide.md`
- `references/agent_training/quality_examples_and_counterexamples.md`
- `references/style_catalog/track_style_card_template.md`
- `tracks/tr_NN/style_card.json`
- `tracks/tr_NN/brief.md`
- `planning/hook_index.md`

## Process
1. Generate 8 title/hook candidates.
2. For each candidate, define hook type and likely delivery.
3. Reject generic or hard-to-sing candidates.
4. Select top 3 and write a two-line chorus nucleus for each.
5. Score memorability, singability/rapability, style fit, album fit, novelty, and MiniMax render likelihood.
6. Select one primary hook and one backup.
7. Update `planning/hook_index.md`.

## Output
Write:

```text
tracks/tr_NN/hook_lab.json
tracks/tr_NN/hook_lab.md
```

JSON must follow `references/schemas/hook_lab.schema.json`.

## Pass criteria
For release-grade work:
- selected hook average score >= 8.0
- singability/rapability >= 8.0
- style fit >= 8.0
- MiniMax render likelihood >= 7.5

If the hook fails, revise before full lyric drafting.
