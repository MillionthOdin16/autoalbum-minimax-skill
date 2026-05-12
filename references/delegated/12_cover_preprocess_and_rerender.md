# Delegated: Cover Preprocess and Re-Render Plan

## Task

Prepare the operational plan for a MiniMax two-step cover workflow or one-step cover generation. This file does not execute the API by itself; it creates the exact plan, payloads, and logs needed for safe execution.

## Read

- `references/api/minimax_cover_workflows.md`
- `references/api/minimax_response_and_artifact_logging.md`
- `references/schemas/cover_packet.schema.json`
- selected cover packet

## One-step workflow output

Create:

```text
covers/payloads/<cover_id>.json
covers/renders/<cover_id>_expected_path.txt
ops/parameter_audit.md update
```

## Two-step workflow output

Create:

```text
covers/preprocess_payloads/<cover_id>_preprocess.json
covers/preprocess_results/<cover_id>_preprocess_expected.json
covers/payloads/<cover_id>_generate.json
ops/parameter_audit.md update
```

## Two-step reminders

- Preprocess returns `cover_feature_id`, `formatted_lyrics`, `structure_result`, and `audio_duration`.
- `cover_feature_id` is valid for 24 hours.
- When generating with `cover_feature_id`, do not pass `audio_url` or `audio_base64`.
- When generating with `cover_feature_id`, lyrics are required and must be 10–1000 characters.

## Review

After render, require `post_generation_review.md` or a cover-specific review:

```text
covers/reviews/<cover_id>_review.md
```

Review questions:
- Did the cover preserve the useful source material?
- Did the target style actually take?
- Does it improve album fit?
- Does it create redundancy?
- Should it replace the original, sit as a reprise, become a deluxe alternate, or be discarded?
