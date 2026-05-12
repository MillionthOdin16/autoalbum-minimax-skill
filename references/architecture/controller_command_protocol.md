# Controller Command Protocol

Use the helper with:

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py <command> ...
```

The helper is intentionally dependency-free and uses only Python's standard library.

## Commands

### Initialize project

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py init "Project Name" \
  --root . \
  --scope album \
  --output-goal release_package \
  --tracks 10 \
  --provider-profile references/api/provider_profiles/direct_minimax_api.json
```

Creates:

```text
<project_slug>/
  project_config.json
  state.json
  project_manifest.json
  intent_intake.json
  seed.txt
  results.tsv
  style_catalog_outputs/
  foundation/
  planning/
  tracks/tr_NN/
  generation/payloads/
  ops/
  reviews/
  release_package/
```

### Check project status

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py status <project_slug>
```

Use this before deciding what to do next.

### Validate project files

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py validate <project_slug>
```

`validate` checks required root control files, JSON/JSONL syntax, and known JSON schemas when `jsonschema` is available. If schema validation is unavailable, the command reports that limitation instead of silently pretending schema validation happened.

Checks root control files and JSON/JSONL parseability. It is not a substitute for stage rubrics.

### Check a phase gate

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py gate <project_slug> --phase packet_compilation --write-report
```

Use before advancing. The report is written under:

```text
<project_slug>/reviews/controller/gate_<phase>.json
```

### Advance phase

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py advance <project_slug> --to packet_evaluation --require-gate
```

`--require-gate` blocks advancement if the current phase's required artifacts are missing.

### Refresh manifest

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py manifest <project_slug>
```

Use after creating, deleting, or moving material artifacts.

### Snapshot before risky revision

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py snapshot <project_slug> --label before-hook-rewrite
```

Use before risky lyric rewrites, style changes, prompt rewrites, resequencing, selected-render replacement, or release-package changes.

### Roll back

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py rollback <project_slug>
```

Rolls back to the latest snapshot. Use `--snapshot <snapshot_dir_name>` to select a specific snapshot.

### Record a score or decision

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py record-result <project_slug> \
  --phase packet_evaluation \
  --artifact-id tr_03_packet \
  --track-number 03 \
  --score-type minimax_packet_score \
  --score 8.6 \
  --status pass \
  --decision keep \
  --path tracks/tr_03/generation_packet.json
```

Use this when a stage evaluator produces a meaningful score or keep/revise/regenerate/cut decision.

### List phases

```bash
python ${HERMES_SKILL_DIR}/scripts/autoalbum_guard.py list-phases
```

## When the agent must run the helper

Run the helper at minimum:

1. after project setup;
2. before moving from planning to lyrics;
3. before MiniMax packet compilation;
4. before declaring packets MiniMax-ready;
5. before rendering;
6. after render download/logging;
7. before release packaging;
8. before final completion claim.

## What gate checks mean

A gate check confirms required artifacts exist. It does not prove those artifacts are good. After a gate passes, still run the required musical, style, API, and final QC evaluators for that phase.

## Failure handling

If a gate fails:

1. Do not advance.
2. Read the missing artifact list.
3. Create or repair missing artifacts using the stage reference map.
4. Re-run the gate.
5. Update `state.json`, `project_manifest.json`, and `results.tsv`.

If validation fails due to malformed JSON/JSONL:

1. Fix syntax without changing artistic content.
2. Re-run validation.
3. Then continue the stage.


## Phase applicability

The controller reads `references/controller/phase_applicability.json` to classify each phase as required, conditional, optional, or skipped for the project scope, output goal, and quality mode. Do not create dummy artifacts for skipped phases. Use `gate --force` only when debugging a skipped phase intentionally.


## Completion-oriented routing

`route` always includes `completion_fit` as the final phase. Earlier output goals such as `minimax_ready_packets` or `generated_candidates` mark later phases as skipped rather than removing the completion check. This prevents the agent from claiming success without verifying that the delivered artifact matches the user story.

`advance --require-gate` treats skipped phases as complete for advancement; it still gates required, optional-activated, and conditional-activated phases.


## Applicability precedence

Controller applicability is resolved in this order: project scope baseline → quality-mode escalation → output-goal override. Output goal is applied last so packet-only, review-only, or candidate-only projects do not accidentally require release-stage artifacts just because the quality mode is strict.


## Sequential advancement rule

`advance` is sequential by default. The controller refuses non-sequential jumps unless `--allow-jump` is used. Use `--allow-jump` only for documented recovery, replanning, or scope changes; write the reason to `results.tsv` and refresh state/manifest afterward.
