# Delegated: Compare Render Candidates

## Task
Compare MiniMax render candidates for one track and choose keep/regenerate/cut actions.

## Read
- `tracks/tr_NN/style_card.json`
- `tracks/tr_NN/generation_packet.json`
- `tracks/tr_NN/variants/*.json`
- `ops/render_log.jsonl`
- audio review notes or human listening notes for each render
- `references/craft/pro_album_a_and_r_standards.md`
- `references/api/minimax_high_control_protocol.md`

## Candidate scorecard
Return JSON with:

```json
{
  "track_number": 1,
  "candidates": [
    {
      "render_id": "",
      "variant": "A_on_brief",
      "lyric_adherence": 0,
      "style_fidelity": 0,
      "hook_impact": 0,
      "vocal_identity": 0,
      "groove_bass_match": 0,
      "arrangement_motion": 0,
      "audio_artifacts": 0,
      "album_fit": 0,
      "distinctiveness": 0,
      "overall": 0,
      "keep_reason": "",
      "failure_reason": ""
    }
  ],
  "winner_render_id": "",
  "recommended_action": "KEEP|SAME_PACKET_NEW_TAKE|PROMPT_MORE_SPECIFIC|PROMPT_SIMPLIFY|LYRIC_REWRITE|STYLE_RETARGET|CUT_TRACK",
  "regeneration_brief_needed": true,
  "notes": ""
}
```

## Rules
- Do not choose the cleanest audio if it loses the requested style.
- Do not choose the most stylish audio if the hook fails.
- If all candidates fail for the same reason, revise the packet rather than generating more takes.
- If variants fail in different ways, combine the best control traits into a new variant.

## Listening-note requirement
Every candidate comparison must include timestamped notes for standout moments, flaws, artifacts, hook impact, and transition implications. Use `references/schemas/timestamped_listening_notes.schema.json` for machine-readable notes when audio is available.
