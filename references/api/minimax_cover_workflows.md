# MiniMax Cover and Re-Render Workflows

## Purpose

Cover mode is optional but strategically valuable. AutoAlbum should use it when an existing audio result has musical value that should be preserved while changing style, production, lyrics, or album fit.

Cover mode should not replace original song planning. It is a producer tool for alternate versions, style transfer, and controlled re-rendering.

## When to use cover mode

Use cover/re-render workflows for:

- preserving a strong melody/performance contour from a generated demo while changing production.
- acoustic, club, cinematic, live, radio, stripped, or deluxe versions.
- reprises that share recognizable material with an earlier track.
- transforming a rough guide demo into the album's sonic world.
- fixing a track whose writing is strong but whose arrangement missed the album identity.
- alternate single versions.

Do not use cover mode for:

- using cover mode without a clear creative or technical reason.
- replacing weak songwriting with style transfer.
- every track by default.
- source audio that is too long, too short, too low quality, or legally unclear.

## One-step cover workflow

Use when you have reference audio and do not need to inspect/edit extracted lyrics first.

Inputs:

```json
{
  "model": "music-cover",
  "audio_url": "https://example.com/source.mp3",
  "prompt": "Target cover style, 10-300 chars",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "output_format": "url"
}
```

Rules:
- Use exactly one of `audio_url` or `audio_base64`.
- Do not provide `cover_feature_id` in one-step mode.
- If `lyrics` is omitted, MiniMax extracts lyrics via ASR.
- If lyrics are supplied, keep them 10–1000 characters.
- Prompt is required, 10–300 characters.

## Two-step cover workflow

Use when you need more control over lyrics, structure, or source-audio interpretation.

### Step 1: Preprocess source audio

Endpoint:

```http
POST https://api.minimax.io/v1/music_cover_preprocess
```

Payload example:

```json
{
  "model": "music-cover",
  "audio_url": "https://example.com/original-song.mp3"
}
```

Capture:

```json
{
  "cover_feature_id": "...",
  "formatted_lyrics": "[Verse]\n...",
  "structure_result": "...",
  "audio_duration": 123.4
}
```

Important rules:
- Preprocess is used to extract audio features and structured lyrics.
- `cover_feature_id` is valid for 24 hours.
- Same audio content returns the same feature ID.
- Store preprocess response immediately.

### Step 2: Generate cover from feature ID

Payload example:

```json
{
  "model": "music-cover",
  "cover_feature_id": "...",
  "lyrics": "[Verse]\nModified lyrics here\n\n[Chorus]\nModified chorus here",
  "prompt": "Jazz lounge cover with warm saxophone and brushed drums",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "output_format": "url"
}
```

Rules:
- Do not pass `audio_url` or `audio_base64` when using `cover_feature_id`.
- Lyrics are required with `cover_feature_id`, 10–1000 characters.
- Prompt is required, 10–300 characters.

## Cover prompt style

Cover prompts must be shorter than ordinary text-to-music prompts. They should describe target style only, not a full album essay.

Good:

```text
Sparse acoustic folk cover with intimate close vocal, fingerpicked guitar, warm room tone, and restrained brushed percussion.
```

Good:

```text
Late-night jazz lounge version with smoky baritone vocal, upright bass, brushed drums, and warm saxophone lines.
```

Bad:

```text
Make it better and more emotional, also like our album world with neon rain memories and several genre references and a long backstory...
```

## Cover packet artifact

Every cover attempt gets a cover packet:

```text
covers/cover_packets/tr_05_acoustic_reprise.json
```

It must include:
- source audio identity.
- source ownership/clearance note.
- workflow: one-step or two-step.
- model: `music-cover` or `music-cover-free`.
- target cover prompt.
- lyrics policy: ASR, unchanged, modified, or new short lyric.
- audio settings.
- output format.
- expected purpose in album.
- success criteria.

## Quality criteria for covers

A cover/re-render succeeds only if:

- it preserves the intended useful musical material from the source.
- it improves album fit.
- it does not sound like a novelty style swap.
- it has a clear role in the sequence.
- it does not create redundancy with the original version.
- it passes post-generation review.

## Album use cases

### Acoustic single version

Purpose: expose lyric and topline; useful for release extras.

### Club version

Purpose: increase energy and replay utility without changing emotional core.

### Cinematic reprise

Purpose: callback in final act of album; should transform the meaning of an earlier hook.

### Live-room version

Purpose: make the album breathe and add humanized contrast.

### Interlude transformation

Purpose: turn a chorus/motif into a short instrumental connective tissue.
