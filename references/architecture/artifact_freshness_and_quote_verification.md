
# Artifact Freshness and Quote Verification

Every evaluative artifact must identify the exact artifact it reviewed.

## Required review metadata

```json
{
  "evaluated_artifact_path": "tracks/tr_01/lyrics_minimax.txt",
  "evaluated_artifact_hash": "sha256:...",
  "review_created_at": "2026-05-12T00:00:00Z",
  "quoted_lines_verified": true
}
```

## Rule

If the evaluated artifact changes, the review is stale and cannot support a gate. If the review quotes a lyric/prompt line, the quote must be present in the current evaluated artifact. Hallucinated or cached quotes fail the review.

Use:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py hash-artifacts <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-freshness <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-quotes <project_slug>
```
