
# Delegated: Line Polish Review

## Task
Perform a harsh line-level lyric polish review before MiniMax packet approval. This stage exists because meaningful lyrics can still fail as professional song lyrics.

## Read
- `tracks/tr_NN/lyrics_minimax.txt` if present, otherwise `tracks/tr_NN/lyrics_working.md`
- `tracks/tr_NN/style_card.json`
- `style_catalog_outputs/style_selection.json`
- `references/agent_training/songwriting_lyric_field_guide.md`
- `references/agent_training/prosody_scansion_worked_examples.md`

## Output
- `tracks/tr_NN/line_polish_review.json`
- `tracks/tr_NN/line_polish_patch.md`
- `tracks/tr_NN/lyrics_verifier_review.json`

## Required checks
Identify and fix:

- awkward idiom,
- unclear slang,
- forced rhyme,
- melodrama,
- censored weak language,
- out-of-character phrasing,
- non-performable line length,
- bad or wrong image,
- generic bar,
- unearned emotional spike,
- lines that do not match the selected style/voice.

## Minimum harshness rule
Quote at least five weakest lines unless the lyric is already release-grade. If fewer than five issues are found, explain why and name the strongest three lines.

## Score cap rule
If any clunky line remains in the hook or first verse, `professional_quality_score` must be <= 7.4. Do not give major-release scores to merely coherent draft lyrics.
