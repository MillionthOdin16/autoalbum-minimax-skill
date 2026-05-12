# Artifact Path Standard

## Canonical root
All project artifacts are relative to `<project_slug>/`.

## Root files
```text
project_manifest.json      # index of all important artifacts and their current status
state.json                 # machine-readable project state and next actions
intent_intake.json          # user request classification and assumptions
project_config.json         # validated project settings
seed.txt                    # user seed / normalized seed
source_notes.md             # notes on user-provided materials, references, and research
results.tsv                 # optional flat score/action ledger for quick inspection
```

## Style artifacts
```text
style_catalog_outputs/style_selection.json
style_catalog_outputs/album_style_map.md
style_catalog_outputs/requested_reference_fingerprints.md
style_catalog_outputs/style_fidelity_report.md
```

## Track artifacts
For every track `tr_NN`:

```text
tracks/tr_NN/brief.md
tracks/tr_NN/style_card.json
tracks/tr_NN/lyrics_working.md
tracks/tr_NN/lyrics_minimax.txt
tracks/tr_NN/prompt_minimax.txt
tracks/tr_NN/generation_packet.json
tracks/tr_NN/minimax_eval.json
tracks/tr_NN/versions/
tracks/tr_NN/variants/
tracks/tr_NN/renders/raw/
tracks/tr_NN/renders/selected/
tracks/tr_NN/renders/rejected/
tracks/tr_NN/candidate_comparison.json
tracks/tr_NN/selected_candidate.json
tracks/tr_NN/post_generation_review.md
tracks/tr_NN/regeneration_brief.md
tracks/tr_NN/approved_pending_generation.md
```

## Variant rule
Every file in `tracks/tr_NN/variants/` must be a complete valid `generation_packet.schema.json` object, not a patch or delta.

## Versioning rule
Current approved files live at the track root. Superseded or experimental versions live under `tracks/tr_NN/versions/`.

Recommended names:

```text
lyrics_v01.md
lyrics_v02.md
prompt_v01.txt
prompt_v02.txt
packet_v01.json
packet_v02.json
```

## Render rule
Never overwrite render files. Use:

```text
tracks/tr_NN/renders/raw/tr_NN_<variant>_take_XX.<ext>
tracks/tr_NN/renders/selected/tr_NN_selected.<ext>
tracks/tr_NN/renders/rejected/tr_NN_<variant>_take_XX.reject.json
```

## Payload rule
Store batch payloads and per-render payloads:

```text
generation/api_payloads.jsonl
generation/payloads/tr_NN_<variant>_take_XX.json
```

## Release package rule
The final user-facing output must be self-contained or explicitly linked through provenance:

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
