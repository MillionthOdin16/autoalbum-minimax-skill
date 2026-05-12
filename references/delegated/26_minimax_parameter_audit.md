# Delegated: MiniMax Parameter Audit

## Task
Audit whether every MiniMax packet and payload uses all relevant API parameters intentionally.

## Read
- `references/api/minimax_music_2_6_full_api_reference.md`
- `references/api/minimax_parameter_decision_tree.md`
- `references/api/minimax_provider_capability_matrix.md`
- `references/schemas/generation_packet.schema.json`
- `references/schemas/cover_packet.schema.json`
- all `tracks/tr_NN/generation_packet.json`
- `generation/api_payloads.jsonl`

## Checks
For each packet, verify:
- model choice is intentional,
- provider choice is supported,
- prompt length is valid,
- lyrics rule matches mode,
- `lyrics_optimizer` rule is valid,
- `is_instrumental` rule is valid,
- direct-API `stream` and `output_format` are compatible when the direct provider is selected; wrapper routes use their own output/download fields,
- audio setting matches selected audio profile,
- download policy exists for URL output,
- tag profile matches lyrics tags,
- cover-specific fields are absent from text-to-music packets,
- response logging fields are prepared.

## Output
Write `ops/parameter_audit.md` and return JSON:

```json
{
  "packets_audited": 0,
  "passed": 0,
  "failed": 0,
  "warnings": [],
  "errors": [],
  "ready_for_generation": false
}
```
