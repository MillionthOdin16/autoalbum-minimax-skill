# Delegated: Build Track Style Card

## Task
Create `tracks/tr_NN/style_card.json` before MiniMax packet compilation.

## Read
- intent_intake.json
- `references/style_catalog/style_catalog_governance.md`
- `references/style_catalog/style_axis_taxonomy.md`
- `references/style_catalog/track_style_card_template.md`
- `references/schemas/track_style_card.schema.json`
- `style_catalog_outputs/style_selection.json`
- `style_catalog_outputs/album_style_map.md`
- selected genre/artist/song profiles
- `planning/tracklist.md`
- `planning/album_arc.md`
- neighboring track cards if available

## Requirements
- Preserve the user's raw style request and reference anchors.
- Identify primary and secondary style profiles.
- Define the track's shared album DNA and track-specific style delta.
- Specify tempo feel, groove, drums, bass/808, harmony, instrumentation, vocal delivery, ad-libs, hook mechanics, lyric posture, arrangement, and mix space.
- Include at least two adjacent-style non-confusion rules for strictness 4-5.
- Separate hard style traits from soft style traits.
- Include avoid/failure-mode instructions.
- Score style card completeness from 0-10.

## Output
Write valid JSON matching `references/schemas/track_style_card.schema.json`.

A style card scoring below 8.0 cannot be compiled into a MiniMax prompt.
