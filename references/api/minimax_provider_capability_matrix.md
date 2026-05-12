# MiniMax Provider Capability Matrix

## Purpose

MiniMax Music 2.6 can be accessed through different routes. Direct API, official `mmx` CLI, and third-party wrappers may expose different controls, names, formats, defaults, and tag behavior. AutoAlbum must select a provider profile before compiling payloads.

## Provider profile selection

`project_config.json` must include:

```json
{
  "target_provider": "direct_minimax_api",
  "model": "music-2.6",
  "tag_profile": "direct_minimax_music_generation",
  "output_route": "url",
  "audio_profile": "candidate_review"
}
```

Supported provider profile names:

```text
direct_minimax_api
mmx_cli
replicate
fal
cloudflare_workers_ai
aimlapi
custom
```

## Capability matrix

| Capability | direct_minimax_api | mmx_cli | third-party wrappers |
|---|---|---|---|
| `model=music-2.6` | yes | route-dependent; official skill examples use free model | varies |
| `music-2.6-free` | yes | yes in official skill | varies |
| `music-cover` | yes | cover command available | varies |
| `prompt` | yes | `--prompt`; also structured flags | yes |
| `lyrics` | yes | `--lyrics` | varies |
| `lyrics_optimizer` | yes | `--lyrics-optimizer` | varies |
| `is_instrumental` | yes | `--instrumental` | varies |
| `stream` | yes | not always exposed | varies |
| `output_format=url/hex` | yes | usually handled by CLI | varies |
| `audio_setting` | yes | may be fixed/implicit | varies |
| `audio_url` for cover | yes | `--audio` | varies |
| local file cover | via base64/upload workflow | `--audio-file` | varies |
| `cover_feature_id` two-step | yes | may not expose | varies |
| structured genre/mood/vocals/etc. | not direct API fields | yes as CLI flags | varies |

## Direct MiniMax API profile

Use for highest control and logging.

Required outputs:
- `generation/api_payloads.jsonl`.
- `ops/response_archive/*.json`.
- `ops/render_log.jsonl`.

Recommended for:
- serious album projects.
- exact payload archiving.
- cover preprocessing.
- full API coverage.

## `mmx` CLI profile

Use when the environment favors the official agent-oriented CLI.

Important CLI controls from the official MiniMax skill:

```text
mmx music generate
  --prompt
  --lyrics
  --lyrics-optimizer
  --instrumental
  --genre
  --mood
  --vocals
  --instruments
  --bpm
  --key
  --tempo
  --structure
  --references
  --avoid
  --use-case
  --out
  --quiet
  --non-interactive
```

Cover controls:

```text
mmx music cover
  --prompt
  --audio-file
  --audio
  --out
  --quiet
  --non-interactive
```

AutoAlbum must export `mmx_commands.sh` when target provider is `mmx_cli`.

## Third-party wrapper profiles

For each wrapper, create a separate profile file if used. Do not assume direct API names apply.

Required checks:
- exact model id.
- input field names.
- accepted output formats.
- whether lyrics are separate from prompt.
- whether BPM/key are explicit fields or prompt text.
- whether seed is exposed.
- whether the wrapper returns URL, base64, or direct file.
- whether commercial/license terms differ from direct MiniMax.

## Provider-specific tag profiles

Do not mix tag profiles in the same album unless intentional.

Default direct profile:

```text
[Intro]
[Verse]
[Pre Chorus]
[Chorus]
[Interlude]
[Bridge]
[Outro]
[Post Chorus]
[Transition]
[Break]
[Hook]
[Build Up]
[Inst]
[Solo]
```

Alternate lyrics-generation examples may use:

```text
[Verse 1]
[Pre-Chorus]
[Build-up]
[Instrumental]
[Breakdown]
[Drop]
```

These are not automatically valid for every music-generation route. Validate against the active route.

## Audio profile resolution

The skill may request:

```text
preview_fast
candidate_review
final_archive
```

Provider adapter must resolve that to actual route-supported settings. If unsupported, downgrade explicitly and write a warning to `generation/readiness_report.md` and `ops/parameter_audit.md`.

## Parameter audit output

For every track, write:

```json
{
  "track": "tr_01",
  "provider": "direct_minimax_api",
  "model": "music-2.6",
  "unsupported_requested_parameters": [],
  "downgraded_parameters": [],
  "omitted_parameters": [
    {"name": "stream", "reason": "final render uses non-streaming batch"}
  ],
  "ready": true
}
```
