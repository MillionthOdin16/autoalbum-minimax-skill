# Style Request Resolution Protocol

## Purpose
Turn user style language into usable musical controls without diluting specificity.

## Inputs
- raw user style request
- project scope
- references: genre, subgenre, artist, producer, song, album, era, region, scene, playlist, or mood
- requested strictness, explicit or inferred

## Output
`style_catalog_outputs/style_selection.json` and the style portion of each `tracks/tr_NN/style_card.json`.

## Strictness

```text
1 = loose mood/style influence
2 = broad recognizable genre lane
3 = specific subgenre/scene
4 = artist/song/producer/era fingerprint
5 = closest-possible style adherence
```

If the user names an artist or song, default to 4. If the user says “as close as possible,” “exactly like,” or “make it sound like,” default to 5.

## Resolution process
1. Preserve the raw wording.
2. Identify all reference anchors.
3. Select catalog profiles.
4. If missing, create an ad hoc fingerprint from research or supplied description.
5. Translate references into axes:
   - tempo/feel,
   - groove/meter,
   - drums,
   - bass/808,
   - harmony/melody,
   - instruments/sound design,
   - vocal delivery,
   - ad-libs,
   - hook mechanics,
   - lyric posture,
   - arrangement,
   - mix/space,
   - failure modes.
6. Define adjacent-style non-confusion rules.
7. Set style-fidelity targets.

## Broad style requests
If the user says only “rap,” “pop,” “R&B,” “rock,” or “EDM,” infer a concrete lane based on concept and appeal target. Document the inference.

Example:
```text
User: “rap album about becoming rich and paranoid”
Likely lane: dark melodic trap / cinematic street rap / paranoia-focused trap, not generic rap.
```

## Multi-style albums
For albums with multiple styles, define:
- shared album DNA,
- style weights,
- track-specific deltas,
- transition logic,
- which tracks are allowed to break the core style and why.

## Failure condition
A style selection fails if it only names labels and does not produce audible MiniMax controls.
