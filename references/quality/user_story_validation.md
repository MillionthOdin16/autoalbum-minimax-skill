# User Story Validation

Use this checklist to evaluate whether AutoAlbum actually works for the way users ask for music.

## Validation table

| User story | Required capability | Current pass standard |
|---|---|---|
| Concept-only album | Infer defaults and run full pipeline | project_config + style map + foundation + packets + variants |
| Concept-only single | Avoid album bloat | one-track project with lead-single/songcraft gates |
| Specific artist/song style | Preserve references and compile detailed fingerprint | style card has strictness 4-5 + non-confusion rules |
| Broad genre style | Resolve to concrete lane | broad labels converted to subgenre/scene controls |
| Multi-style album | Cohesion plus contrast | album style map defines shared DNA and per-track deltas |
| User lyrics supplied | Preserve/revise intentionally | original text preserved and changes justified |
| Instrumental project | No lyric dependency | is_instrumental true, lyrics empty/omitted, instrumental prompt complete |
| Cover/re-render | Source-audio workflow | cover packet + source registry + valid API choice |
| Generated renders supplied | Candidate comparison | keep/regenerate/cut decision based on render evidence |
| Release package | Finalization only after selected takes | metadata, lyrics, credits, cover direction, sequence, reviews |

## Red flags
- The agent asks broad preference questions instead of making documented defaults.
- Single-track projects are forced through album-only gates.
- Full-album projects stop at lyrics without MiniMax packets.
- The style catalog produces labels instead of musical controls.
- Artist/song references lose their distinctive rhythm, vocal, hook, or production traits.
- Track style cards are created before any track role exists.
- Tracklist is frozen before hearing generated audio.
- Release package is declared complete without selected renders.

## Required final report fields
Every project QA report must include:

```text
user_story_classification
project_scope
output_goal
execution_mode
assumptions_made
style_request_summary
raw_references_preserved
artifacts_created
quality_gates_passed
open_items
next_action
```
