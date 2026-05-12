# MiniMax Music 2.6 Full API Reference for AutoAlbum

Last verified against public MiniMax documentation: **2026-05-11**. If the provider dashboard or wrapper schema differs from this file, update the selected provider profile before exporting payloads.

## Purpose

This reference documents every MiniMax Music 2.6 generation capability AutoAlbum must preserve when creating album-generation packets. It is a working reference for skill execution, not marketing copy. Use it whenever compiling, validating, exporting, or auditing payloads.

AutoAlbum should not necessarily use every parameter on every track. It should expose and document every parameter, choose intentionally, and log the choice.

## Source priority

1. Direct MiniMax API docs for `/v1/music_generation` and `/v1/music_cover_preprocess`.
2. Official MiniMax music-generation guide.
3. Official MiniMax `minimax-music-gen` skill and prompt guide.
4. Provider wrapper schemas, only for the selected route.
5. Community notes, only as heuristics; never as source of truth for hard limits.

## Core endpoint

```http
POST https://api.minimax.io/v1/music_generation
Authorization: Bearer <MINIMAX_API_KEY>
Content-Type: application/json
```

## Model choices

| Model | Purpose | Recommended AutoAlbum use |
|---|---|---|
| `music-2.6` | Paid/recommended text-to-music model | Final candidates, lead singles, serious renders |
| `music-2.6-free` | Free text-to-music model with lower RPM | Scratch/demo exploration only |
| `music-cover` | Paid/recommended cover/re-render model | Re-render approved demos, alternate versions, acoustic/club/live versions |
| `music-cover-free` | Free cover model with lower RPM | Scratch cover experiments |

Default for a professional album: `music-2.6`.

## Text-to-music payload fields

### `model`

Required. One of:

```text
music-2.6
music-2.6-free
music-cover
music-cover-free
```

### `prompt`

A description of the music: style, mood, scenario, vocal identity, instrumentation, atmosphere, and production/tension behavior.

Hard limits:

| Mode | Requirement |
|---|---|
| `music-2.6` / `music-2.6-free`, instrumental | Required, 1–2000 chars |
| `music-2.6` / `music-2.6-free`, non-instrumental | Optional by API, but AutoAlbum requires it for quality; 0–2000 chars |
| `music-cover` / `music-cover-free` | Required, 10–300 chars |

AutoAlbum rule: always provide a high-quality prompt except in an intentional diagnostic case. Although the direct API lists the non-instrumental prompt as optional, AutoAlbum treats it as required for quality because it carries the style, arrangement, production, and vocal controls. The prompt should be vivid English prose, not a tag pile.

### `lyrics`

Song lyrics using `\n` line breaks and supported section tags.

Hard limits:

| Mode | Requirement |
|---|---|
| `music-2.6` / `music-2.6-free`, instrumental | Not required |
| `music-2.6` / `music-2.6-free`, non-instrumental | Required, 1–3500 chars |
| `music-cover` / `music-cover-free`, one-step with reference audio | Optional; if omitted, ASR extracts lyrics from reference audio; if supplied, 10–1000 chars |
| `music-cover` / `music-cover-free` with `cover_feature_id` | Required, 10–1000 chars |
| `lyrics_optimizer: true` and empty lyrics | System auto-generates lyrics from prompt |

AutoAlbum rule: for serious album songs, write and validate lyrics yourself. Use `lyrics_optimizer` only for diagnostics, scratch tracks, or fallback.

### Supported direct-API structure tags

Use only these for the direct `/v1/music_generation` route unless the selected provider profile says otherwise:

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

Do not invent tags such as `[Verse 2]`, `[Final Chorus]`, `[Drop]`, `[Breakdown]`, `[Refrain]`, `[Chorus louder]`, or `[whispered]` for this profile. If a provider route supports aliases, select that route's tag profile explicitly.

### `stream`

Boolean. Default: `false`.

Purpose: streaming output.

Rules:
- If `stream: true`, only `output_format: "hex"` is supported.
- For final album renders, default `stream: false`.
- Use streaming only for preview/interactive workflows where the selected route supports it.

### `output_format`

Enum: `url` or `hex`. Default in direct docs: `hex`.

Rules:
- `url` returns a temporary URL; download promptly because it expires after 24 hours.
- `hex` returns encoded audio data directly.
- `stream: true` requires `hex`.

AutoAlbum default:
- Use `url` for ordinary batch generation, then immediately download/archive.
- Use `hex` when streaming, when an integration requires direct bytes, or when URL handling is unreliable.

### `audio_setting`

Object controlling output configuration.

Canonical fields:

```json
{
  "sample_rate": 44100,
  "bitrate": 256000,
  "format": "mp3"
}
```

Route-dependent options may include:
- sample rate: 16000, 24000, 32000, 44100 Hz.
- bitrate: 32000, 64000, 128000, 256000 bps.
- format: `mp3`, `wav`, and in some product surfaces `pcm`.

AutoAlbum must use a provider capability matrix. Do not assume every wrapper supports every format.

Recommended profiles:

```json
{
  "preview_fast": {
    "sample_rate": 44100,
    "bitrate": 128000,
    "format": "mp3"
  },
  "candidate_review": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "final_archive": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "wav"
  }
}
```

If WAV is not supported on the active route, fall back to highest-quality MP3 and record the limitation.

### `lyrics_optimizer`

Boolean. Default: `false`. Only supported on `music-2.6` / `music-2.6-free`.

When true and lyrics are empty, MiniMax auto-generates lyrics from the prompt.

AutoAlbum policy:
- `false` for final album tracks.
- `true` only for baseline comparison, scratch idea expansion, low-stakes interludes, or diagnostics.
- Do not combine `lyrics_optimizer: true` with `is_instrumental: true`; if a provider accepts both, treat the request as invalid because the intent is contradictory.
- Never use optimizer output as final album lyrics without the full lyric/songcraft evaluation loop.

### `is_instrumental`

Boolean. Default: `false`. Only supported on `music-2.6` / `music-2.6-free`.

When true, lyrics are not required and the track should have no vocals.

AutoAlbum uses:
- intro, interlude, reprise, transition, outro, hidden track, score-like connective tissue.
- instrumental variants of vocal tracks.
- album pacing and emotional breathing room.

Rules:
- If `is_instrumental: true`, omit `lyrics` or set it empty according to provider route.
- The prompt must replace vocal instructions with instrumental focus, arrangement, texture, scene, motif, and emotional function.

## Cover-only fields

Cover fields are only used with `music-cover` or `music-cover-free`.

### `audio_url`

URL of reference audio.

Rules:
- Only one of `audio_url` or `audio_base64` must be supplied in one-step cover mode.
- Mutually exclusive with `cover_feature_id`.
- Reference audio: 6 seconds to 6 minutes; max 50 MB; common formats such as mp3, wav, flac.

### `audio_base64`

Base64-encoded reference audio.

Rules:
- Same constraints as `audio_url`.
- Use when a public URL is unavailable or a local file must be embedded.
- Avoid for very large files if URL upload/download is easier.

### `cover_feature_id`

Feature ID returned by `/v1/music_cover_preprocess`.

Rules:
- Only used with `music-cover` / `music-cover-free`.
- Mutually exclusive with `audio_url` and `audio_base64`.
- Valid for 24 hours.
- Same audio content returns the same ID.
- When supplied, `lyrics` is required and must be 10–1000 characters.

## Response fields to log

For every generation, archive raw response and extract:

```json
{
  "trace_id": "...",
  "data_status": 2,
  "audio_output_location": "url or hex archive path",
  "extra_info": {
    "music_duration": 25364,
    "music_sample_rate": 44100,
    "music_channel": 2,
    "bitrate": 256000,
    "music_size": 813651
  },
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

Do not lose traceability between audio output, prompt, lyrics, packet version, provider route, and response metadata.

## Album-quality defaults

For serious album work:

```json
{
  "model": "music-2.6",
  "lyrics_optimizer": false,
  "is_instrumental": false,
  "stream": false,
  "output_format": "url",
  "audio_profile": "candidate_review",
  "download_immediately": true
}
```

For final archive when supported:

```json
{
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "wav"
  }
}
```

For scratch exploration:

```json
{
  "model": "music-2.6-free",
  "audio_profile": "preview_fast"
}
```

For instrumentals:

```json
{
  "model": "music-2.6",
  "is_instrumental": true,
  "lyrics": ""
}
```

For one-step cover:

```json
{
  "model": "music-cover",
  "audio_url": "https://example.com/source.mp3",
  "prompt": "Sparse acoustic folk cover with intimate close vocal and brushed percussion",
  "output_format": "url"
}
```

For two-step cover:

```json
{
  "model": "music-cover",
  "cover_feature_id": "...",
  "lyrics": "[Verse]\n...",
  "prompt": "Late-night jazz lounge cover with warm saxophone and brushed drums",
  "output_format": "url"
}
```

## Parameter audit checklist

Before generation, verify:

- Model allowed for selected route.
- Prompt required/optional rule satisfied.
- Prompt length valid for selected model.
- Lyrics required/optional rule satisfied.
- Lyrics length valid for selected model.
- Tags match selected tag profile.
- `lyrics_optimizer` used only with supported model.
- `is_instrumental` used only with supported model.
- Instrumental tracks do not include lyric content.
- Cover mode includes exactly one reference input path: `audio_url`, `audio_base64`, or `cover_feature_id`.
- Cover reference audio constraints documented.
- `stream: true` uses `output_format: hex`.
- `output_format: url` has immediate download policy.
- Audio settings supported by route.
- Response metadata will be logged.
