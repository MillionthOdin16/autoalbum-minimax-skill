# Delegated Task: Final Audio, Mastering, and Transition QC

## Objective
Perform the final critical listening and release-readiness check for selected renders. Evaluate the album as music, not as prompts.

## Read
- `<project_slug>/project_config.json`
- `<project_slug>/state.json`
- `<project_slug>/project_manifest.json`
- `<project_slug>/planning/tracklist.md`
- `<project_slug>/planning/album_energy_map.md`
- `<project_slug>/planning/transition_map.md`
- `<project_slug>/ops/render_log.jsonl`
- `<project_slug>/tracks/tr_NN/selected_candidate.json` for all tracks
- selected audio files under `<project_slug>/tracks/tr_NN/renders/selected/`
- `references/craft/final_audio_mastering_and_album_qc.md`
- `references/schemas/final_audio_qc.schema.json`
- `references/schemas/timestamped_listening_notes.schema.json`

## Process
1. Confirm selected renders exist and match release metadata.
2. Listen to every selected track individually.
3. Write timestamped notes for every material issue or standout moment.
4. Listen to the album sequence in order.
5. Evaluate transitions, gap/fade/segue needs, opener, middle, climax, and closer.
6. Identify technical issues that require regeneration, remix/remaster, or external mastering.
7. Decide whether the release package passes, fails, or passes with named risks.

## Output
Write:

```text
<project_slug>/reviews/final_audio_qc.json
<project_slug>/reviews/final_audio_qc.md
<project_slug>/reviews/timestamped_listening_notes.md
<project_slug>/release_package/quality/final_audio_qc.md
```

Update `state.json` and `project_manifest.json`.
