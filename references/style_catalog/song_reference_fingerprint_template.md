# Song Reference Fingerprint Template

Use this when the user says: “make it like [specific song]” or “track 4 should feel like [song].”

Do not rely on the song title alone. Build a fingerprint, then compile that fingerprint into MiniMax.

## Research/analysis checklist

```markdown
# Song Reference Fingerprint: {song} by {artist}

## Raw reference
- Song:
- Artist:
- Album/era:
- User's requested strictness:

## Tempo and meter
- Approximate BPM:
- Meter:
- Tempo feel:
- Swing/shuffle/straight:

## Groove
- Drum pattern:
- Backbeat/clap/snare placement:
- Hi-hat/percussion motion:
- Syncopation:
- Dropouts/breaks:

## Bass
- Bass source: 808, synth bass, electric bass, acoustic, log drum, sub, etc.
- Movement: static, sliding, melodic, staccato, walking, pulsing.
- Relationship to kick:

## Harmony
- Key/mode if known:
- Chord complexity:
- Loop length:
- Harmonic tension/release:

## Instrumentation and texture
- Core instruments:
- Signature texture:
- Ear candy:
- Sonic foreground vs background:

## Vocal delivery
- Rap/sung ratio:
- Register:
- Flow density:
- Ad-libs:
- Vocal effects:
- Emotional posture:

## Lyrics and hook
- Hook type:
- Title placement:
- Lyric mode:
- Rhyme density:
- Repetition strategy:

## Arrangement
- Section order:
- Energy curve:
- Where the track changes:
- Best moment:
- Weakness to avoid:

## Mix / space
- Dry vs wet:
- Intimate vs arena:
- Bright vs dark:
- Low-end emphasis:
- Stereo width:

## MiniMax prompt translation
- Reference anchor sentence:
- Required traits:
- Optional traits:
- Avoid traits:
- Structure tag plan:
```

## MiniMax compilation format

```text
A track in the lane of {song} by {artist}, translated into {genre/subgenre}. Use {tempo/groove}, {drums/bass}, {vocal delivery}, {instrumentation}, and {arrangement behavior}. The hook should {hook mechanics}. Keep the mix {mix space}. The song's theme is {new original theme from album}; do not import the reference song's lyrics or story unless user explicitly asks for thematic similarity.
```

## Best practice

For one song reference, produce at least two prompt variants:

- `A_fingerprint_exact`: closest style behavior.
- `B_album_integrated`: keeps fingerprint but adapts to current album DNA.
