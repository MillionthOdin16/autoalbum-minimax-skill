# Delegated Task: Prompt Budget and Compression

## Objective
Audit and, if needed, compress `prompt_minimax.txt` so it is concise, vivid, MiniMax-compatible, and musically controlling.

## Read
- `<project_slug>/tracks/tr_NN/style_card.json`
- `<project_slug>/tracks/tr_NN/brief.md`
- `<project_slug>/tracks/tr_NN/prompt_minimax.txt`
- `<project_slug>/tracks/tr_NN/generation_packet.json`
- `<project_slug>/project_config.json`
- `references/api/prompt_budget_and_compression_protocol.md`
- selected provider profile under `references/api/provider_profiles/`
- `references/schemas/prompt_budget_report.schema.json`

## Process
1. Count prompt characters.
2. Identify all style anchors, controls, and production details.
3. Remove non-audible exposition and redundant adjectives.
4. Preserve reference anchors and concrete controls.
5. Ensure the prompt contains groove/drums/bass/vocal/hook/arrangement/mix cues where relevant.
6. Check for contradictions.
7. Save a revised prompt if compression improves the packet.

## Output
Write:

```text
<project_slug>/tracks/tr_NN/prompt_budget_report.json
<project_slug>/tracks/tr_NN/prompt_budget_report.md
```

If revised, also write a new version under:

```text
<project_slug>/tracks/tr_NN/versions/prompt_vXX.txt
```

and update `prompt_minimax.txt`, `generation_packet.json`, `state.json`, and `project_manifest.json`.
