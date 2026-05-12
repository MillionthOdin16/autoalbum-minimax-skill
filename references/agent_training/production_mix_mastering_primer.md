# Production, Mix, and Mastering Language Primer

This guide teaches the agent how to describe production in terms MiniMax can use and how to judge rendered tracks.

## Production vs mix vs master

- **Production**: sounds chosen and arranged: drums, instruments, vocals, effects, structure.
- **Mix**: balance and space: vocal level, bass/kick relationship, brightness, width, depth, reverb.
- **Master**: final loudness/tonal consistency across tracks and formats.

## Production controls that affect style

### Vocal space
- dry close-mic vocal
- airy reverb vocal
- heavily tuned melodic rap vocal
- stacked harmonies
- call-and-response ad-libs
- distorted shouted vocal
- whispery intimate vocal
- choir/gang vocal

### Drum texture
- crisp modern trap drums
- dusty boom-bap drums
- live rock kit
- glossy pop drums
- minimal rim/click percussion
- metallic drill hats
- swung R&B percussion
- four-on-the-floor dance kick

### Bass/sub
- clean sub-bass under vocal
- aggressive 808 slides
- warm live bass
- distorted synth bass
- sparse low-end only at chorus
- log-drum bounce

### Space/depth
- intimate dry foreground
- wide cinematic reverb
- dark club space
- bedroom lo-fi close space
- glossy radio-pop width
- claustrophobic mono center

### Texture
- glassy synth arpeggios
- warm Rhodes chords
- distorted guitars
- nylon guitar loop
- choir pads
- vinyl/dust noise
- metallic percussion
- ambient field texture

## What a good MiniMax production prompt includes

1. genre/subgenre/style lane
2. vocal identity
3. groove/drum behavior
4. bass behavior
5. 2-4 production elements
6. mix-space description
7. arrangement/tension instruction

## What to avoid

- too many instruments
- conflicting mix descriptions: “dry intimate vocal” plus “huge washed-out reverb lead” unless section-specific
- abstract-only descriptors
- forcing exact engineering settings MiniMax may not honor
- copying worldbuilding prose into the prompt

## Audio review checklist

When audio exists, listen for:

- vocal intelligibility
- lyrics followed correctly
- hook lands within first half of song
- drums/bass match style
- production not generic
- obvious artifacts or warble
- energy changes between sections
- intro not wasting time
- ending intentional
- adjacent tracks not too similar
- loudness/tonal continuity across album

## Timestamp note examples

```text
00:12 vocal enters too buried; lyric intelligibility weak.
00:41 chorus opens well, but title phrase is not memorable.
01:18 808 slide matches style; keep this take's low-end behavior.
02:05 bridge fails to change enough; regenerate with stronger dropout before final hook.
```

## Mastering/QC language

Use cautious, observable language:
- “appears quieter than surrounding tracks”
- “vocal is masked by synth pad”
- “high end feels harsh on chorus hats”
- “low end overpowers vocal on hook”
- “transition gap feels unintentional”

Do not pretend to measure LUFS or phase without tools unless actual measurements exist.
