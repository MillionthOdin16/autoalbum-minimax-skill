# Style Catalog QA Checklist

Use this checklist before approving a genre, artist, song, or fusion style profile for strictness 4-5 generation.

## Minimum required fields

A usable profile must define:

```text
1. style_id
2. plain-language lane
3. best use cases
4. tempo / feel range
5. drum pattern and swing/pocket
6. bass / 808 behavior
7. harmonic color and melodic language
8. instrument / texture palette
9. vocal delivery and vocal processing
10. ad-lib / background vocal behavior when relevant
11. hook mechanics
12. lyric posture and subject-matter tendencies
13. arrangement architecture
14. mix / space
15. MiniMax prompt capsule
16. adjacent-style differentiators
17. failure modes
18. album integration guidance
19. confidence/currentness notes
```

If any of items 4-15 are missing, the profile is not ready for high-fidelity generation.

## Anti-generic test

Ask whether the profile could also describe three other artists or genres. If yes, it is too generic.

Bad:

```text
modern trap with hard 808s, catchy hook, confident vocals
```

Good:

```text
slow-to-mid tempo Atlanta motivational street trap with urgent triplet/double-time pockets, clean piano/guitar loop, punchy but not psychedelic 808s, clipped aspirational verses, no slurred narcotic melody, and a hook that sounds like a disciplined comeback mantra rather than a party chant
```

## Differentiation test

For every artist profile, explicitly distinguish it from at least three adjacent profiles.

Examples:

```text
Future vs Gunna: slurred narcotic emotion vs smooth polished glide.
Gunna vs Lil Baby: relaxed elastic pocket vs urgent motivational pressure.
Carti vs Yeat: punk vamp ad-lib chaos vs robotic alien lexicon and bell/synth churn.
Drake vs Don Toliver: diaristic narrator and luxury grievance vs psychedelic floating melodic texture.
Kendrick vs J. Cole: theatrical character-switching and regional chant energy vs reflective everyman technical clarity.
```

## MiniMax usability test

A profile is only useful if it can compile to a 700-1400 character MiniMax prompt without losing its identity.

The compiled prompt must include:

```text
mood + genre/subgenre
vocal identity
rhythmic/groove instruction
2-4 production elements
hook behavior
scene or emotional premise
one clear differentiator
```

Do not copy the entire profile into the prompt.

## Song-reference test

A song-reference card must describe the reference at the level of:

```text
tempo/feel
drum groove
bass behavior
harmonic/melodic language
main texture
vocal role
hook role
arrangement event
mix space
best use case
what to preserve
what not to collapse into
```

## Album integration test

Every style profile must answer:

```text
How can this style define an entire album?
How can it appear as one track inside a different album style?
What adjacent styles can blend with it cleanly?
What adjacent styles will muddy it?
```

## Currentness test

For current-pop profiles, maintain:

```text
last_reviewed_date
source_basis
chart/streaming/cultural signal
currentness: evergreen | active-current | emerging-current | legacy-reference
update_priority: low | medium | high
```

## Failure responses

If a profile fails QA:

```text
- mark status: needs_refinement
- list missing fields
- identify adjacent-style blur risk
- generate a refined fingerprint before using it
```

## Expanded QA requirement
For non-rap styles, run the same specificity standard as current rap. A profile must not pass unless it identifies tempo/groove, drums, bass, harmony, instrument palette, vocal delivery, hook mechanics, arrangement, mix space, failure modes, and adjacent-style differentiation. Use `references/style_catalog/non_rap_expansion/evaluators/non_rap_style_fidelity_rubric.md` for scoring.
