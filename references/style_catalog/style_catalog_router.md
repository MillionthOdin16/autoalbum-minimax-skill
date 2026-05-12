# Style Catalog Router

Use this router whenever the user asks for a genre, subgenre, artist style, producer style, album style, scene, era, or song-specific reference.

## Inputs

```json
{
  "raw_style_request": "in the style of Juicy J, dark Memphis crunk trap, but with a modern radio hook",
  "album_or_track_scope": "album|track|section|variant",
  "style_strictness": 1,
  "reference_anchors": [],
  "album_context": "..."
}
```

## Resolution order

1. **Exact artist/producer/song reference**
   - Search artist profiles first.
   - If missing, use `song_reference_fingerprint_template.md` or research the reference.
   - Preserve the name in `reference_anchors`.
   - Expand into rhythm, vocal, harmony, instrumentation, arrangement, lyrics, and mix traits.

2. **Exact subgenre**
   - Search `genre_templates/`.
   - Prefer subgenre over parent genre. Example: `Memphis crunk` beats `rap`; `UK drill` beats `hip-hop`.

3. **Parent genre**
   - Use baseline genre card and ask the album concept to supply distinctiveness.
   - For generic terms like “rap,” immediately select a more specific lane: boom bap, trap, melodic trap, drill, Memphis rap, rage, conscious/jazz rap, club rap, etc.

4. **Era/scene request**
   - Map to sound markers: decade, geography, recording fidelity, drum machines, synths, vocal treatment, mix values.
   - Example: “early 2010s Toronto R&B” means shadowy minimal R&B/rap, sparse drums, airy pads, low-pass textures, introspective sung-rap.

5. **Hybrid request**
   - Assign primary/secondary weights.
   - Default blend: 70% primary, 20% secondary, 10% album DNA.
   - Never combine more than three major style anchors in one track prompt unless the user explicitly asks.

## Output: Style Selection Object

```json
{
  "raw_style_request": "...",
  "scope": "album|track|section|variant",
  "style_strictness": 4,
  "primary_style_ids": ["genre.memphis_crunk_trap"],
  "secondary_style_ids": ["artist.juicy_j_three_6_mafia_lane"],
  "reference_anchors": ["Juicy J", "Three 6 Mafia", "Memphis crunk"],
  "style_weights": {
    "genre.memphis_crunk_trap": 0.55,
    "artist.juicy_j_three_6_mafia_lane": 0.35,
    "album_dna": 0.10
  },
  "fingerprint_priority": [
    "808/cowbell/syncopated Memphis bounce",
    "dark minor synth loop",
    "chantable repetitive hook",
    "shouted ad-libs and call-response energy",
    "club/crunk command language"
  ],
  "minimax_compilation_notes": "Use vivid English sentences. Include reference anchors if style strictness >= 4. Keep production details concrete."
}
```

## Style strictness behavior

### Strictness 1: loose color
Use broad genre/mood words. Do not overconstrain.

### Strictness 2: recognizable lane
Include core groove, instrumentation, and vocal mode.

### Strictness 3: specific subgenre
Include tempo, rhythm, drum/bass behavior, vocal delivery, arrangement, and hook type.

### Strictness 4: artist/scene lane
Retain named reference anchors and add a detailed fingerprint. Use 6-10 style constraints.

### Strictness 5: maximum fidelity
Retain named reference anchors; specify era/song/album if provided; encode tempo, drum pocket, bass, vocal effects, section behavior, hook mechanics, lyric posture, and mix space. Generate multiple prompt variants and score style fidelity before rendering.

## MiniMax-specific routing tips

- Direct API: the final style target must be inside the `prompt` field.
- `mmx` CLI: use structured flags when possible: genre, mood, vocals, instruments, bpm, key, structure, references, avoid, use_case.
- Use artist/song names plus descriptors; names alone are too underspecified.
- Do not put production instructions in the lyrics field.
- Use structure tags only from the selected MiniMax tag profile.

## Current rap catalog routing

When the user requests a current rap style, current rapper, rap hit, or specific rap-song lane, read these files before compiling style prompts:

1. `references/style_catalog/rap_current/current_popularity_basis_2026.md`
2. `references/style_catalog/rap_current/artist_fingerprints/current_rap_artist_fingerprints.md`
3. `references/style_catalog/rap_current/song_fingerprints/current_rap_song_fingerprints.md`
4. `references/style_catalog/rap_current/style_differentiation_matrix.md`
5. `references/style_catalog/rap_current/prompts/minimax_rap_prompt_recipes.md`
6. `references/style_catalog/rap_current/evaluators/rap_style_fidelity_rubric.md`

### Routing rules

- If the request names a rapper, use the matching artist fingerprint at strictness 4 by default.
- If the request says “as close as possible,” “make it like,” “sounds like,” or names a specific song, use strictness 5.
- If the request names both an artist and a song, prioritize the song fingerprint for track architecture and the artist fingerprint for vocal/lyric posture.
- If the request names multiple artists, assign roles instead of averaging:
  - beat/production source
  - vocal source
  - hook source
  - lyric posture source
  - mix-space source
- Always run the differentiation matrix before finalizing prompts.

## Non-rap expansion routing
If the style request is not primarily rap/current hip-hop, consult `references/style_catalog/non_rap_expansion/` before approving a style card. Select the most relevant detailed fingerprint and transfer its concrete controls into the style card: groove, drums, bass, harmony, instrument palette, vocal delivery, hook mechanics, arrangement, mix space, failure modes, and adjacent-style differentiators.

A non-rap style card fails if it only says "pop", "R&B", "house", "country", "rock", "Latin", or another broad label without the mechanics that make that style audible.
