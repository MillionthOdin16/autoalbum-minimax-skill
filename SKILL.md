---
name: autoalbum-minimax
version: 24.0-production-test-ready-2026-05-12
description: MiniMax Music 2.6 professional track/album creation-control skill with progressive disclosure, style catalogs, songwriting/production training, provider-aware generation packets, quality gates, and agent-native workflow enforcement.
triggers:
  - "write an album"
  - "generate an album with minimax"
  - "autoalbum"
  - "run album pipeline"
  - "create an EP"
  - "create a MiniMax album"
  - "make a song with MiniMax"
---

# AutoAlbum MiniMax 2.6

AutoAlbum is the creative-control layer for MiniMax Music 2.6. It guides an agent from concept to high-quality song/album artifacts: style resolution, songwriting, production planning, MiniMax packets, candidate renders, review, sequencing, final QC, and release packaging.

## Prime directive

Create coherent, distinctive, high-craft, high-appeal tracks and albums. Every stage must improve at least one of: concept strength, songwriting, style fidelity, MiniMax controllability, candidate selection, album flow, or release readiness. Remove or skip work that does not improve those outcomes.

## Progressive disclosure

Do **not** load the whole reference tree. Start with:

```text
references/active/CURRENT.md
references/architecture/stage_reference_map.md
references/architecture/phase_gate_matrix.md
```

Then read only the stage-specific, style-specific, provider-specific, or failure-specific references named there. This follows the skill pattern: `SKILL.md` is the playbook, with resources and scripts loaded only when needed.

## Agent-native enforcement

This is an agent-executed production pipeline. Required artifacts, gates, schemas, state updates, manifest updates, and controller checks are mandatory execution logic, not optional inspiration.

Use the helper for professional, release-grade, autonomous, album/EP/concept-album, or style-strict work:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py <command> ...
```

Core commands:

```text
init        create project root and control files
status      report phase, blockers, missing artifacts, next actions
route       show phase route and required/conditional/skipped applicability for the project
validate    check control files, JSON/JSONL syntax, and known schemas
gate        check required artifacts for a phase
advance     move state.json to next/specified phase
manifest    refresh project_manifest.json
snapshot    save a transaction snapshot before risky edits
rollback    restore latest/named snapshot
record-result append a score/decision row to results.tsv
preflight   run full production-test readiness checks before any completion claim
```

Controller checks prove structure, schema validity, and workflow completeness, not artistry. Musical quality still requires the rubrics, style catalog, listener/A&R review, post-render evaluation, and final QC.


## Verification-first rule

A project is not complete because the required files exist. It is complete only when the files are current, schema-valid, content-valid, provider-ready, and independently verified.

Before any completion claim, run the production preflight. It reconciles state, refreshes manifest, validates schemas, verifies freshness/quotes/style/tournaments/variants/payloads, and lints MiniMax prompts:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py preflight <project_slug> --reconcile
```

For `minimax_ready_packets`, `generated_candidates`, `selected_album_sequence`, and `release_package`, provider-ready payloads are required. Export and verify them before preflight if they do not already exist:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py export-payloads <project_slug>
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py verify-payloads <project_slug>
```

Every evaluation/review that scores or criticizes an artifact must include the path and SHA-256 hash of the artifact it evaluated. Stale reviews, reviews quoting lines that do not exist, invalid style catalog references, non-renderable variants, or prompt lint blockers cap or fail downstream quality gates.

Controller routing is completion-oriented: even packet-only or generated-candidate projects must still run `completion_fit` before the agent claims the requested work is complete. Non-applicable phases are marked `skip`; they should not be fabricated.

## Project root

Every project lives inside a top-level folder named for the work:

```text
<project_slug>/
  project_manifest.json
  state.json
  intent_intake.json
  project_config.json
  seed.txt
  source_notes.md
  results.tsv
  style_catalog_outputs/
  foundation/
  planning/
  tracks/
  generation/
  covers/
  ops/
  reviews/
  release_package/
```

Skill references stay under `references/` and are not modified during ordinary project execution.

## Supported scopes

```text
single_track
lead_single
EP
mixtape
album
concept_album
beat_tape
instrumental_score
cover_or_rerender
revision_of_existing_work
```

Execution modes:

```text
autonomous_full_pipeline
collaborative_checkpoints
packet_only
render_review_only
release_package_only
```

Proceed with reasonable defaults unless a missing decision would materially change the result. If a user gives a concept but no style, treat style as material: generate distinct style-lane options, ask when interactive, or document the selected autonomous style as a material assumption in `intent_intake.json`, `project_config.json`, and `style_selection.json`.

## Canonical workflow

Use `references/architecture/canonical_phase_order.md`, `references/architecture/stage_reference_map.md`, and the controller `route` command for exact stage files, gates, applicability, and escalation references.

Short form:

```text
intent/config
→ concept option search when required/conditional by route
→ style resolution
→ style/voice trials
→ foundation and album canon
→ track planning/style cards/motifs
→ hook/form/preproduction
→ lyrics/prosody
→ adversarial song/preproduction edit
→ MiniMax packet compilation
→ prompt budget/compression
→ adversarial prompt/packet review
→ packet/style/API evaluation
→ unified quality decision
independent verifier review at lyrics, packet, and completion gates
→ variants and payloads
→ candidate rendering/review
→ post-audio rebuild
→ final QC/release package
→ executive producer review
→ completion fit check
```

## Non-expert agent rule

Assume the agent does not already know songwriting, music theory, production, mixing, style analysis, or MiniMax prompting. For any stage that requires musical judgment, use the relevant `references/agent_training/` and `references/craft/` files named in the stage map.

A track cannot pass because it is elaborate. It must demonstrate concrete musical mechanisms: memorable hook, performable prosody, style-specific groove, arrangement tension/release, clear vocal identity, and MiniMax-actionable prompt controls.

## Non-negotiable gates

A vocal track is not MiniMax-ready until the applicable gates pass:

```text
hook/title lab
track style card
songcraft evaluation
arrangement/energy review
prosody/topline review
line polish review
preproduction brief
album canon consistency
adversarial song/preproduction review
provider profile selection
prompt budget report
MiniMax packet evaluation
style fidelity evaluation when a style/reference is requested
parameter audit
unified quality decision
independent verifier review at lyrics, packet, and completion gates
```

An album/release package is not complete until:

```text
all required track artifacts pass
selected renders or approved pending-generation statuses exist
post-audio planning rebuild is complete when renders exist
sequence has been reviewed against actual audio
weakest track is revised, cut, or justified
final audio QC passes for release-package goals
completion claim matches the user’s requested output goal
```

Every material phase must update or explicitly justify no change to:

```text
<project_slug>/state.json
<project_slug>/project_manifest.json
<project_slug>/results.tsv
```

## MiniMax rules

Use the selected provider profile under `references/api/provider_profiles/`. Validate prompt, lyrics, tags, audio settings, streaming/output behavior, and cover-mode fields against that route.

Default serious-work policy:

```text
model: music-2.6
lyrics_optimizer: false except diagnostic/scratch use
is_instrumental: true only for intentional instrumental tracks
prompt language: English unless user asks otherwise
output_format: url for ordinary batch generation, downloaded immediately
stream: false for final renders
archive highest reliable route-supported audio profile
```

## Style catalog rule

When the user names a genre, subgenre, artist, producer, song, album, era, scene, or hybrid style, resolve it through the style catalog before foundation or prompt generation. Preserve the raw style request, then expand it into concrete controls: tempo, groove, drums, bass, harmony, instruments, vocal delivery, ad-libs, hook mechanics, lyric posture, arrangement, mix space, and failure modes.

A good lyric with a weak style card is not MiniMax-ready.

## Optional critic mode

Use critic mode only for high-rigor, style-strict, release-grade, post-render, or blocked projects. It is not a default step after every minor phase.

## Completion

Before claiming completion, run the user-story fit and full-skill quality checks in the stage map. Packet-ready is not generated audio; generated candidates are not a release-ready album.
