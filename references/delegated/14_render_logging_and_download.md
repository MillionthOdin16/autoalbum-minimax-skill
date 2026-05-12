# Delegated: Render Logging and Download

## Task

Define the exact artifact logging and download procedure for every MiniMax render. This stage protects reproducibility and prevents lost URL outputs.

## Read

- `references/api/minimax_response_and_artifact_logging.md`
- `references/schemas/render_log.schema.json`
- exported payloads
- raw provider responses

## Required behavior

For every render:

1. Assign a stable `render_id`.
2. Save exact payload JSON.
3. Save exact raw response JSON.
4. Extract `trace_id`, `data.status`, `extra_info`, and `base_resp` if present.
5. If response uses URL output, download immediately and compute SHA-256.
6. If response uses hex output, decode to audio file and compute SHA-256.
7. Append one JSON line to `ops/render_log.jsonl`.
8. Update `ops/download_manifest.json`.
9. Link render to post-generation review.

## Naming

```text
tr_01_A_on_brief_take_01.mp3
tr_01_B_hook_forward_take_01.mp3
tr_01_C_bold_take_01.mp3
tr_01_selected.mp3
```

## Never overwrite

Never overwrite a render, payload, or raw response. If regenerating, increment `take`.

## Failure policy

If render fails, still log:

```json
{
  "render_id": "...",
  "failed": true,
  "error_type": "validation_error|provider_error|download_error|timeout|unknown",
  "error_message": "...",
  "next_action": "same_payload|simplify_prompt|change_output_format|manual_review"
}
```
