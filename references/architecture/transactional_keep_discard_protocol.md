# Transactional Keep/Discard Protocol

## Purpose

A serious creative pipeline must not treat every revision as progress. Before a risky change, the agent must snapshot current artifacts, make a targeted change, evaluate the affected scope, and keep only if quality improves or if a documented strategic reason justifies the change.

This is the AutoAlbum equivalent of AutoNovel's git-backed keep/discard behavior.

## When to use

Use a transaction before any change that can degrade more than one artifact:

- rewriting a hook or chorus
- changing lyric voice
- changing style lane
- changing track order
- altering sound signature
- replacing a selected render
- revising album canon
- switching provider profile
- adding/cutting/merging tracks
- changing a lead single packet
- revising release-package metadata after audio selection

## Transaction folder

For each transaction, create:

```text
<project_slug>/ops/transactions/tx_YYYYMMDD_HHMMSS_<slug>/
  transaction.json
  before_manifest.json
  changed_files.txt
  before/
  after/
  evaluation_before.json
  evaluation_after.json
  decision.md
```

## Transaction JSON

```json
{
  "transaction_id": "tx_20260511_181500_rewrite_track_03_hook",
  "scope": "track|album|release|style|provider|canon",
  "reason": "Hook failed memorability and prosody gate.",
  "files_to_snapshot": [],
  "quality_dimensions_targeted": ["hook_memorability", "prosody", "style_fidelity"],
  "risk_level": "low|medium|high",
  "rollback_allowed": true,
  "started_at": "",
  "completed_at": "",
  "decision": "KEEP|DISCARD|KEEP_WITH_DEBTS|MANUAL_REVIEW"
}
```

## Evaluation rule

Keep a transaction only if:

- targeted quality dimension improves, and
- no critical dimension regresses, and
- no unresolved propagation debts are introduced, and
- unified evaluation is `PASS` or `PASS_WITH_DEBTS`.

Discard if:

- the change only sounds more elaborate but less musical,
- style fidelity drops below target,
- prompt validity breaks,
- track distinctiveness worsens,
- album canon contradiction appears,
- listener-panel or A&R decision worsens.

## Strategic exceptions

Sometimes a local score drops for a better album-level decision. Example: a song becomes less single-like but better as an interlude. In that case, keep only if:

- the tradeoff is explicit,
- album-level score improves,
- the decision is logged,
- affected downstream artifacts are updated.

## State update

Every transaction must append to:

```text
<project_slug>/state.json.transactions[]
<project_slug>/results.tsv
<project_slug>/project_manifest.json
```
