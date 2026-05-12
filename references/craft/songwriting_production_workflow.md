# Professional Songwriting and Production Workflow for AutoAlbum

## Purpose
This file converts professional music-making process into AutoAlbum stages. The agent should use it to avoid shortcutting from concept directly to a MiniMax prompt.

## Professional sequence

### 1. Artistic brief
Define the reason the song or album exists. A brief must include emotional promise, audience aftertaste, style lane, sonic DNA, and the one thing the listener should remember.

### 2. Hook and title lab
Before full lyric drafting, identify candidate titles and hook contracts. A strong hook contract answers:

```text
What phrase, melody, riff, rhythm, bass move, or vocal gesture will the listener remember?
What section delivers it?
Why does it belong in this style?
```

### 3. Form and energy sketch
Map song form and energy before final lyrics:

```text
Intro -> Verse -> Pre Chorus -> Chorus -> Post Chorus -> Verse -> Bridge/Break -> Chorus -> Outro
```

or a genre-appropriate alternative. The form must create tension and release, not merely fill sections.

### 4. Lyric draft
Write section by section. Verses should advance information. Hooks should crystallize. Bridges/breaks should change angle, harmony, rhythm, or emotional pressure.

### 5. Prosody/topline pass
Scan stress, syllables, breath, vowels, cadence, and hook singability. This is mandatory before MiniMax packet compilation.

### 6. Production pre-brief
Define the audible production fingerprint:

```text
groove
drums
bass
harmony
instrument palette
vocal production
arrangement arc
mix space
```

### 7. MiniMax prompt compilation
Compress the pre-brief into a vivid, provider-valid prompt. The prompt should control what the model can render and avoid what it cannot.

### 8. Candidate generation
Generate multiple candidates. Treat renders as demos. Do not choose automatically. Compare against the brief, style card, and actual listening experience.

### 9. Producer review and revision
Choose whether to keep, regenerate from same packet, revise prompt, revise lyrics, change style card, cut track, or resequence.

### 10. Album assembly
Make album-level decisions only after hearing audio. Sequence for promise, contrast, development, climax, and closer. Final package requires selected audio, metadata, provenance, and QC.

## Anti-shortcut rule
The agent must not skip from `style_selection.json` to `generation_packet.json` without the intervening craft artifacts unless the user explicitly requests a rough scratch prompt.
