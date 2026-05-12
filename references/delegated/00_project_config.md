# Delegated: Project Configuration and Project Root

## Task
Create `<project_slug>/project_config.json` and the top-level project folder before any creative drafting. Validate against `references/schemas/project_config.schema.json`.

## Output schema

```json
{
  "project_name": "...",
  "project_slug": "filesystem-safe-project-name",
  "project_root": "filesystem-safe-project-name/",
  "project_scope": "single_track|lead_single|EP|mixtape|album|concept_album|beat_tape|instrumental_score|cover_or_rerender|revision_of_existing_work",
  "execution_mode": "autonomous_full_pipeline|collaborative_checkpoints|packet_only|render_review_only|release_package_only",
  "output_goal": "minimax_ready_packets|generated_candidates|selected_album_sequence|release_package",
  "album_title_working": "...",
  "album_type": "single_track|narrative_concept_album|emotional_arc_album|persona_album|genre_world_album|EP|mixtape|beat_tape|instrumental_score",
  "track_count": 10,
  "target_model": "music-2.6",
  "target_provider": "direct_minimax_api|mmx_cli|replicate|fal|runware|other",
  "tag_profile": "direct_minimax_music_generation",
  "lyric_language": "English",
  "prompt_language": "English",
  "audio_format_preview": "mp3",
  "audio_format_archive": "wav_if_available",
  "sample_rate": 44100,
  "bitrate": 256000,
  "creative_risk": "medium|high|very_high",
  "appeal_target": "niche_classic|broad_crossover|art_album|club_play|sync_ready",
  "reference_policy": "preserve requested references and convert them into explicit musical, vocal, lyrical, arrangement, and production controls",
  "lyrics_optimizer_policy": "disabled_except_diagnostic_baseline",
  "checkpoint_policy": "autonomous_by_default; ask only when a missing decision would materially change the project",
  "assumptions_to_document": [],
  "user_story": "..."
}
```

## Requirements
- Infer project scope from the user request. A user who asks for “a track” should not be forced into an album pipeline; a user who asks for “an album” should not stop at a single-song workflow.
- Choose an album mode appropriate to the seed. Do not force a narrative cast if the seed is better as an emotional arc or genre-world album.
- Specify exact provider/tag profile.
- Define the quality target in plain language: what kind of record would make this a success?


## Autonomous defaults
If the user gives only a concept, choose sensible defaults and document them. Do not stall the pipeline for avoidable preference questions.

Default assumptions when absent:
- album_type: emotional_arc_album for conceptual/emotional seeds; genre_world_album for style-first seeds; single_track for one-song requests.
- track_count: 1 for single track, 5 for EP, 10 for album, 12 for concept album unless user specifies otherwise.
- target_provider: direct_minimax_api unless another route is specified.
- execution_mode: autonomous_full_pipeline for creation requests, packet_only when user only wants prompts/packets, render_review_only when audio is supplied.
- prompt_language: English for MiniMax style prompts unless user explicitly asks otherwise.


## Project root naming requirements
- Derive `project_name` from the user's supplied title when available; otherwise create a strong working title from the concept.
- Derive `project_slug` from `project_name`: lowercase, ASCII where possible, hyphen-separated, no spaces, no punctuation except hyphen.
- `project_root` must equal `<project_slug>/` unless the user explicitly supplies a path.
- All artifacts for this project must live inside `project_root`.
- Create `project_manifest.json`, `state.json`, and `source_notes.md` immediately after creating `project_config.json`.

## Initial files to create
```text
<project_slug>/
  project_manifest.json
  state.json
  intent_intake.json
  project_config.json
  seed.txt
  source_notes.md
```

## Initial state update
After writing the config, run `references/delegated/30_update_project_state.md` and record:
- project root created
- scope and output goal
- assumptions
- next phase
- blocking issues, if any

## Required configuration fields
The project configuration must include:

```json
{
  "provider_profile_path": "references/api/provider_profiles/direct_minimax_api.json",
  "quality_mode": "release_grade",
  "target_quality_bar": "professional_major_release",
  "require_prosody_gate": true,
  "require_prompt_budget_gate": true,
  "require_final_audio_qc_for_release": true
}
```

Select a different provider profile only when the chosen route is not the direct MiniMax API. Do not export payloads without a provider profile.
