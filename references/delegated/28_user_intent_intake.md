# Delegated: User Intent Intake

## Task
Classify the user's request before project configuration.

## Read
- user request
- any supplied lyrics/audio/prompts/files
- references/architecture/user_story_operating_flows.md
- references/architecture/project_scope_modes.md
- references/architecture/autonomy_and_interaction_modes.md

## Output
Write `intent_intake.json`.

## Schema

```json
{
  "user_story_classification": "concept_only_album|concept_only_single|specific_style_album|specific_style_track|multi_style_album|user_lyrics_supplied|render_review|cover_or_rerender|release_package|revision",
  "project_scope": "single_track|lead_single|EP|mixtape|album|concept_album|beat_tape|instrumental_score|cover_or_rerender|revision_of_existing_work",
  "output_goal": "minimax_ready_packets|generated_candidates|selected_album_sequence|release_package|critique_or_regeneration_brief",
  "execution_mode": "autonomous_full_pipeline|collaborative_checkpoints|packet_only|render_review_only|release_package_only",
  "raw_user_concept": "...",
  "raw_style_request": "...",
  "reference_anchors": [],
  "supplied_materials": [],
  "assumptions_to_make": [],
  "clarifying_question_required": false,
  "clarifying_question": null,
  "reason": "..."
}
```

## Rules
- Default to autonomous execution unless the user asks for collaboration.
- A vague concept is not a blocker; infer and document.
- Ask at most one clarifying question, only if the answer would materially change the result.
- Preserve every named artist, song, producer, album, era, region, and scene reference.
- Do not convert a single-track request into an album request.
- Do not declare a full album complete if only packets exist.

## Intake additions
When the user asks for professional-quality output, default `quality_mode` to `release_grade` and `target_quality_bar` to `professional_major_release`. If the user only asks for prompt packets, still require prosody and prompt-budget gates, but final audio QC is only required after renders exist.
