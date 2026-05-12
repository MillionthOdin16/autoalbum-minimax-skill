# MiniMax Style Compiler

The style compiler turns a style selection object and track brief into `prompt_minimax.txt`, `generation_packet.json`, and provider-specific CLI/API fields.

## Prompt architecture

For strict artist/subgenre targets, use this order:

```text
[Reference anchor + style lane]. [Tempo/groove]. [Vocal identity]. [Drums/bass]. [Harmony/instrumentation]. [Lyric/theme posture]. [Arrangement/tension behavior]. [Mix/space].
```

Example skeleton:

```text
A {style_lane} track in the lane of {reference_anchors}, with {tempo_feel} and {groove}. The vocal is {vocal_delivery}, with {adlib_behavior}. Production centers on {drums}, {bass}, {instrumentation}, and {mix_space}. The song is about {theme}. The arrangement should {section_energy_arc}, with a hook that {hook_contract}.
```

## Maximum useful density

MiniMax performs best when the style prompt feels like a musician/producer brief, not a taxonomy dump. Use:

- 1 named lane line
- 1 rhythm/groove line
- 1 vocal line
- 1 production/mix line
- 1 lyric/theme/arrangement line

For style strictness 5, add one more sentence with non-negotiable details.

## Bad prompt

```text
Trap, dark, Juicy J, Memphis, 808, cowbell, crunk, club, horrorcore, chant, triplet, energetic, bass, synth, adlibs, repetitive, rap.
```

## Strong prompt

```text
A raw Memphis crunk-trap anthem in the lane of Juicy J and Three 6 Mafia, built around a slow half-time bounce that can also feel double-time. The beat should hit with thick tuned 808s, sharp digital snares, syncopated hi-hats, and a persistent cowbell pulse over an eerie minor synth loop. The vocal should be commanding, shouted, chant-like, and full of short ad-libs, with a repetitive club hook that sounds instantly usable by a crowd. Keep the arrangement stripped down, dark, bass-heavy, and hypnotic rather than glossy.
```

## Style prompt fields for `generation_packet.json`

```json
{
  "style_selection": {
    "raw_style_request": "...",
    "style_strictness": 4,
    "reference_anchors": [],
    "primary_style_ids": [],
    "secondary_style_ids": [],
    "style_weights": {},
    "fingerprint_priority": []
  },
  "style_card": {
    "genre_lane": "...",
    "tempo_range_bpm": "...",
    "groove": "...",
    "drums": "...",
    "bass": "...",
    "harmony": "...",
    "instrumentation": "...",
    "vocal_delivery": "...",
    "lyric_posture": "...",
    "arrangement_arc": "...",
    "mix_space": "...",
    "hook_mechanics": "...",
    "avoid": []
  }
}
```

## For album-level style maps

Compile shared DNA and controlled deviations separately:

```text
Album DNA: traits that recur across most tracks.
Track Delta: what changes on this track.
```

MiniMax prompt should include both:

```text
This track belongs to the album's shared nocturnal Memphis-trap world, but it is the most aggressive club-facing cut: faster hi-hat motion, more crowd ad-libs, and a simpler hook than the surrounding tracks.
```

## CLI export mapping

When provider is `mmx_cli`, map style fields as:

```json
{
  "genre": "primary genre/subgenre",
  "mood": "emotional + energy posture",
  "vocals": "lead vocal identity and delivery",
  "instruments": "drums, bass, key instruments",
  "bpm": "target range or exact if requested",
  "key": "target key/mode if important",
  "tempo": "slow|medium|fast plus feel",
  "structure": "MiniMax tag plan",
  "references": "artist/song/album anchors",
  "avoid": "failure modes",
  "use_case": "album track / lead single / interlude / closer"
}
```
