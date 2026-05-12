# Style Catalog Governance

## Purpose
The style catalog converts user style requests into high-fidelity, MiniMax-actionable musical controls.

## Catalog layers
1. Genre templates: broad mechanics shared by a style family.
2. Subgenre profiles: concrete tempo/groove/drum/bass/vocal/hook patterns.
3. Artist fingerprints: specific delivery, arrangement, writing, and texture signatures.
4. Song fingerprints: reference-track mechanics for a single lane.
5. Fusion matrix: controlled blends and conflict resolution.
6. Track style cards: per-track operational packets.
7. Fidelity evaluators: pre-generation and post-render scoring.

## Required profile fields
Every profile used at strictness 4-5 must include:
- currentness metadata,
- popularity/use-case rationale,
- tempo range and feel,
- drum/groove mechanics,
- 808/bass behavior,
- harmonic/melodic palette,
- instrument/texture palette,
- vocal delivery and density,
- ad-lib behavior,
- hook mechanics,
- lyric posture,
- arrangement architecture,
- mix/space,
- MiniMax prompt capsule,
- differentiators from adjacent profiles,
- failure modes,
- album-use recommendations.

## Currentness policy
For current rap/pop catalogs, add or refresh profiles when an artist/song appears in at least two of:
- Billboard chart signal,
- Apple Music/Spotify/YouTube chart or playlist signal,
- major album release or viral moment,
- credible music press coverage,
- platform-native chart mirrors when primary charts are inaccessible.

## Style strictness
- 1: loose vibe.
- 2: recognizable broad lane.
- 3: specific subgenre.
- 4: artist/song/era fingerprint.
- 5: maximum style adherence with adjacent-style non-confusion tests.

## Non-confusion rule
A profile fails if it could be swapped with an adjacent artist or subgenre without changing most of the prompt. Each strict profile must answer: what traits make this not the neighboring lane?

## Prompt compilation rule
A style profile is not copied wholesale into MiniMax. It is distilled into a style card and then into a prompt. The prompt must prioritize audible controls: groove, drums, bass, vocal, hook, arrangement, and mix space.
