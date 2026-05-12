# Delegated: Evaluate MiniMax Packet

## Task
Evaluate whether Track NN is ready for MiniMax Music 2.6 generation.

## Read
- `references/agent_training/minimax_control_cookbook.md`
- `references/agent_training/agent_anti_shortcut_checklists.md`
- `tracks/tr_NN/preproduction_brief.json`
- `tracks/tr_NN/prompt_budget_report.json`
- intent_intake.json
- references/model_profiles/minimax_music_2_6.md
- references/api/minimax_music_2_6_full_api_reference.md
- references/api/minimax_provider_capability_matrix.md
- references/schemas/generation_packet.schema.json
- project_config.json
- foundation/*.md
- planning/*.md
- tracks/tr_NN/style_card.json
- tracks/tr_NN/generation_packet.json

## Output
Write `tracks/tr_NN/minimax_eval.json`.

## Checks
- The packet must be judged against the preproduction brief, not against generic quality.
- Confirm that every important musical control is either in prompt, lyrics, metadata, or intentionally omitted.
- prompt <= 2000 chars.
- lyrics <= 3500 chars.
- all tags valid for chosen profile.
- prompt is vivid English prose.
- lyrics are not overloaded with stage directions.
- style prompt does not conflict with section plan.
- BPM/key/genre/vocal descriptions are compatible.
- track is distinct from previous and next track.
- album DNA is present.
- constraints are not overstuffed.
- the prompt gives MiniMax enough control over tension, vocal, arrangement, and hook behavior.

## JSON schema

```json
{
  "track_number": 1,
  "prompt_char_count": 0,
  "lyrics_char_count": 0,
  "valid_tags": true,
  "unsupported_tags": [],
  "prompt_vividness": 0,
  "prompt_actionability": 0,
  "vocal_identity_control": 0,
  "arrangement_control": 0,
  "tension_architecture": 0,
  "hook_generation_likelihood": 0,
  "album_fit": 0,
  "adjacent_track_contrast": 0,
  "overconstraint_risk": "low|medium|high",
  "underconstraint_risk": "low|medium|high",
  "conflicts": [],
  "required_fixes": [],
  "minimax_packet_score": 0,
  "ready_for_generation": false
}
```


## Full API validation additions

Score and report:

```json
{
  "stream_output_format_rule_ok": true,
  "instrumental_lyrics_rule_ok": true,
  "lyrics_optimizer_rule_ok": true,
  "audio_setting_supported_by_provider": true,
  "download_policy_present_for_url": true,
  "response_logging_ready": true,
  "provider_parameters_supported": true,
  "unsupported_requested_parameters": [],
  "omitted_parameters_with_reasons": []
}
```

A packet cannot be marked ready if direct-API `stream` and `output_format` conflict, if instrumental/lyrics rules fail, or if the selected provider cannot represent the chosen controls. For provider wrappers, verify the wrapper-specific output/download fields instead of requiring direct-only fields.

## Mandatory additions
The packet evaluation must read:

```text
tracks/tr_NN/prosody_review.json
tracks/tr_NN/prompt_budget_report.json
selected provider profile JSON
```

The packet fails if prosody is not approved, the prompt is above provider limit, the prompt lacks concrete musical controls, or provider-specific fields are omitted without rationale.
