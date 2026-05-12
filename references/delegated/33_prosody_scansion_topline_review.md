# Delegated Task: Prosody, Scansion, and Topline Review

## Objective
Review one track's lyrics as a professional songwriter, topliner, rapper/vocal arranger, and producer. Identify whether the lyric can be convincingly performed in the requested style and whether the hook has real replay value.

## Read
- `<project_slug>/project_config.json`
- `<project_slug>/foundation/lyric_voice.md`
- `<project_slug>/foundation/vocal_identity.md`
- `<project_slug>/planning/tracklist.md`
- `<project_slug>/tracks/tr_NN/brief.md`
- `<project_slug>/tracks/tr_NN/style_card.json`
- `<project_slug>/tracks/tr_NN/lyrics_working.md`
- `references/craft/prosody_scansion_and_topline_gate.md`
- `references/schemas/prosody_review.schema.json`

## Analyze
1. Mark the primary hook phrase and decide whether it is memorable and performable.
2. Scan chorus/hook lines for syllables, stress, vowel shape, consonant friction, and repetition value.
3. Scan at least one verse for cadence, breath points, rhyme density, and style fit.
4. Check whether section-to-section phrasing creates contrast.
5. Check whether the lyric format can be converted cleanly to `lyrics_minimax.txt`.
6. Identify the smallest changes that would most improve delivery.

## Output
Write:

```text
<project_slug>/tracks/tr_NN/prosody_review.json
<project_slug>/tracks/tr_NN/prosody_review.md
```

Return exactly the JSON object described by `prosody_review.schema.json` in the JSON file.

## Decision rules
- If `ready_for_packet_compilation` is false, revise lyrics before MiniMax packet compilation.
- If the hook fails, do not approve the track by averaging the score upward with strong verses.
- If the lyric is intentionally dense, explain the rhythmic logic that makes it performable.
- If the song is rap, evaluate bar feel, pocket, internal rhyme, flow switching, and ad-lib placement.
- If the song is melodic, evaluate vowel openness, phrase length, breath, chorus lift, and emotional clarity.
