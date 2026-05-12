# Final Audio, Mastering, Transition, and Album QC

## Purpose
A project is not release-ready merely because the prompts and lyrics are strong. Rendered audio must be evaluated as music: arrangement, performance, mix, loudness consistency, transitions, sequence, and listener experience.

## Release-readiness principle
Pre-render planning is a hypothesis. The rendered audio is the artifact. Final album decisions must be made after listening to selected renders in sequence.

## Required listening passes

### 1. Individual track pass
For each selected render, check:

```text
lyric adherence
section adherence
hook impact
vocal intelligibility
vocal identity/style fidelity
arrangement momentum
drum/bass relationship
low-end stability
harshness/sibilance
clipping/distortion artifacts
AI warble/phoneme errors
intro/outro usefulness
replay value
```

### 2. Adjacent-track pass
Listen to each transition pair:

```text
track_N -> track_N+1
```

Check whether the change feels intentional, redundant, jarring in the wrong way, or dramatically effective. Silence, gap length, fade, hard cut, segue, or interlude must be chosen intentionally.

### 3. Whole-album pass
Listen from first selected render to last. Check:

```text
first-three-track promise
energy contour
listener fatigue
middle-album sag
single/deep-cut balance
motif payoff
vocal/production consistency
contrast without disjointedness
closer aftertaste
```

### 4. Technical consistency pass
Check practical release issues:

```text
format consistency
sample-rate/bitrate consistency
obvious loudness mismatch
excessive clipping or distortion
long silence or abrupt cutoff
file naming
metadata correctness
selected render provenance
```

## Mastering realism
AutoAlbum does not replace a mastering engineer or DAW. It must not invent precise LUFS or EQ decisions unless measured. It should instead identify practical issues and recommend whether a track needs regeneration, remastering, external mastering, or sequencing changes.

## Failure conditions
A release package fails if:

```text
selected audio is missing for release_package goals
any selected render lacks provenance
transitions have not been heard in order
weakest track is accepted without rationale
opener does not establish identity
closer does not land
lead single lacks a memorable moment
album has redundant adjacent tracks
technical artifacts distract from the song
release metadata does not map to selected renders
```

## Required outputs

```text
<project_slug>/reviews/final_audio_qc.json
<project_slug>/reviews/final_audio_qc.md
<project_slug>/reviews/timestamped_listening_notes.md
<project_slug>/release_package/quality/final_audio_qc.md
```
