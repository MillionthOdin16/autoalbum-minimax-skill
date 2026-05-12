# MiniMax Music 2.6 Prompting and Style-Control Playbook

## Purpose

This file converts MiniMax Music 2.6 API capabilities into practical music-generation decisions. Use it whenever compiling or evaluating `prompt_minimax.txt`, `generation_packet.json`, variants, or cover/re-render packets.

## Source-grounded MiniMax facts

- Direct API models include `music-2.6`, `music-cover`, `music-2.6-free`, and `music-cover-free`.
- `prompt` describes style, mood, and scenario.
- For direct text-to-music, prompt length is 0-2000 characters for non-instrumental and 1-2000 for instrumental.
- `lyrics` is required for non-instrumental `music-2.6` / `music-2.6-free` and can be 1-3500 characters.
- `lyrics` is not required for instrumental mode.
- Structure tags supported by the direct API include `[Intro]`, `[Verse]`, `[Pre Chorus]`, `[Chorus]`, `[Interlude]`, `[Bridge]`, `[Outro]`, `[Post Chorus]`, `[Transition]`, `[Break]`, `[Hook]`, `[Build Up]`, `[Inst]`, and `[Solo]`.
- `stream=true` requires `output_format=hex`.
- URL outputs expire after 24 hours and must be downloaded immediately.
- `lyrics_optimizer=true` can generate lyrics from prompt when lyrics are empty.
- `is_instrumental=true` removes the need for lyrics.
- MiniMax prompting guidance favors vivid English sentences rather than comma-separated tags.

## Prompt density target

For most serious album tracks, target:

```text
700-1400 characters: ideal
1400-1800 characters: acceptable if complex
1800-2000 characters: risky; use only when style/fusion demands it
```

Do not use the full 2000-character limit by default. More words can reduce control by making the most important instructions less salient.

## Prompt architecture

Use this order:

```text
1. Mood + tempo feel + exact style lane
2. Vocal identity and delivery
3. Track premise / emotional scene
4. Groove, drums, bass, and harmonic color
5. Hook behavior
6. Tension/arrangement architecture
7. Album-continuity cue or style differentiator
```

Example skeleton:

```text
A tense but triumphant 96 BPM West Coast rap anthem with dry commanding lead vocals, crisp claps, clipped sub bass, and a chant-hook designed for crowd response. The song is about {track premise}. The groove should bounce hard without turning into cloudy trap: bright percussion, sparse eerie synth stabs, short bass punctuation, and sudden DJ-style drops. Verses should feel sharply articulated and competitive; the chorus should turn one central phrase into a slogan. Keep the vocal front-and-center and leave room for every bar to land.
```

## Style-control hierarchy

Use hard constraints only for what must happen. Use soft guidance for what should happen if the model can follow it.

### Hard constraints

```text
lyrics field exactly as supplied
valid structure tags only
vocal track vs instrumental
core style lane
main hook function
critical avoid-list items
```

### Soft guidance

```text
BPM range
key center / harmonic color
instrument palette
effects/mix texture
arrangement details
section energy levels
reference anchors
```

### Non-controllable or weakly controllable

```text
exact chord voicings
exact bar counts
exact melody notes
specific plugin/signal-chain settings
precise loudness targets
exact mix balance
```

Do not let weakly controllable details crowd out the core style lane.

## Lyrics field rules

Use the lyrics field for words and structure, not production prose.

Good:

```text
[Verse]
line
line

[Pre Chorus]
line
line

[Chorus]
line
line
```

Avoid:

```text
[Chorus louder with more reverb and distorted synths]
```

Put that in the prompt instead.

## Structure-tag strategy

### Rap and trap

Common effective skeletons:

```text
[Intro]
[Hook]
[Verse]
[Hook]
[Verse]
[Bridge] or [Break]
[Hook]
[Outro]
```

or:

```text
[Intro]
[Verse]
[Chorus]
[Verse]
[Chorus]
[Break]
[Chorus]
[Outro]
```

### R&B / melodic rap

```text
[Intro]
[Verse]
[Pre Chorus]
[Chorus]
[Verse]
[Pre Chorus]
[Chorus]
[Bridge]
[Chorus]
[Outro]
```

### Rage / chant tracks

```text
[Intro]
[Build Up]
[Hook]
[Verse]
[Hook]
[Break]
[Hook]
[Outro]
```

### Dance / electronic

```text
[Intro]
[Build Up]
[Hook]
[Break]
[Build Up]
[Hook]
[Outro]
```

## Style fidelity levers MiniMax can hear

Prioritize these in prompts:

```text
groove and drum feel
bass/808 shape
vocal tone and delivery
hook type
main texture/instrument palette
energy curve
mix-space adjectives
scene/atmosphere
```

Lower priority:

```text
long biographies
abstract lore
highly specific chord numerals
overlong reference lists
unrelated adjectives
```

## Variant design

Every important track should have variants that change only one or two control dimensions.

```text
A_on_brief: most faithful version
B_hook_forward: same style, stronger hook/chorus salience
C_bold: more extreme texture or arrangement risk
D_vocal_focus: more vocal identity and delivery control
E_groove_focus: stronger drums/bass/pocket control
```

Never create variants that change everything at once. If the render improves, you need to know why.

## Cover / re-render guidance

Use cover mode when there is existing source audio whose melody/structure should be preserved while changing style. Use text-to-music when the track is still being invented.

Cover prompts are shorter. Prioritize:

```text
target genre
vocal/arrangement transformation
energy level
instrument palette
mix feel
```

## Packet evaluation hot list

Before generation, fail the packet if:

```text
prompt is a tag pile
prompt exceeds 2000 chars
lyrics exceed 3500 chars
unsupported bracket tags appear
style lane could fit multiple unrelated artists
hook function is unclear
there is no section energy map
BPM/tempo/genre conflict
voice direction conflicts with lyric density
track duplicates neighbor track
output_format conflicts with stream setting
URL output lacks download policy
```


## Contradictory modes

Do not combine `lyrics_optimizer: true` with `is_instrumental: true`. Optimizer asks the model to create vocal lyrics; instrumental mode asks for no vocals. Pick one intent and make the packet unambiguous.
