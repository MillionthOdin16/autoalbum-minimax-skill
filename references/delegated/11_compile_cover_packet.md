# Delegated: Compile MiniMax Cover Packet

## Task

Create a MiniMax `music-cover` or `music-cover-free` packet for an optional cover/re-render/alternate-version workflow.

## Read

- `references/api/minimax_cover_workflows.md`
- `references/api/minimax_music_2_6_full_api_reference.md`
- `references/schemas/cover_packet.schema.json`
- `foundation/sound_signature.md`
- `foundation/reference_translation.md`
- `planning/album_arc.md`
- source track brief, lyrics, generation packet, and post-generation review
- source audio registry entry

## Decide workflow

Choose one:

```text
one_step_url
one_step_base64
two_step_feature_id
```

Use two-step only when lyric/structure editing is needed or when preserving extracted structure matters.

## Output

Write:

```text
covers/cover_packets/<cover_id>.json
```

## Requirements

- Prompt must be 10–300 characters.
- Prompt must describe target cover style, not full album backstory.
- Exactly one of `audio_url`, `audio_base64`, or `cover_feature_id` is used according to workflow.
- If using `cover_feature_id`, lyrics are required and 10–1000 characters.
- Cover must have an album purpose: reprise, alternate single, acoustic version, club version, cinematic version, live-room version, interlude transform, or deluxe bonus.
- Cover must not create redundancy unless redundancy is the artistic point and is justified.

## Return exactly

```json
{
  "cover_id": "...",
  "source_track": "tr_NN",
  "model": "music-cover",
  "workflow": "one_step_url|one_step_base64|two_step_feature_id",
  "audio_url": "... optional ...",
  "audio_base64": "... optional ...",
  "cover_feature_id": "... optional ...",
  "prompt": "...10-300 chars...",
  "lyrics": "... optional, <=1000 chars ...",
  "lyrics_policy": "asr_extract|unchanged|modified|new_short_lyric|instrumental_reference",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "output_format": "url",
  "album_purpose": "...",
  "success_criteria": [],
  "validation": {
    "prompt_char_count": 0,
    "source_audio_constraints_checked": true,
    "mutual_exclusion_ok": true,
    "lyrics_length_ok": true,
    "album_purpose_clear": true
  }
}
```
