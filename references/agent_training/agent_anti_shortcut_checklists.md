# Agent Anti-Shortcut Checklists

These checklists are designed to stop non-expert agents from producing low-quality work that merely looks complete.

## Universal anti-shortcut checklist

Before passing any artifact, confirm:

- It has a clear musical purpose.
- It uses concrete terms, not only adjectives.
- It would help MiniMax or a human producer make a better song.
- It identifies failure modes.
- It distinguishes this track from adjacent tracks.
- It preserves project style DNA.
- It has been recorded in state/provenance.

## Genericness detector

Fail the artifact if it depends on phrases like:

- emotional and catchy
- professional sounding
- dark vibe
- hard beat
- memorable hook
- cinematic production
- unique style
- polished vocals
- radio ready

unless those are followed by concrete mechanisms.

## Concrete mechanism requirements

For every track, name at least one item from each category:

```text
hook mechanism:
groove:
drum behavior:
bass behavior:
vocal delivery:
harmonic color:
arrangement/tension move:
production/mix texture:
lyric image/motif:
style differentiator:
```

## “Looks complete but is not” examples

- A 12-track list where every track has a different title but no different function.
- A style card that says “modern trap” without 808/drum/vocal/hook specifics.
- Lyrics with supported tags but no chorus memory.
- Prosody review that scores high without citing weak lines.
- Prompt under 2000 characters but too vague.
- Three variants that differ only by adjectives.
- Post-generation review with no timestamps.
- Release package that lacks selected-audio provenance.

## Mandatory challenge questions

Ask before each pass:

1. What would a listener remember after one play?
2. What would a professional producer cut?
3. What would make this style request fail?
4. What part of this is most likely to become generic in MiniMax?
5. Which neighboring track could this be confused with?
6. What is the weakest line, section, or prompt sentence?
7. Is this artifact useful, or is it just documentation?

## Pass/fail attitude

A stage should fail if it is elaborate but musically weak. A short artifact with concrete, actionable musical controls is better than a long artifact full of vague concept language.
