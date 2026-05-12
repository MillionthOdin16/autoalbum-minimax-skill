# Current Rap Style Catalog

Purpose: provide high-fidelity, MiniMax Music 2.6-ready style fingerprints for current mainstream rap, trap, rage, melodic rap, pain rap, conscious rap, Memphis club rap, UK drill-pop, and rap/R&B crossover lanes.

This catalog is designed for direct use by AutoAlbum when a user asks for a current rap album, a specific rap substyle, a current artist lane, or a song-reference lane.

## Core operating rule

When a user names an artist or song, preserve the named reference in the internal style record and expand it into concrete musical controls:

- tempo and groove
- drum programming
- 808/bass behavior
- harmonic palette
- melodic/instrumental palette
- vocal delivery and cadence
- hook mechanics
- ad-lib system
- arrangement architecture
- mix space
- lyric posture
- album role
- MiniMax prompt capsule
- differentiation notes

Do not collapse distinct artists into generic labels like "trap" or "rap." For example, Future, Gunna, Lil Baby, and Young Thug are all Atlanta trap-adjacent, but their vocal pocket, hook logic, lyric posture, and production density differ enough that they must remain separate profiles.

## Files

- `current_popularity_basis_2026.md` — selection basis and source notes.
- `artist_fingerprints/current_rap_artist_fingerprints.md` — detailed profiles for major current rappers and rap-adjacent vocalists.
- `song_fingerprints/current_rap_song_fingerprints.md` — detailed track-reference cards for popular/current rap songs.
- `style_differentiation_matrix.md` — prevents blurring adjacent artists.
- `prompts/minimax_rap_prompt_recipes.md` — ready-to-use MiniMax style-prompt templates.
- `evaluators/rap_style_fidelity_rubric.md` — scoring rubric for style match.

## How AutoAlbum should use this catalog

1. Parse the user request: genre, subgenre, artist, song, era, tempo, energy, explicitness, and album role.
2. Select a base genre card from `genre_templates/hiphop_rap.md`.
3. Select one or more artist/song fingerprints from this folder.
4. Build a per-album style map:
   - shared sonic DNA
   - track-specific deltas
   - artist/song reference anchors
   - no two tracks allowed to collapse into the same fingerprint unless intentionally paired
5. Compile each track into a MiniMax packet:
   - vivid English prompt, not tag pile
   - supplied lyrics with valid MiniMax tags
   - avoid/failure modes
   - hard/soft constraints
6. Run style fidelity evaluation before generation and again after hearing the render.

## Style strictness scale

- 1: loose rap influence
- 2: broad subgenre lane
- 3: recognizable current rap lane
- 4: artist/song-specific fingerprint
- 5: maximum reference fidelity

Artist/song requests default to 4. "As close as possible" defaults to 5.


## Quality additions

Read these before using strict current-rap requests:

```text
profile_quality_standards.md
current_rap_refresh_2026_05_11.md
```

A profile is not approved for strictness 4-5 use unless it passes the profile quality standards and has enough differentiators to avoid collapsing into adjacent rap styles.
