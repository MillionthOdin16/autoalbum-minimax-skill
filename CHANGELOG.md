# Changelog

## v24 — Production Test Ready

- Added artifact hash/freshness verification.
- Added quote verification for lyric/prompt reviews to prevent hallucinated stale critiques.
- Added scope-aware line-polish gate and independent verifier reviews.
- Added style catalog grounding verification.
- Added tournament consistency validation.
- Added prompt linting for MiniMax readiness.
- Required complete renderable variant packets.
- Required provider-ready payload export for MiniMax-ready output goals.
- Added state reconciliation from actual artifacts.
- Added score-cap rules for objective failures.
- Hardened completion fit with adversarial completion audit and verifier review.



Additional v24 hardening after Publix Deli output review:

- Fixed a controller contradiction: `minimax_ready_packets` now requires `payload_export` instead of skipping it.
- Added `preflight` command for one-shot production-test readiness validation.
- Added `verify-payloads` and `verify-state` commands.
- Changed `advance --require-gate` to use the same content validators as `gate`, not existence-only checks.
- Completion gates now run full content validation, including schemas, freshness, quotes, style, tournaments, variants, payloads, prompt lint, and state consistency.
- Strengthened quote verification so important review files without evaluated artifact metadata fail instead of being silently ignored.
- Made line-polish mandatory for vocal MiniMax-ready output goals.
- Updated active docs so routine stage validation stays lightweight while `preflight` / `validate --deep` are used for completion readiness.

## v22 — Deep consistency hardened

- Corrected controller routing so all output goals proceed to `completion_fit`; later phases are skipped by applicability instead of dropping the final completion check.
- Updated `advance --require-gate` and `status` to treat skipped phases as pass-through rather than false failures.
- Removed an obsolete `listener_panel` phase override from controller applicability; listener panel remains part of `post_render_review`, not a standalone controller phase.
- Added `style_strict` as an explicit quality mode.
- Updated controller JSON version labels and removed generated `__pycache__` artifacts from the package.
- Clarified conditional gate semantics and completion-oriented routing in architecture docs.
- Output-goal applicability now has final precedence over quality-mode escalation, preventing packet-only projects from requiring post-render/release phases.
- Sequential advancement is now enforced by default; non-sequential jumps require `--allow-jump`.


## v20 — Streamlined agent-enforced workflow

- Pruned superseded versioned references, historical audits, generated critic comments, inventories, and cache artifacts.
- Replaced active v-numbered control filenames with stable unversioned names.
- Shortened `SKILL.md` to a focused activation contract.
- Added `file_purpose_index.md` and a pruning/organization audit.
- Updated `autoalbum_guard.py` to use stable controller filenames and added a `route` command.
- Preserved all active stage instructions, schemas, style catalogs, MiniMax provider docs, craft guidance, and quality gates.


# v16 — Quality-loop enhanced AutoNovel transfer

Implemented the highest-value AutoNovel mechanisms that improve AutoAlbum output quality and pipeline reliability without forcing identical architecture. Added album canon, propagation debts, unified evaluation, adversarial song/prompt editing, patch application, listener panel, post-audio planning rebuild, and plateau-aware revision-cycle management. Updated active reference maps, phase gates, readiness gates, and schemas.

New active files include:

- `references/architecture/autonovel_quality_mechanisms_for_autoalbum.md`
- `references/architecture/quality_loop_controller.md`
- `references/architecture/propagation_and_debt_rules.md`
- `references/craft/adversarial_song_editing.md`
- `references/craft/listener_panel_method.md`
- `references/delegated/41_build_album_canon.md` through `47_revision_cycle_manager.md`
- `references/schemas/album_canon.schema.json`
- `references/schemas/propagation_debt.schema.json`
- `references/schemas/unified_eval.schema.json`
- `references/schemas/adversarial_edit.schema.json`
- `references/schemas/edit_patch.schema.json`
- `references/schemas/listener_panel.schema.json`
- `references/schemas/post_audio_rebuild.schema.json`
- `references/schemas/revision_cycle.schema.json`

# Changelog

## v15.0 — Progressive Disclosure and Skill Best Practices Audit

- Replaced the overloaded root `SKILL.md` with a concise activation contract.
- Added `references/active/CURRENT.md` as the current active-map entry point.
- Added progressive-disclosure operating model.
- Added stage reference map that names exact references, outputs, and pass criteria per phase.
- Added v15 phase gate matrix.
- Added skill best-practices audit and progressive-disclosure review.
- Preserved v14 full skill file under `removed historical SKILL archive` for history.
- Clarified that historical versioned docs do not override v15 active rules unless explicitly named.


## v14.0 — Non-Expert Agent Musical Expertise Complete

- Added embedded agent-training reference system so the skill no longer assumes musical expertise.
- Added `references/agent_training/` with primers, manuals, examples, anti-shortcut checklists, and final album judging rubric.
- Added mandatory hook/title/chorus lab before full lyric drafting.
- Added arrangement, form, and energy review gate before MiniMax packet compilation.
- Added track preproduction brief to bridge songcraft, style, arrangement, and prompt compilation.
- Added knowledge-dependency check task for high-rigor/release-grade stages.
- Added quality counterexample review task to catch generic-but-formally-complete artifacts.
- Added schemas for knowledge checks, hook lab, arrangement review, and preproduction brief.
- Updated SKILL.md, active reference index, phase gate matrix, and delegated prompts to require embedded training references.
- Updated generation packet/state/config schemas with v14 training/preproduction fields.


## v12.0 — Skill Self-Audit and Optional Critic Mode

- Reframed the v11 critic system as optional/checkpoint-based rather than mandatory after every material stage.
- Added `references/quality/pruning_and_organization_audit.md`, a direct critical analysis of the skill itself.
- Added recommended future additions for prosody/scansion and MiniMax prompt budgeting.
- Updated `SKILL.md` and critic protocol language to reduce document-factory risk while preserving high-rigor critic review when useful.

# Changelog

## v10.0-completion-hardened-state-provenance-2026-05-11
- Added neutral active reference filenames so the current workflow no longer depends on stale v7/v8 document names.
- Added `references/prompt_guide.md` shim for internal reference consistency.
- Added `references/architecture/results_tsv_spec.md`.
- Added schemas for `candidate_comparison.json`, `selected_candidate.json`, `approved_pending_generation.md` logical contents, and `results.tsv`.
- Updated SKILL references to include final completion/provenance schemas.
- Preserved older versioned files only as historical compatibility references.

## v9.0 — Project root, state, provenance, and release organization refinement
- Replaced generic `autoalbum-full/` active-work directory with `<project_slug>/` top-level project folders.
- Added canonical project-root organization and artifact-path standards.
- Added `state.schema.json`, `project_manifest.schema.json`, `release_metadata.schema.json`, and `final_tracklist.schema.json`.
- Added `30_update_project_state.md` for resumable state and manifest maintenance.
- Added `31_build_release_package.md` for self-contained final output packaging.
- Standardized renders into `raw/`, `selected/`, and `rejected/` directories.
- Standardized API payload paths under `generation/payloads/` plus `generation/api_payloads.jsonl`.
- Clarified that variant files must be complete generation packets, not deltas.
- Added prompt/lyrics/packet versioning under each track's `versions/` folder.
- Added release-package subfolders for audio, prompts, packets, provenance, and quality reviews.

# Changelog

## v8.0-user-story-validated-autonomous-workflows-2026-05-11

- Added user-story operating flows for concept-only albums, singles, artist/song style requests, user-supplied lyrics, generated-render review, cover/re-render workflows, current-trend projects, and release packaging.
- Added intent intake, project scope modes, autonomy/interaction modes, and agent execution playbook.
- Fixed a workflow circularity: tracklist planning now runs as skeleton plan → per-track style cards → refined tracklist.
- Added user-story fit validation and fragility register.
- Added `project_config.schema.json`.
- Updated project configuration to distinguish `project_scope`, `execution_mode`, and `output_goal`.
- Clarified packet-only vs render-ready vs release-ready completion states.
- Removed stale restrictive reference-policy wording and replaced it with high-fidelity reference preservation plus musical-control compilation.

# AutoAlbum MiniMax Changelog

## 3.0-full-api-and-cover-reference-2026-05-11

Added comprehensive MiniMax Music 2.6 API documentation inside the skill:

- Full direct API reference for model choices, prompt, lyrics, stream, output_format, audio_setting, lyrics_optimizer, is_instrumental, cover fields, and response metadata.
- Optional cover/re-render workflows with one-step and two-step cover support.
- Provider capability matrix for direct API, `mmx` CLI, and third-party wrappers.
- Response/artifact logging reference.
- `mmx` CLI reference.
- Expanded generation packet schema covering stream, output_format, audio profiles, download policy, and provider support validation.
- New cover packet schema.
- New render log schema.
- New delegated prompts for cover packets, cover preprocess/re-render, API payload export, render logging/download, and audio profile selection.

Core philosophy preserved: AutoAlbum is the creative-control, songwriting, production-planning, and prompt-compilation layer; MiniMax renders audio.

## v4.0 - Style catalog and artist fingerprints

- Added first-class style catalog subsystem for genre, subgenre, artist, producer, scene, era, and song-reference requests.
- Added detailed genre templates for hip-hop/rap, pop/R&B, electronic/dance, Latin/global, and rock/country/alt.
- Added high-detail artist influence profiles for Juicy J / Three 6 Mafia, Kendrick Lamar lanes, Juice WRLD, Travis Scott, Future, Drake, Playboi Carti, Tyler, The Creator, The Weeknd, SZA, Billie Eilish, Frank Ocean, Ariana Grande, Taylor Swift, Bad Bunny, Burna Boy, Fred again.., Tame Impala, Olivia Rodrigo, and Lana Del Rey.
- Added style-selection, album-style-map, style-to-MiniMax compilation, and style-fidelity evaluation delegated prompts.
- Added `style_profile.schema.json` and expanded `generation_packet.schema.json` with style-selection/style-card fields.
- Added source-index research notes for MiniMax, genre templates, artist profiles, and professional production/songcraft references.

## v5 — Current Rap Style Catalog Expansion

Added a detailed current-rap style catalog with:

- high-detail fingerprints for major current rappers and rap-adjacent artists;
- song-reference fingerprints for dominant/current rap hits;
- differentiation matrix to prevent artist/style blur;
- MiniMax prompt recipes for rap lanes;
- rap style-fidelity rubric for pre-generation and post-generation review;
- routing rules for strictness 4–5 artist/song requests.


## v6 — Quality review, style QA, and MiniMax control hardening

- Added a full QA review of the skill as a system.
- Added style catalog quality standards and a catalog QA checklist.
- Added MiniMax prompting and style-control playbook connecting API parameters to musical decisions.
- Added professional songcraft and arrangement controls for melody, harmony, groove, tension, and album sequencing.
- Added current-rap 2026 addendum for recent chart/currentness tracking and expansion targets.
- Added delegated prompts for style catalog refinement and current rap refresh.
- Updated SKILL.md version metadata and quality discipline section.


## v7.0 — Deep refined skill QA, style-card schema, parameter audit, and current rap precision

- Standardized style artifact paths under `style_catalog_outputs/`.
- Added `references/architecture/operating_contract.md`.
- Added `references/architecture/artifact_path_standard.md`.
- Added `references/api/minimax_high_control_protocol.md`.
- Added `references/api/minimax_parameter_decision_tree.md`.
- Added `references/craft/pro_album_a_and_r_standards.md`.
- Added `references/style_catalog/style_catalog_governance.md`.
- Added `references/style_catalog/style_axis_taxonomy.md`.
- Added `references/style_catalog/track_style_card_template.md`.
- Added `references/schemas/track_style_card.schema.json`.
- Added current rap refresh, artist precision, song precision, and source-index files.
- Added delegated prompts for track style cards, candidate comparison, final A&R review, MiniMax parameter audit, and style catalog QA/refresh.
- Added deep review and completion matrix quality references.
- Tightened `SKILL.md` gates with track-style-card and parameter-audit requirements.

## v11.0 — Critical Musical Analyst Gates

- Added mandatory harsh critical musical analyst review protocol after every material pipeline stage.
- Added `references/critics/critical_musical_analyst_protocol.md`.
- Added `references/delegated/32_critical_musical_stage_review.md`.
- Added `references/schemas/critic_stage_review.schema.json`.
- Added a comprehensive full-pipeline critical audit: `removed historical critical-audit file`.
- Added per-stage critic comment files under `removed generated critic-comment examples`.
- Updated `SKILL.md` to require project-level critic comments under `<project_slug>/reviews/critic_comments/` before phase advancement.
- The critic now explicitly reviews songcraft, style fidelity, musical theory, arrangement, MiniMax parameter control, post-render review, album sequence, release packaging, and state/provenance discipline.
- Added `references/architecture/render_error_handling.md` and `references/schemas/render_queue.schema.json` to support the critic's render-logistics findings.

## v13.0 — Professional Completion Hardening

Implemented all v12 self-audit recommendations as active skill mechanics:

- Mandatory prosody/scansion/topline gate before MiniMax packet compilation.
- Mandatory prompt-budget and compression gate before packet approval.
- Provider-specific MiniMax route profiles for direct API, CLI, Replicate, fal, and Cloudflare routes.
- Final audio/mastering/transition QC for release-package goals.
- Timestamped listening-note schemas for render review and final QC.
- Expanded non-rap style catalog fingerprints for pop/R&B, electronic/dance, Latin/global, rock/country/alternative, and producer/mix taxonomies.
- Professional songwriting and production workflow reference.
- Active phase gate matrix and active reference index.
- Generation packet schema now records provider profile, style card, prosody review, prompt-budget report, and control reliability.

## v17 — AutoNovel Strength Closure

Added the remaining high-impact AutoNovel-derived mechanisms that improve AutoAlbum quality without forcing identical architecture:

- concept/seed tournament
- style and voice fingerprint trials
- hook/title tournament
- motif plant/payoff ledger
- head-to-head candidate tournament
- transactional keep/discard protocol
- regression invariant checks
- executive producer review loop

Also added schemas and stage-map wiring for these mechanisms.

## v18 — Second-Round Design Verified

- Fixed stale active routing so `references/active/CURRENT.md` now points to v18 active control files.
- Added `canonical_phase_order.md` to integrate AutoNovel-inspired mechanisms into the normal phase sequence instead of appending them as optional extras.
- Added `gate_applicability_matrix.md` so gates are scope-aware and quality-mode-aware.
- Added `pipeline_controller_blueprint_v18.md` to define how an agent/future orchestrator should select gates, update state, use transactions, and avoid false completion claims.
- Added `second_round_design_audit_v18.md` documenting design choices, rejected alternatives, and remaining implementation-level limitations.
- Added `stage_reference_map.md` with corrected sequencing.
- Added `phase_gate_matrix.md` with concise v18 pass/failure actions.
- Split adversarial review into pre-packet song/preproduction review and post-packet prompt/packet review.
- Updated `SKILL.md` to reference v18 active files and corrected completion checks.

## v20.0-agent-enforced-workflow-2026-05-11

- Added agent-native enforcement layer with bundled `scripts/autoalbum_guard.py`.
- Added machine-readable controller assets:
  - `references/controller/phase_order.json`
  - `references/controller/gate_requirements.json`
- Added controller architecture docs:
  - `references/architecture/agent_native_enforcement_layer.md`
  - `references/architecture/controller_command_protocol.md`
  - `references/architecture/active_reference_index.md`
  - `references/architecture/stage_reference_map.md`
  - `references/architecture/phase_gate_matrix.md`
- Updated `SKILL.md` and `references/active/CURRENT.md` to make controller usage part of the active workflow.
- Updated `state.schema.json` to accept v20 controller phase IDs and optional controller bookkeeping fields.
- Controller supports `init`, `status`, `validate`, `gate`, `advance`, `manifest`, `snapshot`, `rollback`, `record-result`, and `list-phases`.
- Design decision: enforce workflow structure programmatically while leaving creative/music judgment to the skill's rubrics, style catalog, and review loops.

## v21 — Current consistency verified

- Re-verified MiniMax Music 2.6 direct API assumptions against public docs on 2026-05-11.
- Added `references/controller/phase_applicability.json` so controller routing distinguishes required, conditional, optional, and skipped phases.
- Updated `autoalbum_guard.py` to report phase applicability in `route` and `status`, skip non-applicable gates by default, and support `gate --force` for debugging.
- Updated `autoalbum_guard.py validate` to run JSON/JSONL syntax checks plus schema validation for known artifacts when `jsonschema` is available.
- Fixed project initialization so generated `project_config.json` conforms to `project_config.schema.json`.
- Updated state schema and initialization for controller metadata and nullable canon path during early phases.
- Updated generation packet schema to align provider/model identifiers, require non-empty prompts for AutoAlbum quality, and reject contradictory `lyrics_optimizer=true` with `is_instrumental=true`.
- Clarified direct API defaults versus AutoAlbum quality defaults, especially `output_format` and prompt requirements.
- Removed or neutralized stale active version labels from key instruction files.
- Expanded provider profile metadata with last-verified/source fields and current direct-API mode rules.
