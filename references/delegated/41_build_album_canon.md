# Delegated 41 — Build and Maintain Album Canon

## Purpose
Create and maintain the album's truth ledger. This is the music equivalent of AutoNovel's canon: hard facts, motifs, style rules, callback rules, accepted render facts, and continuity constraints that future artifacts must obey.

## Read
- `references/architecture/propagation_and_debt_rules.md`
- `references/schemas/album_canon.schema.json`
- `foundation/album_thesis.md`
- `foundation/sound_signature.md`
- `foundation/lyric_voice.md`
- `foundation/vocal_identity.md`
- `style_catalog_outputs/album_style_map.md`
- `planning/tracklist.md` if it exists
- track artifacts and render reviews when updating canon later

## Write
- `<project_slug>/foundation/album_canon.json`
- `<project_slug>/foundation/album_canon.md`

## Canon sections

1. Album identity facts
2. Sonic rules
3. Lyric/narrator/persona rules
4. Style fingerprint commitments
5. Motif ledger entries
6. Vocabulary/callback rules
7. Track-specific established facts
8. Render-accepted facts
9. Prohibited contradictions
10. Open canon debts

## Rules

- Do not include vague aspirations. Canon entries must be enforceable.
- Every intentional callback must be registered.
- Every repeated phrase must be classified as intentional motif or accidental repetition.
- Every selected render can create new canon facts, such as a vocal texture, transition behavior, or recurring sonic motif.
- If canon changes, create propagation debts for affected tracks, prompts, packets, or release metadata.

## Output JSON
Return a valid `album_canon.schema.json` object.
