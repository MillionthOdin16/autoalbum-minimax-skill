# MiniMax Parameter Decision Tree

## Model
- Use `music-2.6` for serious candidate and final generation.
- Use `music-2.6-free` only for scratch exploration when quality/cost tradeoff is acceptable.
- Use `music-cover` when preserving an approved melody/performance contour while changing style or lyrics.
- Use `music-cover-free` only for scratch cover experiments.

## Vocal vs instrumental
- Set `is_instrumental: false` for normal album tracks.
- Set `is_instrumental: true` only for intentional intros, interludes, reprises, outros, score cues, or style scouting.
- When `is_instrumental: true`, omit lyrics unless the active wrapper requires an empty string.

## Lyrics optimizer
- Default `lyrics_optimizer: false` for album work.
- Use `lyrics_optimizer: true` only for scratch ideation, baseline comparison, or emergency filler.
- Do not use lyrics optimizer for lead singles, narrative tracks, or strict artist/song fingerprints.

## Stream and output format
- Final/candidate batch renders: `stream: false`, `output_format: url`, download immediately.
- Interactive preview where supported: `stream: true`, `output_format: hex`.
- If `stream: true` and `output_format` is not `hex`, the packet fails.

## Audio setting
Use route-supported highest quality for serious renders.

```json
{
  "preview_fast": {"sample_rate": 44100, "bitrate": 128000, "format": "mp3"},
  "candidate_review": {"sample_rate": 44100, "bitrate": 256000, "format": "mp3"},
  "final_archive": {"sample_rate": 44100, "bitrate": 256000, "format": "wav"}
}
```

If the selected provider does not support WAV through the current route, use MP3 256k for candidate generation and store the limitation in `ops/parameter_audit.md`.

## Prompt and lyrics length
- Direct text-to-music prompt: max 2000 chars.
- Direct non-instrumental lyrics: 1-3500 chars.
- Cover prompt: 10-300 chars.
- Cover replacement lyrics: 10-1000 chars when using `cover_feature_id`.

## Cover mode
Use cover mode when:
- a generated take has the right melody but wrong style,
- a strong guide demo should be re-rendered,
- a deluxe/acoustic/club/radio version is desired,
- a reprise should preserve melodic identity with changed production.

Reference audio must be 6 seconds to 6 minutes, max 50 MB, common audio format. Use exactly one of `audio_url`, `audio_base64`, or `cover_feature_id`.

## Response logging
Always capture:
- trace_id or request_id,
- response status,
- audio URL or hex metadata,
- duration,
- sample rate,
- channels,
- bitrate,
- file size,
- local downloaded file path,
- prompt hash,
- lyrics hash,
- packet hash.
