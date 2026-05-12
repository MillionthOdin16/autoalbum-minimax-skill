# Canonical Phase Order

This is the active phase order. It integrates quality loops, AutoNovel-inspired search/revision mechanisms, and MiniMax-specific controls into one workflow rather than leaving them as optional afterthoughts.

## Universal rule

Do not advance a project phase if a required artifact for the selected scope/output goal/quality mode is missing or failed. Use `gate_applicability_matrix.md` to determine whether a gate is required, recommended, optional, or skipped.

## Phase order

### 0 — Intent and project setup

Create project root, classify scope, output goal, execution mode, quality mode, provider route, and assumptions.

### 0A — Concept option search

Run concept tournament when the seed is vague, generic, high-stakes, release-grade, album/EP-scale, or when the user asks for maximum quality.

### 0B — Style resolution

Resolve genres, artists, songs, eras, scenes, producer styles, and hybrids into concrete musical controls.

### 1A — Style/voice fingerprint trials

Before locking foundation, test candidate lyric voices, vocal identities, style directions, and MiniMax style capsules.

### 1 — Foundation

Define thesis, sound signature, lyric voice, vocal identity, generation constraints, motifs, and vocabulary rules.

### 1B — Album canon and propagation setup

Build the formal canon and initial propagation debt rules.

### 2 — Tracklist, album arc, and style cards

Create skeleton tracklist, track roles, per-track style cards, refined tracklist, energy map, key/BPM map, transition map, and hook index.

### 2C — Motif plant/payoff ledger

For EP/album/concept projects, map motifs, callbacks, transformations, reprises, and forbidden accidental repetition.

### 2D — Hook/title tournament

Run for lead singles, openers, closers, release-grade tracks, or any track whose hook is not obviously strong.

### 2B — Hook/form/arrangement energy design

Design the memory target, form, tension/release, groove, section dynamics, and arrangement energy before full lyric drafting.

### 3 — Lyrics and songcraft

Write/revise lyrics as songs, not poems. Evaluate structure, section progression, emotional specificity, hook support, and cliché avoidance.

### 3B — Prosody/scansion/topline

Evaluate stress, syllables, breath, vowel shape, cadence, genre delivery, rap flow/singability, and hook performance.

### 3C — Preproduction brief

Define groove, drums, bass, harmony, instruments, vocal delivery, mix-space, arrangement priorities, and MiniMax controllability.

### 3D — Adversarial song/preproduction edit

Attack lyrics, hook, form, arrangement, style fit, and preproduction. Patch or revise before prompt compilation.

### 5 — MiniMax packet compilation

Compile lyrics, prompt, provider parameters, generation packet, and versions.

### 5B — Prompt budget and compression

Compress prompts to audible controls, enforce provider limits, remove lore/backstory that will not affect generation.

### 5C — Adversarial prompt/packet edit

Attack MiniMax prompt, packet fields, style translation, API controls, over/underconstraint, and generation risk after the packet exists.

### 6 — Packet/style/parameter evaluation

Validate API/provider constraints, structure tags, prompt clarity, style fidelity, album fit, adjacent-track contrast, and parameter audit.

### 6D — Unified quality evaluation and revision-cycle decision

Combine specialized scores into a single decision: PASS, PASS_WITH_DEBTS, REVISE, REGENERATE, CUT_OR_REPLACE, ESCALATE, or FAIL.

### 7 — Variant strategy

Create complete variant packets for meaningful search space: faithful, hook-forward, bold, and specialist versions when needed.

### 6B — Payload export and render logistics

Export payloads/commands, queue renders, log exact provenance, and archive responses/downloads.

### 6C — Cover/re-render workflow

Run only for source-audio, cover, re-render, or alternate-version projects.

### 8 — Render candidates

Generate audio candidates from approved packets/variants.

### 9 — Candidate review, listener panel, regeneration

Listen, compare, select, revise, regenerate, cut, or escalate. Use listener panel when release-grade, style-strict, high-risk, or borderline.

### 10 — Post-audio rebuild and album assembly

Rebuild tracklist, arc, energy map, transition map, and final sequence from actual selected audio.

### 10B — Final audio QC and release package

Check artifacts, loudness/format consistency, transitions, sequence, metadata, final lyrics, final packets, cover direction, credits, and release package.

### 10C — Executive producer review loop

For release-grade outputs, run whole-work review cycles until no major release blockers remain or the project is marked not release-ready.

### 11 — User-story fit and completion claim

Confirm the actual outputs match the user's requested output goal. Do not claim generated audio when only packets exist; do not claim release readiness without selected renders and final QC.


## V23 additions

- `line_polish` is mandatory for vocal professional-quality tracks.
- `completion_fit` must include freshness, quote, style-catalog, tournament, prompt-lint, variant, payload, state-reconciliation, and independent-verifier checks.
