# MiniMax Music 2.6 Model Profile

## Source status

This profile merges the direct MiniMax Music Generation API docs, MiniMax's official prompt guide/skill references, and observed provider/community notes. If direct API docs and third-party wrappers disagree, prefer the provider actually being called.

## Direct API default

```json
{
  "model": "music-2.6",
  "lyrics_optimizer": false,
  "is_instrumental": false,
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  }
}
```

Use WAV for archive/final exports if the chosen route exposes WAV. Use MP3 for preview and fast iteration.

## Length limits

- `prompt`: maximum 2000 characters.
- `lyrics`: 1-3500 characters for non-instrumental tracks.
- Instrumental mode: `lyrics` not required; `prompt` required.
- Lyrics optimizer: only for baseline/diagnostic/fallback, not for serious album lyrics, because AutoAlbum is responsible for lyrics.

## Canonical tag profile: `direct_minimax_music_generation`

Use these tags for `/v1/music_generation` unless the caller selects another provider profile:

```text
[Intro]
[Verse]
[Pre Chorus]
[Chorus]
[Interlude]
[Bridge]
[Outro]
[Post Chorus]
[Transition]
[Break]
[Hook]
[Build Up]
[Inst]
[Solo]
```

## Alternate tag profiles

Some MiniMax-adjacent routes and lyrics-generation docs expose aliases such as `[Pre-Chorus]`, `[Build-up]`, `[Instrumental]`, `[Breakdown]`, and `[Drop]`. Do not mix profiles in a single album. If using a wrapper route, validate against that route's schema.

## Strict lyrics rules

- Tags must appear alone on their own lines.
- Do not use `[Verse 2]`, `[Final Chorus]`, `[Chorus louder]`, `[whispered]`, or custom section labels.
- Do not put parenthetical stage directions inside lyrics if they might be sung.
- Use blank lines between sections for readability and pause cues.
- Put performance, energy, vocal, arrangement, and mix instructions in the prompt, not in the lyrics field.

## Prompt rules

MiniMax performs best when the prompt is a vivid English creative brief, not a comma-separated tag pile.

Recommended prompt shape:

```text
A [mood/emotion] [BPM optional] [genre/subgenre] song.
Vocals: [specific vocal identity and delivery].
The song is about [narrative/theme].
The atmosphere feels like [scene/image/world].
Production centers on [2-4 key instruments/textures] with [energy/tension behavior].
```

Best practices:
- English prompts by default.
- Use 2-4 decisive production details, not an overloaded inventory.
- Describe vocals as a character, not as "male vocal" or "female vocal".
- Translate artist references into attributes.
- Use BPM/key when they matter, but avoid false precision if the genre/track does not require it.
- Use tension architecture: what is withheld, what builds, where the low end enters, where the chorus opens.

## MiniMax strengths to exploit

- Full vocal tracks and instrumentals from lyrics + style prompt.
- Song structure control via tags.
- Good prompt-following when prompt is clear and not overloaded.
- Improved low-end/drums in 2.6.
- Stronger dramatic build/tension direction than earlier models.
- Fast enough iteration to justify multiple candidates.

## Known risks to defend against

- Generic lyrics if lyrics optimizer is used as the main writer.
- Overloaded prompts that average many unrelated instructions.
- Unsupported tags or parenthetical stage directions becoming sung text.
- Tracks becoming samey if album DNA is not paired with track-level contrast.
- Synthetic vocal artifacts, especially on longer tracks or dense English lyric passages.
- Weak choruses when lyrics are literary but not singable.

## Recommended payload schema

```json
{
  "model": "music-2.6",
  "prompt": "... <= 2000 chars ...",
  "lyrics": "... <= 3500 chars ...",
  "lyrics_optimizer": false,
  "is_instrumental": false,
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  }
}
```


## Full API capability coverage

AutoAlbum treats this model profile as the quick-start profile only. For complete behavior, read:

```text
references/api/minimax_music_2_6_full_api_reference.md
references/api/minimax_cover_workflows.md
references/api/minimax_provider_capability_matrix.md
references/api/minimax_response_and_artifact_logging.md
references/api/minimax_cli_reference.md
```

Tracked direct API parameters:

```text
model
prompt
lyrics
stream
output_format
audio_setting.sample_rate
audio_setting.bitrate
audio_setting.format
lyrics_optimizer
is_instrumental
audio_url
audio_base64
cover_feature_id
```

Required operational metadata:

```text
provider
route
model tier
output mode
payload path
response path
trace_id
extra_info
local audio path
prompt hash
lyrics hash
candidate decision
```

## Cover mode summary

Cover mode uses `music-cover` or `music-cover-free` and is optional for AutoAlbum. Use it for controlled re-renders, alternate versions, reprises, and style-transfer variants. One-step cover passes `audio_url` or `audio_base64` directly. Two-step cover preprocesses source audio to obtain `cover_feature_id`, `formatted_lyrics`, `structure_result`, and `audio_duration`, then generates from `cover_feature_id` plus optional/modified lyrics.

Cover prompt length is much shorter than ordinary text-to-music: 10–300 characters. Source audio must be 6 seconds to 6 minutes and at most 50 MB. `cover_feature_id` is valid for 24 hours.

## Provider-profile rule
This model profile gives general MiniMax Music 2.6 behavior. Actual payload export must select a provider-specific profile from `references/api/provider_profiles/` because direct API, CLI, and third-party wrappers can expose slightly different controls. The generation packet must record `provider_profile_path`.
