# Delegated: Build Final Release Package

## Task
Create or update `<project_slug>/release_package/` as the user-facing final output.

## Read
- `<project_slug>/state.json`
- `<project_slug>/project_manifest.json`
- `<project_slug>/planning/tracklist.md`
- `<project_slug>/reviews/final_aandr_review.md`
- `<project_slug>/ops/render_log.jsonl`
- each selected track's lyrics, prompt, packet, selected render, and selected candidate record
- `references/schemas/release_metadata.schema.json`
- `references/schemas/final_tracklist.schema.json`

## Output
```text
release_package/metadata.json
release_package/final_tracklist.md
release_package/final_lyrics.md
release_package/audio/
release_package/prompts/
release_package/packets/
release_package/provenance/
release_package/quality/
release_package/credits.md
release_package/cover_direction.md
release_package/liner_notes.md
release_package/press_release.md
```

## Requirements
- Copy or reference selected audio clearly. Do not leave the user guessing which render is final.
- Copy final prompts and generation packets into `release_package/prompts/` and `release_package/packets/`.
- Copy final quality reviews into `release_package/quality/`.
- Include `render_log.final.jsonl`, `selected_candidates.json`, and `generation_manifest.json` in `release_package/provenance/`.
- Validate `metadata.json` against `release_metadata.schema.json`.
- Validate the machine-readable tracklist data if emitted as JSON; markdown `final_tracklist.md` must include sequence rationale.
- Run `30_update_project_state.md` after packaging.

## Release package addition
For release-package goals, copy or reference these into `release_package/quality/` and `release_package/provenance/`:

```text
reviews/final_audio_qc.json
reviews/final_audio_qc.md
reviews/timestamped_listening_notes.md
ops/render_log.jsonl
tracks/tr_NN/selected_candidate.json
```
