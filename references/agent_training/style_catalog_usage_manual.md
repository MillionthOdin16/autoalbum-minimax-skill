# Style Catalog Usage Manual

This manual teaches the agent how to use style fingerprints without collapsing styles into vague labels.

## Style is not a label

A style request like “rap,” “Juice WRLD,” “dark R&B,” or “reggaeton” is incomplete until converted into musical mechanisms.

Every style card must define:

```text
reference anchors
tempo/groove
drum pattern
bass behavior
harmony/melodic language
instrument palette
vocal delivery
ad-libs/background vocals
hook mechanics
lyric posture
arrangement arc
mix-space fingerprint
failure modes
adjacent-style differentiators
```

## Adjacent-style differentiation

For any strict style request, the agent must explain what would make the output wrong.

Examples:

- Future vs Gunna: Future is more toxic, slurred, narcotic, and chant/melody-driven; Gunna is smoother, glossier, more pocket-focused and fashion/lifestyle-coded.
- Carti vs Yeat: Carti is more punk/minimal/ad-lib/persona driven; Yeat is more alien, bell-heavy, synthetic, slang-dense, and rhythmically tumbling.
- Travis Scott vs Don Toliver: Travis is larger, psychedelic, ad-lib/space/show architecture; Don Toliver is smoother, more melodic, liquid, and sensual.
- Kendrick vs J. Cole: Kendrick is theatrical, voice-shifting, conceptually staged; Cole is conversational, reflective, bar-forward, and less theatrical.
- Alt-R&B vs pop R&B: alt-R&B uses negative space, ambiguity, darker harmony, intimate phrasing; pop R&B uses clearer hooks and radio polish.

## Profile completeness test

A profile fails if it could describe three different artists or subgenres.

Weak:
```text
Modern trap with 808s, catchy hooks, and confident lyrics.
```

Stronger:
```text
Slow half-time Memphis-influenced trap with eerie minor synth loops, dry digital snares, heavy 808/cowbell pulse, chant-like hooks, shouted ad-libs, and club-command lyrics that feel menacing rather than melodic.
```

## Style-card compilation process

1. Preserve raw user reference.
2. Look up catalog profile.
3. If missing, build a temporary fingerprint from available references.
4. Select style strictness.
5. Identify non-confusion controls.
6. Translate style to MiniMax prompt controls.
7. Define album DNA and track-specific delta.
8. Validate with style-fidelity rubric.

## When to refresh catalog

Refresh if:
- user asks for current chart sound
- named artist/song is newer than catalog date
- profile lacks differentiators
- style has shifted recently
- user asks for strictness 5

## How to combine styles

Do not simply list styles. Define hierarchy:

```text
primary style: 70%
secondary style: 20%
accent: 10%
non-negotiable controls:
forbidden bleed:
```

Example:
```text
Primary: melodic trap vocal posture.
Secondary: dark alt-R&B harmony/space.
Accent: synthwave nocturnal pads.
Forbidden bleed: no bright EDM drop, no acoustic singer-songwriter chorus.
```

## Album style map

For albums, define:

- shared DNA across all tracks
- allowed style variation zones
- forbidden off-album sounds
- track-by-track style deltas
- how style changes support the album arc

Cohesion without contrast produces boredom. Contrast without shared DNA produces disjointedness.
