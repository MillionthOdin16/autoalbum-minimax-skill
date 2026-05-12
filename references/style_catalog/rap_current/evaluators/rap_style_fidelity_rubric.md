# Rap Style Fidelity Rubric

Run this before MiniMax generation and again after listening to each render.

## Scoring dimensions

Return exact JSON:

```json
{
  "requested_reference": "",
  "style_strictness": 5,
  "genre_mechanics_score": 0.0,
  "artist_fingerprint_score": 0.0,
  "song_reference_score": 0.0,
  "tempo_groove_score": 0.0,
  "drum_bass_score": 0.0,
  "vocal_delivery_score": 0.0,
  "hook_mechanics_score": 0.0,
  "lyric_posture_score": 0.0,
  "arrangement_score": 0.0,
  "mix_texture_score": 0.0,
  "differentiation_score": 0.0,
  "album_fit_score": 0.0,
  "overall_style_fidelity": 0.0,
  "critical_misses": [],
  "repair_actions": []
}
```

## Thresholds

- Strictness 3: pass if overall >= 7.5 and no critical miss.
- Strictness 4: pass if overall >= 8.2 and artist_fingerprint >= 8.0.
- Strictness 5: pass if overall >= 8.8, artist_fingerprint >= 8.7, and differentiation_score >= 8.5.

## Critical misses

Flag as critical if any are true:

- Artist request collapses into generic trap.
- Requested vocal posture is missing.
- Wrong drum language: e.g., UK drill request becomes Atlanta trap.
- Hook mechanics are wrong: e.g., chant request becomes sung pop chorus.
- Mix texture is wrong: e.g., Carti/Opium request becomes clean pop-trap.
- Adjacent artist confusion: e.g., Future prompt sounds like Drake, Gunna prompt sounds like Lil Baby, Sexyy Red prompt sounds like Cardi.
- Song reference role is wrong: e.g., `luther` lane becomes diss track, `FE!N` lane becomes lyric-heavy storytelling.

## Repair actions

Use one or more:

- `RECOMPILE_PROMPT_WITH_STRONGER_DRUMS`
- `RECOMPILE_PROMPT_WITH_VOCAL_POSTURE_LOCK`
- `RECOMPILE_PROMPT_WITH_HOOK_MECHANICS_LOCK`
- `ADD_NEGATIVE_STYLE_CONSTRAINTS`
- `SWAP_BASE_GENRE_CARD`
- `REBALANCE_REFERENCE_WEIGHTS`
- `MAKE_PROMPT_LESS_GENERIC`
- `SIMPLIFY_PROMPT_FOR_MINIMAX`
- `REWRITE_LYRICS_FOR_STYLE_POSTURE`
- `REGENERATE_WITH_SAME_PACKET`
- `REGENERATE_WITH_BOLD_VARIANT`

## Differentiation check

For every style packet, answer:

1. If the artist name were removed, could a knowledgeable listener still identify the lane?
2. What exact rhythm, vocal, hook, and production traits make this lane distinct?
3. Which adjacent artist is most likely to be confused with this, and what guardrail prevents that?
4. Does the track still serve the album, or is it merely a disconnected style exercise?
