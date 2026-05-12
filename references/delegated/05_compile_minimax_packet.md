# Delegated: Compile MiniMax Packet

## Task
Compile a MiniMax Music 2.6 generation packet for Track NN.

## Read
- `references/agent_training/minimax_control_cookbook.md`
- `references/agent_training/production_mix_mastering_primer.md`
- `tracks/tr_NN/preproduction_brief.json`
- `tracks/tr_NN/hook_lab.json`
- `tracks/tr_NN/arrangement_energy_review.json`
- intent_intake.json
- references/model_profiles/minimax_music_2_6.md
- references/api/minimax_music_2_6_full_api_reference.md
- references/api/minimax_provider_capability_matrix.md
- references/schemas/generation_packet.schema.json
- project_config.json
- foundation/*.md
- planning/*.md
- tracks/tr_NN/style_card.json
- tracks/tr_NN/lyrics_minimax.txt
- tracks/tr_NN/songcraft_eval.json
- previous and next track cards

## Output files
- tracks/tr_NN/prompt_minimax.txt
- tracks/tr_NN/generation_packet.json

## Prompt writing rules
- Compile from `preproduction_brief.json`; do not improvise the prompt from vibes.
- Include groove/drums/bass, vocal delivery, hook mechanics, production/mix space, and arrangement/tension behavior.
- English vivid prose, not comma-separated tags.
- <= 2000 characters.
- Include mood + genre/subgenre.
- Include specific vocal identity.
- Include narrative/theme of the track.
- Include scene/atmosphere.
- Include 2-4 production elements.
- Include tension architecture: what starts withheld, what builds, where chorus opens, where low end or drums enter.
- Translate album lore into audible instructions.
- Do not include unsupported structure tags in the prompt.
- Do not overload with every instrument in the world bible.

## Generation packet schema

```json
{
  "track_number": 1,
  "title": "...",
  "album_function": "...",
  "model": "music-2.6",
  "provider": "direct_minimax_api",
  "provider_profile_path": "references/api/provider_profiles/direct_minimax_api.json",
  "tag_profile": "direct_minimax_music_generation",
  "mode": "vocal",
  "is_instrumental": false,
  "lyrics_optimizer": false,
  "stream": false,
  "output_format": "url",
  "audio_profile": "candidate_review",
  "prompt": "...",
  "lyrics": "...",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "download_policy": {
    "download_immediately": true,
    "url_expiration_hours": 24,
    "archive_raw_response": true,
    "archive_audio": true
  },
  "style_card_path": "tracks/tr_01/style_card.json",
  "prompt_budget_report_path": "tracks/tr_01/prompt_budget_report.json",
  "hard_constraints": [],
  "soft_guidance": [],
  "avoid": [],
  "album_continuity": {
    "shared_dna": [],
    "track_distinction": "..."
  },
  "music_theory_plan": {
    "bpm_feel": "...",
    "key_center": "...",
    "harmonic_color": "...",
    "groove": "...",
    "section_energy_map": []
  },
  "validation": {
    "prompt_char_count": 0,
    "lyrics_char_count": 0,
    "supported_tags_only": true,
    "unsupported_tags": [],
    "instrumental_lyrics_rule_ok": true,
    "stream_output_format_rule_ok": true,
    "provider_parameters_supported": true,
    "provider_profile_id_matches_provider": true
  }
}
```


## Full API parameter requirements

Every `generation_packet.json` must explicitly set or intentionally omit, with reason logged in validation warnings when omitted:

```text
model
provider
tag_profile
mode
prompt
lyrics
lyrics_optimizer
is_instrumental
stream
output_format
audio_profile
audio_setting
download_policy
mmx_cli_args if provider is mmx_cli
```

For `direct_minimax_api`, use `output_format: "url"` for normal batch generation and set `download_policy.download_immediately: true`; use `stream: false` for final renders. Use `stream: true` only if the active provider supports streaming and then force `output_format: "hex"`. For provider wrappers such as FAL or Cloudflare, do not invent direct-only `output_format`/`stream` request fields; store equivalent download/archive policy in the packet and payload metadata.

## Mandatory inputs
Do not compile the final MiniMax packet unless these exist and pass:

```text
tracks/tr_NN/prosody_review.json
tracks/tr_NN/style_card.json
tracks/tr_NN/lyrics_working.md
selected provider profile under references/api/provider_profiles/
```

After creating `prompt_minimax.txt`, run `34_prompt_budget_and_compression.md` before approving the packet.
