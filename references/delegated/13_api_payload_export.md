# Delegated: API Payload Export

## Task

Export provider-specific MiniMax payloads or CLI commands from approved generation packets. This is the bridge between AutoAlbum planning and actual MiniMax rendering.

## Read

- `references/api/minimax_music_2_6_full_api_reference.md`
- `references/api/minimax_provider_capability_matrix.md`
- `references/api/minimax_cli_reference.md` if provider is `mmx_cli`
- `references/schemas/generation_packet.schema.json`
- all approved `tracks/tr_NN/generation_packet.json`
- all approved variants

## Direct API output

Write JSON Lines:

```text
generation/api_payloads.jsonl
```

One line per render attempt. Include only fields supported by the direct API:

```json
{
  "model": "music-2.6",
  "prompt": "...",
  "lyrics": "...",
  "stream": false,
  "output_format": "url",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "lyrics_optimizer": false,
  "is_instrumental": false
}
```

For instrumental:

```json
{
  "model": "music-2.6",
  "prompt": "...",
  "is_instrumental": true,
  "stream": false,
  "output_format": "url",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  }
}
```

## CLI output

If provider is `mmx_cli`, write:

```text
generation/mmx_commands.sh
```

Every command must include:

```bash
--quiet --non-interactive
```

## Audit output

Write:

```text
ops/parameter_audit.md
```

For each track/variant, list:
- provider.
- model.
- included parameters.
- omitted parameters and reasons.
- downgraded parameters and reasons.
- unsupported requested parameters.
- readiness status.

## Hard validation

Do not export a payload when:
- prompt exceeds selected model limits.
- lyrics exceed selected model limits.
- required lyrics are missing.
- unsupported tags exist.
- `stream: true` with `output_format: url`.
- cover fields are present in a text-to-music packet.
- text-to-music fields violate instrumental/optimizer rules.


## Provider wrapper warning

The examples above show direct MiniMax API payloads. If the active provider is FAL, Cloudflare, Replicate, or another wrapper, export the provider-specific payload shape from `provider_profile_path`. Do not pass direct-only fields such as `output_format` or `stream` unless that wrapper explicitly exposes them. Always preserve the normalized AutoAlbum packet and write the exact provider payload to `generation/payloads/`.
