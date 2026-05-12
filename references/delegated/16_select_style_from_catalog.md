# Delegated: Select Style From Catalog

## Task
Resolve the user's raw style request into a concrete AutoAlbum style selection object.

## Read
- intent_intake.json
- `references/style_catalog/README.md`
- `references/style_catalog/style_catalog_router.md`
- all relevant `references/style_catalog/genre_templates/*.md`
- all relevant `references/style_catalog/artist_profiles/*.md`
- `references/style_catalog/song_reference_fingerprint_template.md` if the user names a specific song
- `project_config.json`
- `seed.txt`

## Inputs
- raw user request
- album/track scope
- album concept
- requested genres/artists/songs/eras/scenes
- style strictness if provided

## Process
1. Preserve the exact raw style wording.
2. Extract all named references: artist, song, album, producer, era, scene, genre, subgenre.
3. Prefer specific subgenres over parent genres.
4. If the user says only “rap,” “pop,” “R&B,” “rock,” or “EDM,” choose a more precise lane based on the concept and ask no unnecessary follow-up if enough context exists.
5. If a named artist profile exists, use it.
6. If a specific song is named and no profile exists, build a song reference fingerprint using the template.
7. Assign style weights.
8. Return style selection JSON.

## Output
Save as:

```text
style_catalog_outputs/style_selection.json
```

Return exactly:

```json
{
  "raw_style_request": "...",
  "scope": "album|track|section|variant",
  "style_strictness": 4,
  "primary_style_ids": [],
  "secondary_style_ids": [],
  "reference_anchors": [],
  "style_weights": {},
  "fingerprint_priority": [],
  "selected_catalog_files": [],
  "research_needed": false,
  "missing_profiles_to_create": [],
  "minimax_compilation_notes": "..."
}
```

## Quality bar
The style selection is not acceptable if it only says a broad genre. It must identify the concrete musical behaviors MiniMax should generate.


## V23 catalog-grounding requirement

Write `style_catalog_outputs/style_catalog_verification.json` after style selection.

A selected catalog file must be an actual skill reference under `references/style_catalog/`. Project artifacts such as `source_notes.md`, `concept_tournament.md`, or `seed.txt` are not valid catalog files.

If the selected genre family is rap/hip-hop/trap/drill/rage/pluggnb, load at least one relevant file from `references/style_catalog/rap_current/` or explain why no current-rap profile applies. Any weighted style component greater than 0% must have a fingerprint or be removed.

If the user supplies no style, treat style as a material decision: present distinct style-lane options, ask the user when possible, or explicitly record the autonomous assumption.
