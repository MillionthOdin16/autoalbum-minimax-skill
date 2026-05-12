# AutoAlbum Style Catalog

The style catalog is the skill's library of genre, artist, scene, era, and song-reference fingerprints. Its purpose is to turn a user's style request into MiniMax Music 2.6-ready musical control data.

The catalog is not a list of vague moods. Every useful style profile should identify actionable traits:

- tempo range and tempo feel
- meter and groove
- drums and percussion
- bass behavior
- harmonic language
- melodic/topline behavior
- vocal delivery
- ad-lib behavior
- lyric mode and subject posture
- instrumentation
- arrangement arc
- mix/space/aesthetic texture
- album-placement use cases
- MiniMax prompt fragments
- MiniMax structure-tag recommendations
- avoid-list / failure modes

## Core operating rule

When a user names a genre, subgenre, artist, producer, album, era, or specific song, preserve the reference as part of the style request and then expand it into concrete musical parameters. Artist or song names alone are usually weaker than artist/song names plus detailed fingerprints.

## Style request hierarchy

1. **Raw user request**: Keep the exact style wording.
2. **Reference anchors**: Artist names, songs, albums, eras, scenes, labels, producers.
3. **Fingerprint extraction**: Translate references into audible traits.
4. **Album style map**: Define shared album DNA and per-track deviations.
5. **Track style card**: Convert the chosen style into track-specific control data.
6. **MiniMax prompt**: Compile the style card into a vivid English prompt under API limits.
7. **Fidelity evaluation**: Check whether the prompt still carries the style fingerprint.

## Recommended style strictness values

```json
{
  "1": "loose influence: light color only",
  "2": "recognizable genre lane",
  "3": "clear style target with moderate specificity",
  "4": "strict style fingerprint; named references retained",
  "5": "maximum style adherence; named anchors plus detailed production/vocal/rhythmic fingerprint"
}
```

Default for user-specified artist/song references: `style_strictness = 4`.
Default for genre-only requests: `style_strictness = 3`.
Use `style_strictness = 5` when the user explicitly asks for the closest possible match to a reference.

## Catalog files

- `style_catalog_router.md`: how to resolve user style requests.
- `minimax_style_compiler.md`: how to turn style cards into MiniMax prompts.
- `album_style_map_template.md`: album-level style planning.
- `song_reference_fingerprint_template.md`: method for specific songs not already cataloged.
- `fusion_matrix.md`: how to combine styles without making mud.
- `style_profile.schema.json`: machine-readable style profile format.
- `genre_templates/`: baseline genre/subgenre fingerprints.
- `artist_profiles/`: artist/producer/era fingerprints.
- `evaluators/style_fidelity_rubric.md`: quality gate for style matching.
