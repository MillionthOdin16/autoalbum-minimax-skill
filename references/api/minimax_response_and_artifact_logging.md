# MiniMax Response and Artifact Logging

## Purpose

Professional album generation requires reproducibility. Every rendered audio file must be traceable to the exact generation packet, payload, provider route, response, prompt, lyrics, and selected candidate version.

## Required directories

```text
ops/
  render_log.jsonl
  response_archive/
  download_manifest.json
  parameter_audit.md

tracks/tr_NN/renders/
  raw/
  selected/
  rejected/
```

## Render log schema

Every generation attempt appends one JSON line to `ops/render_log.jsonl`.

```json
{
  "render_id": "tr_03_B_hook_forward_take_02",
  "track_number": 3,
  "variant": "B_hook_forward",
  "take": 2,
  "timestamp_utc": "2026-05-11T18:00:00Z",
  "provider": "direct_minimax_api",
  "model": "music-2.6",
  "mode": "vocal",
  "packet_path": "tracks/tr_03/variants/B_hook_forward.json",
  "payload_path": "generation/payloads/tr_03_B_take_02.json",
  "response_path": "ops/response_archive/tr_03_B_take_02.response.json",
  "prompt_hash": "sha256:...",
  "lyrics_hash": "sha256:...",
  "audio_path": "tracks/tr_03/renders/raw/tr_03_B_take_02.mp3",
  "trace_id": "...",
  "status": 2,
  "base_status_code": 0,
  "base_status_msg": "success",
  "duration_ms": 25364,
  "sample_rate": 44100,
  "channels": 2,
  "bitrate": 256000,
  "size_bytes": 813651,
  "selected": false,
  "review_path": "tracks/tr_03/post_generation_review.md"
}
```

## Download manifest

When `output_format: url`, the URL expires. Download immediately and write:

```json
{
  "source_url_expiration_hours": 24,
  "downloaded_at_utc": "2026-05-11T18:05:00Z",
  "local_path": "tracks/tr_03/renders/raw/tr_03_B_take_02.mp3",
  "sha256": "...",
  "bytes": 813651,
  "content_type": "audio/mpeg"
}
```

## Raw response archive

Save exact raw response JSON even when you parse it. This allows future debugging of failed renders, provider changes, and candidate provenance.

## Candidate selection log

When a candidate is selected or rejected, update:

```text
tracks/tr_NN/post_generation_review.md
tracks/tr_NN/selected_candidate.json
```

Selection record:

```json
{
  "selected_render_id": "tr_03_B_hook_forward_take_02",
  "reason": "Best chorus lift and vocal identity; minor artifact at outro accepted",
  "rejected_render_ids": [
    {"id": "tr_03_A_take_01", "reason": "Too generic, weak low end"},
    {"id": "tr_03_C_take_01", "reason": "Bold but off-album"}
  ],
  "next_action": "KEEP"
}
```

## Failure logging

If generation fails, log:

```json
{
  "render_id": "...",
  "failed": true,
  "error_type": "provider_error|validation_error|download_error|timeout|unknown",
  "error_message": "...",
  "payload_path": "...",
  "retry_policy": "same_payload|simplify_prompt|change_output_format|manual_review"
}
```

## Naming conventions

```text
tr_01_A_on_brief_take_01.mp3
tr_01_B_hook_forward_take_01.mp3
tr_01_C_bold_take_01.mp3
tr_01_selected.mp3
```

Never overwrite original candidates.
