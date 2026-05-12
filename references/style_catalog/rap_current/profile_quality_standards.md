# Current Rap Profile Quality Standards

## Purpose

Current rap profiles must be sharp enough that two adjacent artists do not collapse into the same MiniMax output. This file defines the standard for artist, song, scene, and fusion fingerprints.

## Required profile anatomy

Each artist profile must include:

```text
Current lane
Best AutoAlbum use cases
Tempo / feel
Drums / groove
808 / bass behavior
Harmony / melodic language
Instrument and texture palette
Vocal delivery
Flow pocket
Ad-lib behavior
Hook mechanics
Lyric posture
Arrangement architecture
Mix / texture
MiniMax prompt capsule
Differentiators
Avoid / failure modes
Album integration notes
Currentness metadata
```

## Currentness metadata

Add this block when refining or adding profiles:

```yaml
currentness:
  status: evergreen | active-current | emerging-current | legacy-current
  last_reviewed: 2026-05-11
  evidence: chart | streaming | playlist | press | cultural-moment | catalog-persistence
  confidence: high | medium | low
  refresh_priority: high | medium | low
```

## Specificity floor

A rap profile must name at least one concrete trait in each column:

| Dimension | Examples of acceptable specificity |
|---|---|
| Tempo/feel | 70-85 half-time, 130-165 rage, 92-104 West Coast bounce |
| Drums | dry clap bounce, rolling hi-hats, detuned drill slides, stomp-clap Memphis chant |
| Bass | clipped sub hits, long distorted 808 slides, rounded luxury bass, blown-out rage 808 |
| Vocal | deadpan, breathy melodic, raspy chant, elastic Auto-Tune, shouted group-hook |
| Hook | slogan chant, one-word mosh hook, melodic refrain, diaristic caption hook |
| Arrangement | beat switch, dropout, long intro/drop, verse-hook loop, feature event |
| Mix | dry forward vocal, cavernous psychedelic, blown-out distorted, glossy expensive |

## Adjacent-artist blur tests

### Drake vs Don Toliver

- Drake: narrator-centered, quotable, diaristic, luxury-confessional, smoother rap/R&B pivot.
- Don Toliver: floating psychedelic melody, voice as texture, less diaristic detail, more woozy nocturnal atmosphere.

### Future vs Gunna

- Future: slurred, narcotic, toxic, emotional fog, heavier darkness.
- Gunna: polished glide, fashion/luxury ease, elastic pocket, lighter status-motion.

### Lil Baby vs NBA YoungBoy

- Lil Baby: urgent aspirational street pressure, clean motivational momentum.
- NBA YoungBoy: raw pain, unstable intensity, emotional rupture, less polished control.

### Carti vs Yeat

- Carti: punk vamp persona, ad-lib architecture, phonetic repetition, mosh chaos.
- Yeat: robotic alien lexicon, bell/synth churn, cybernetic chants, engine-like momentum.

### Travis Scott vs Don Toliver

- Travis: stadium-scale psychedelic trap, cinematic drops, layered Auto-Tuned atmosphere.
- Don Toliver: smoother vocal glide, melodic R&B-rap float, less event-driven production.

### Kendrick vs J. Cole

- Kendrick: theatrical character switches, regional bounces, chant slogans, conceptual compression.
- J. Cole: reflective technical everyman, soulful samples, conversational moral clarity.

## Current rap style lanes to keep distinct

```text
West Coast anthem rap
Toronto melodic rap/R&B
Opium rage / vamp trap
psychedelic stadium trap
Atlanta toxic melodic trap
Atlanta motivational street trap
polished drip trap
Memphis club chant rap
raw St. Louis club rap
UK drill-pop
Florida motion/hustle rap
pain rap / romantic sing-rap
technical legacy rap
alt-rap theatrical performance
```

## MiniMax prompt compilation rule

For a strict current-rap style request, compile no fewer than six style cues:

```text
style lane
groove/drums
bass/808
vocal delivery
hook mechanism
lyric posture
mix texture
arrangement event
```

The prompt should be vivid prose and should generally stay between 800 and 1500 characters.

## Post-render style-fidelity listening checklist

After generation, listen for:

```text
Does the drum pocket match the requested lane?
Does the vocal posture match the artist profile?
Does the hook function match the style?
Does the bass/808 behavior match the lane?
Does the arrangement create the expected event or loop behavior?
Did MiniMax over-smooth an intentionally raw style?
Did MiniMax turn a rap request into pop/R&B?
Did MiniMax ignore the ad-lib or vocal texture requirement?
Does the track sound like the target lane rather than generic trap?
```
