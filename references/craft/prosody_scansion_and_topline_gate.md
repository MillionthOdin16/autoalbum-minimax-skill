# Prosody, Scansion, and Topline Gate

## Purpose
This gate prevents AutoAlbum from producing lyrics that read well on paper but fail as sung or rapped music. A lyric is not approved until it has a plausible delivery rhythm, stress pattern, breath design, hook shape, and section-level energy contour.

## Core principle
Words must land where a performer can deliver them. Meaning, stress, rhyme, vowel shape, and melodic/rhythmic contour must reinforce each other. If the lyric sounds clever but cannot be naturally sung, rapped, or phrased in the requested style, it fails.

## Required review dimensions

### 1. Natural speech stress
For every hook and at least one verse, mark the stressed words. The strongest semantic words should not be forced into weak rhythmic positions. Fix lines where the ordinary spoken emphasis fights the intended groove.

### 2. Syllable density and breath map
For every section, estimate syllable density:

```text
sparse: 4-7 syllables per line
moderate: 8-12 syllables per line
dense: 13-18+ syllables per line
```

Then mark expected breath points. Dense rap may intentionally exceed these ranges, but it must still have controlled internal pauses, bar turns, or triplet/double-time logic. Pop/R&B hooks should usually avoid dense syllable stacking unless the style specifically calls for it.

### 3. Hook phonetics
Every lead hook must be checked for:

```text
open vowels on long notes or likely emphasized words
memorable title phrase or title-adjacent phrase
repeatable melodic/rhythmic cell
low friction consonants at fast tempos
no tongue-twister collisions unless the style wants aggression
```

### 4. Rhyme and cadence design
Identify whether the song uses end rhyme, internal rhyme, multisyllabic rhyme, assonance, slant rhyme, chant repetition, or melodic repetition. The rhyme design should match the style card. A Kendrick-like dense rap lane needs different rhyme/cadence expectations than a dark pop hook, Memphis chant record, Afrobeats groove, or country chorus.

### 5. Section contrast
Verses, pre-choruses, hooks, bridges, breaks, and outros need different functions. The prosody gate fails if every section has the same line length, stress rhythm, rhyme density, and emotional pressure.

### 6. Performance feasibility
Check whether the requested vocal persona can plausibly deliver the text. A whispery intimate vocal cannot carry overstuffed tongue-twister hooks. A shouted club chant does not need literary subtlety. A melodic trap flow needs room for pitch contour and ad-libs.

### 7. MiniMax compatibility
The final `lyrics_minimax.txt` must use only provider-valid structure tags. Do not bury production notes inside lyrics. Performance clues belong in `prompt_minimax.txt` unless the provider explicitly supports bracketed stage directions.

## Failure conditions
A track fails this gate if any of the following are true:

```text
hook is not singable/chantable after one listen
section labels are invalid for the selected provider
chorus is too wordy to feel like a chorus
verse cadence does not match requested genre/style
line stress fights the intended groove
breath map is impossible or exhausting without purpose
rhyme pattern becomes monotonous or accidental
bridge/break does not change perspective, rhythm, harmony, texture, or energy
lyrics read like a poem rather than a performable song
```

## Required output
Write `tracks/tr_NN/prosody_review.json` using `references/schemas/prosody_review.schema.json` and write a human-readable summary to `tracks/tr_NN/prosody_review.md`.

## Approval threshold

```text
prosody_score >= 8.0
hook_singability_score >= 8.0
section_contrast_score >= 7.5
breath_feasibility_score >= 7.5
style_delivery_fit >= 8.0
```

A track cannot proceed to MiniMax packet compilation until this gate passes or a named exception is recorded in `state.json` with rationale.
