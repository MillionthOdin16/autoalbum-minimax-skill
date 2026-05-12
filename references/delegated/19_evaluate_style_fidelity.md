# Delegated: Evaluate Style Fidelity

## Task
Evaluate whether a compiled MiniMax prompt or generated render preserves the requested style fingerprint.

## Read
- `references/style_catalog/evaluators/style_fidelity_rubric.md`
- `style_catalog_outputs/style_selection.json`
- `style_catalog_outputs/album_style_map.md`
- selected catalog profile files
- `tracks/tr_NN/prompt_minimax.txt`
- `tracks/tr_NN/generation_packet.json`
- rendered audio review notes if post-generation

## Pre-generation output
Save:

```text
tracks/tr_NN/style_fidelity_eval.json
```

Return exactly:

```json
{
  "track_number": 1,
  "style_request_preserved": true,
  "reference_anchors_present": true,
  "genre_mechanics_score": 0.0,
  "artist_fingerprint_score": 0.0,
  "rhythm_groove_score": 0.0,
  "vocal_delivery_score": 0.0,
  "production_texture_score": 0.0,
  "lyric_posture_score": 0.0,
  "album_integration_score": 0.0,
  "overloaded_prompt_risk": "low|medium|high",
  "missing_style_traits": [],
  "conflicting_style_traits": [],
  "ready_for_minimax": false,
  "required_fixes": []
}
```

## Post-generation output
If audio/render notes exist, also score rendered output:

```json
{
  "render_id": "...",
  "followed_reference_anchor": 0.0,
  "drum_groove_match": 0.0,
  "bass_match": 0.0,
  "vocal_delivery_match": 0.0,
  "hook_mechanics_match": 0.0,
  "arrangement_match": 0.0,
  "mix_space_match": 0.0,
  "album_fit": 0.0,
  "recommended_action": "KEEP|SAME_PACKET_NEW_TAKE|PROMPT_MORE_SPECIFIC|PROMPT_SIMPLIFY|STYLE_RETARGET|LYRIC_REWRITE"
}
```
