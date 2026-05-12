# Style Fidelity Rubric

Use this after compiling `prompt_minimax.txt` and after hearing generated audio.

## Pre-generation style fidelity JSON

```json
{
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
  "ready_for_minimax": false
}
```

## Minimum gates

For style strictness 4:

```text
artist_fingerprint_score >= 8.0
rhythm_groove_score >= 8.0
vocal_delivery_score >= 7.5
production_texture_score >= 7.5
album_integration_score >= 7.5
```

For style strictness 5:

```text
artist_fingerprint_score >= 8.7
rhythm_groove_score >= 8.5
vocal_delivery_score >= 8.3
production_texture_score >= 8.3
album_integration_score >= 7.0
```

## Post-generation evaluation

Score the rendered track against the intended fingerprint:

```json
{
  "render_id": "...",
  "style_target": "...",
  "followed_reference_anchor": 0.0,
  "drum_groove_match": 0.0,
  "bass_match": 0.0,
  "vocal_delivery_match": 0.0,
  "hook_mechanics_match": 0.0,
  "arrangement_match": 0.0,
  "mix_space_match": 0.0,
  "album_fit": 0.0,
  "best_matching_traits": [],
  "failed_traits": [],
  "recommended_action": "KEEP|SAME_PACKET_NEW_TAKE|PROMPT_MORE_SPECIFIC|PROMPT_SIMPLIFY|STYLE_RETARGET|LYRIC_REWRITE"
}
```

## Common failures and fixes

| Failure | Cause | Fix |
|---|---|---|
| MiniMax produced generic pop | prompt had mood but no groove/drum/bass/vocal fingerprint | add style card traits and reference anchor |
| Rap track lacks regional identity | prompt said “rap” only | choose subgenre/scene card |
| Artist influence disappeared | name was omitted or not translated | include reference anchor plus fingerprint priority |
| Prompt ignored rhythm | too much lore, not enough music | move story to one sentence, add groove/drums/bass |
| All tracks sound same | album DNA not balanced with track deltas | revise album style map and contrast matrix |
| Track is accurate but not appealing | fingerprint lacks hook mechanics | add hook contract and chorus/post-chorus directive |
