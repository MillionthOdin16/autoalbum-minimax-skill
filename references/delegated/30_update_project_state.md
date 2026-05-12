# Delegated: Update Project State and Manifest

## Task
Update `<project_slug>/state.json` and `<project_slug>/project_manifest.json` after each material pipeline action.

## Read
- `<project_slug>/project_config.json`
- `<project_slug>/state.json` if it exists
- `<project_slug>/project_manifest.json` if it exists
- newly created or modified artifact paths
- relevant evaluation outputs
- `references/schemas/state.schema.json`
- `references/schemas/project_manifest.schema.json`
- `references/architecture/state_and_provenance.md`
- `references/architecture/artifact_path_standard.md`

## Requirements
1. Validate state against `state.schema.json`.
2. Validate manifest against `project_manifest.schema.json`.
3. Record the current phase, overall status, blocking issues, and next actions.
4. For every track, update current paths, scores, variant status, render status, and decision.
5. Do not delete history. Append a concise event to `history`.
6. Do not mark a track `packet_ready` until all packet gates pass.
7. Do not mark a project `release_packaged` unless the release package contains metadata, selected audio or explicit packet-only status, provenance, and final review.

## State event format
Append one object to `history`:

```json
{
  "timestamp": "ISO-8601",
  "phase": "packet_compilation",
  "action": "compiled_generation_packet",
  "artifact_paths": ["tracks/tr_01/generation_packet.json"],
  "decision": "approved_for_packet_evaluation",
  "notes": "Prompt and lyrics within MiniMax limits."
}
```

## Manifest artifact entry format
```json
{
  "artifact_id": "tr_01_generation_packet_current",
  "path": "tracks/tr_01/generation_packet.json",
  "category": "generation_packet",
  "track_number": 1,
  "variant_id": null,
  "version": "current",
  "status": "approved",
  "schema": "references/schemas/generation_packet.schema.json",
  "notes": "Current approved packet for Track 01."
}
```

## Output
Write updated:

```text
<project_slug>/state.json
<project_slug>/project_manifest.json
```
