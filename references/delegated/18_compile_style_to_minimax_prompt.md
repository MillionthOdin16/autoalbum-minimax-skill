# Delegated: Compile Style To MiniMax Prompt

## Task
Convert the selected style fingerprint and track brief into MiniMax-compatible prompt text.

## Read
- `references/style_catalog/minimax_style_compiler.md`
- `style_catalog_outputs/style_selection.json`
- `style_catalog_outputs/album_style_map.md`
- selected catalog profile files
- `tracks/tr_NN/brief.md`
- `tracks/tr_NN/lyrics_minimax.txt`
- `references/model_profiles/minimax_music_2_6.md`

## Output
Update:

```text
tracks/tr_NN/prompt_minimax.txt
tracks/tr_NN/generation_packet.json
```

## Prompt requirements
- Prompt must be English unless user explicitly requests otherwise.
- Prompt must be vivid sentences, not a comma-separated tag pile.
- Prompt must preserve named reference anchors when style strictness >= 4.
- Prompt must contain rhythm/groove, vocal identity, production texture, hook mechanics, and arrangement arc.
- Prompt must include album DNA and track-specific delta.
- Prompt must be <= 2000 characters.
- Production details go in prompt, not lyrics.

## Generation packet additions
Add or update:

```json
{
  "style_selection": {},
  "style_card": {},
  "style_strictness": 4,
  "reference_anchors": [],
  "style_fidelity_targets": []
}
```

## Quality bar
The prompt should allow someone to infer the intended style without reading the original user request.
