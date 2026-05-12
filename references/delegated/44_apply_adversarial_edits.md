# Delegated 44 — Apply Adversarial Edits

## Purpose
Convert adversarial findings into controlled patches. Do not rewrite more than necessary.

## Read
- `references/schemas/edit_patch.schema.json`
- `tracks/tr_NN/adversarial_song_edit.json`
- current affected artifacts
- prior versions under `tracks/tr_NN/versions/`
- `state.json`

## Write

```text
tracks/tr_NN/edit_patch_<timestamp>.json
tracks/tr_NN/edit_patch_<timestamp>.md
tracks/tr_NN/versions/*
updated affected artifacts
```

## Patch principles

1. Use the smallest change that resolves the issue.
2. Preserve any section, line, prompt phrase, or production idea that already works.
3. If a local fix causes a global issue, stop and create a propagation debt.
4. Record before/after snippets.
5. Run the relevant evaluator after patching.

## Decision

After patching, choose:

```text
KEEP_PATCH
REVISE_PATCH
DISCARD_PATCH
ESCALATE
```

Update `results.tsv`, `state.json`, and the project manifest.
