# Delegated: Evaluate Songcraft

## Task
Evaluate Track NN as a song before MiniMax packet compilation.

## Read
- `references/agent_training/songwriting_lyric_field_guide.md`
- `references/agent_training/quality_examples_and_counterexamples.md`
- `references/agent_training/agent_anti_shortcut_checklists.md`
- `tracks/tr_NN/hook_lab.json`
- `tracks/tr_NN/arrangement_energy_review.json`
- intent_intake.json
- foundation/*.md
- planning/*.md
- tracks/tr_NN/style_card.json
- tracks/tr_NN/lyrics_working.md
- tracks/tr_NN/lyrics_minimax.txt
- references/craft/professional_album_craft.md

## Output
Write `tracks/tr_NN/songcraft_eval.json`.

## JSON schema

```json
{
  "track_number": 1,
  "lyrics_char_count": 0,
  "valid_section_tags_for_project": true,
  "unsupported_tags": [],
  "voice_adherence": 0,
  "album_fit": 0,
  "track_distinctiveness": 0,
  "hook_contract": 0,
  "hook_memorability": 0,
  "verse_progression": 0,
  "bridge_or_contrast_function": 0,
  "singability": 0,
  "phonetic_hook_quality": 0,
  "concrete_image_ratio": 0,
  "motif_use": 0,
  "cliche_count": 0,
  "weakest_lines": [],
  "strongest_lines": [],
  "required_revisions": [],
  "songcraft_score": 0,
  "ready_for_packet_compilation": false
}
```

## Scoring guidance
The evaluator must cite concrete evidence from the lyric: hook phrase, weak lines, generic phrases, verse progression, section contrast, and style/delivery fit. Do not give high scores for emotional sincerity alone.
- 6 = competent AI demo lyric.
- 7 = good and usable but not special.
- 8 = strong songcraft, clear identity, likely worth generating.
- 9 = rare, memorable, professional-level writing.
- Never score high if the chorus is not memorable or singable.

## Required handoff
Songcraft evaluation is not complete until it identifies whether the lyric is ready for `33_prosody_scansion_topline_review.md`. A high literary score cannot override a failed hook, breath, cadence, or delivery-fit issue.
