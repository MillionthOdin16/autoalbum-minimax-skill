# Delegated: A&R Final Album Review

## Task
Perform final professional A&R review before release package assembly.

## Read
- intent_intake.json
- project_config.json
- `release_package/final_tracklist.md` if present
- `planning/album_arc.md`
- `planning/album_energy_map.md`
- `style_catalog_outputs/album_style_map.md`
- all `tracks/tr_NN/style_card.json`
- all `tracks/tr_NN/post_generation_review.md`
- all selected render comparison outputs
- `references/craft/pro_album_a_and_r_standards.md`

## Required outputs
Write `reviews/final_aandr_review.md` with:

1. Album thesis assessment.
2. First-three-tracks promise assessment.
3. Track-by-track necessity table.
4. Weakest-track diagnosis.
5. Sequence and pacing notes.
6. Style cohesion vs contrast assessment.
7. Hook/replay distribution.
8. Emotional arc and closer assessment.
9. Cut/regenerate/resequence recommendations.
10. Release readiness decision.

## Release readiness
Return one of:
- READY_FOR_RELEASE_PACKAGE
- READY_AFTER_MINOR_RESEQUENCE
- NEEDS_REGENERATIONS
- NEEDS_FOUNDATION_REVISION
- CUT_OR_REPLACE_WEAK_TRACKS

The album cannot pass if more than one track feels interchangeable or if the closer does not earn its position.


## Scope-aware rule
Judge the project against its declared output_goal. A packet-only project can pass as generation-ready but cannot pass as release-ready. A single-track project should be reviewed as a single/track, not as an album.

## Final-release requirement
For generated-audio or release-package goals, the A&R review must incorporate `references/delegated/35_final_audio_mastering_and_transition_qc.md` and may not declare the album release-ready without selected audio, timestamped listening notes, transition review, and provenance.
