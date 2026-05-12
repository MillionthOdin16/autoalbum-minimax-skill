# State and Provenance

## Purpose
`state.json` is the single source of truth for pipeline progress. `project_manifest.json` is the index of artifacts. Operational logs such as `ops/render_log.jsonl` preserve the exact history of rendered candidates.

## State principles
- Update state after every phase and after every material artifact change.
- State must point to current approved artifacts, not every old draft.
- Historical versions belong in `versions/` and render logs.
- State must make the next action obvious.
- If a stage fails, record the blocking issue and recommended fix.

## Provenance principles
Every render must be traceable to:
- track number
- variant id
- take number
- exact generation packet
- exact prompt
- exact lyrics
- exact API payload
- MiniMax response metadata
- local audio path
- review decision

## Completion levels
A project may be complete at different output goals:

```text
packet_ready              # all selected tracks have approved MiniMax packets
candidate_generated       # candidate renders exist and are logged
sequence_selected         # final sequence and selected renders exist
release_packaged          # release package exists with metadata, audio, provenance, reviews
```

Never report a project as release-ready when it is only packet-ready.
