# Delegated: Select Audio Profile

## Task

Choose the correct output-quality profile for a generation attempt.

## Inputs

- selected provider.
- selected model.
- generation purpose: scratch, candidate, final, cover, interlude.
- provider capability matrix.
- user quality/cost preference.

## Profiles

### `preview_fast`

Use for rough exploration and low-stakes idea checking.

```json
{
  "sample_rate": 44100,
  "bitrate": 128000,
  "format": "mp3"
}
```

### `candidate_review`

Default for serious candidate generation.

```json
{
  "sample_rate": 44100,
  "bitrate": 256000,
  "format": "mp3"
}
```

### `final_archive`

Use for final selected tracks when route supports it.

```json
{
  "sample_rate": 44100,
  "bitrate": 256000,
  "format": "wav"
}
```

If WAV is unsupported by the selected provider route, use highest-quality MP3 and write a downgrade notice to `ops/parameter_audit.md`.

## Output

Return:

```json
{
  "audio_profile": "candidate_review",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "downgraded": false,
  "reason": "..."
}
```
