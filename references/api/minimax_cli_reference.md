# MiniMax `mmx` CLI Reference for AutoAlbum

## Purpose

This file documents the official `mmx` CLI route as a provider profile. Use it when AutoAlbum is run in an agent environment where `mmx` is installed and authenticated.

## Verification commands

```bash
command -v mmx && mmx --version || echo "mmx not found"
mmx quota show
```

## Agent flags

Always include:

```bash
--quiet --non-interactive
```

## Vocal generation with AutoAlbum lyrics

```bash
mmx music generate \
  --prompt "<vivid English prompt>" \
  --lyrics "<lyrics_minimax.txt content>" \
  --genre "<primary genre/subgenre>" \
  --mood "<mood>" \
  --vocals "<vocal identity>" \
  --instruments "<2-5 key instruments/textures>" \
  --bpm "<BPM or range if supported>" \
  --key "<key center if useful>" \
  --tempo "<tempo feel>" \
  --structure "<section plan>" \
  --references "<translated influence attributes, not copy targets>" \
  --avoid "<failure modes>" \
  --use-case "album track" \
  --out "tracks/tr_01/renders/raw/tr_01_A_take_01.mp3" \
  --quiet --non-interactive
```

## Vocal generation with lyrics optimizer

Use only for scratch/baseline diagnostics:

```bash
mmx music generate \
  --prompt "<vivid English prompt>" \
  --lyrics-optimizer \
  --genre "<genre>" \
  --mood "<mood>" \
  --vocals "<vocal identity>" \
  --out "tracks/tr_01/renders/scratch/tr_01_optimizer_baseline.mp3" \
  --quiet --non-interactive
```

## Instrumental generation

```bash
mmx music generate \
  --prompt "<instrumental scene + style prompt>" \
  --instrumental \
  --genre "<genre>" \
  --mood "<mood>" \
  --instruments "<instruments/textures>" \
  --structure "<intro/buildup/break/etc.>" \
  --out "tracks/tr_04/renders/raw/tr_04_instrumental_take_01.mp3" \
  --quiet --non-interactive
```

## Cover from local file

```bash
mmx music cover \
  --prompt "<target cover style>" \
  --audio-file "<local_source_audio>" \
  --out "covers/renders/tr_05_acoustic_cover.mp3" \
  --quiet --non-interactive
```

## Cover from URL

```bash
mmx music cover \
  --prompt "<target cover style>" \
  --audio "<source_audio_url>" \
  --out "covers/renders/tr_05_acoustic_cover.mp3" \
  --quiet --non-interactive
```

## AutoAlbum CLI export rules

When target provider is `mmx_cli`, generate:

```text
generation/mmx_commands.sh
generation/mmx_command_manifest.json
ops/parameter_audit.md
```

The CLI route may not expose every direct API field. If a direct API parameter has no CLI equivalent, record it as omitted due to provider route.
