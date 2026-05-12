# Musical Expertise Bootcamp for Non-Expert Agents

This file defines the minimum music vocabulary and reasoning needed to run AutoAlbum at high quality. Use it whenever a task asks for musical judgment.

## The five pillars of a high-quality song

1. **Hook**: the memorable musical, lyrical, rhythmic, or production event that makes the listener return. It may be a chorus phrase, melody, chant, riff, drop, vocal gesture, drum pocket, or post-chorus motif.
2. **Identity**: the listener can describe the song in one sentence after one listen. Identity comes from vocal posture, groove, sound palette, lyric world, title phrase, and arrangement shape.
3. **Movement**: the song changes over time. Verses add information, pre-choruses increase tension, choruses release, bridges shift perspective or texture, outros leave an aftertaste.
4. **Fit**: every choice belongs to the intended style, artist lane, album world, and MiniMax prompt. Good choices can be wrong for the target lane.
5. **Finish**: the audio or packet is complete enough to survive professional comparison: no generic filler, no weak opening, no confusing prompt, no careless tags, no unresolved artifact.

## The five pillars of a high-quality album

1. **Promise**: the first one to three tracks tell the listener what world they have entered.
2. **Arc**: the album changes state: emotionally, narratively, sonically, rhythmically, or psychologically.
3. **Cohesion**: recurring DNA connects the songs: voice, production world, motifs, mix space, lyric posture, recurring symbols, or rhythmic philosophy.
4. **Contrast**: tracks do not blur together. Adjacent tracks must have different function, energy, groove, texture, hook type, or emotional angle.
5. **Aftertaste**: the closer or final sequence gives the album a memorable final emotional state.

## Core terms

- **Tempo/BPM**: speed. For MiniMax, express as a feel/range unless the provider reliably supports exact BPM.
- **Meter**: rhythmic grouping, usually 4/4 in pop/rap/dance.
- **Groove**: how rhythm feels: straight, swung, half-time, double-time, behind-the-beat, dembow, four-on-the-floor, bounce, shuffle.
- **Pocket**: the tightness/feel of performance around the beat. A laid-back pocket feels behind the beat; urgent pocket feels on or ahead of it.
- **Cadence**: vocal rhythmic pattern. In rap this includes flow density, rests, syncopation, triplets, double-time, chant delivery.
- **Topline**: vocal melody plus lyrics. For AI music, the lyric must imply singable/rap-able rhythms.
- **Prosody**: alignment between lyric stress, meaning, rhythm, and melody/delivery.
- **Harmony**: chord/key color. Major/minor is not enough; specify sparse modal, jazzy extended, gospel, chromatic, two-chord loop, trap minor loop, etc.
- **Arrangement**: sections and how energy changes: intro, verse, build, hook, break, bridge, drop, outro.
- **Sound palette**: instruments and textures: dry drums, 808, warm Rhodes, glassy synth, distorted guitars, log drum, live brass, etc.
- **Mix space**: perceived depth/width: dry close vocal, wide reverb, dark low-pass, bright glossy top, mono center drums, huge stereo pads.
- **Motif**: recurring lyrical, melodic, rhythmic, or sonic element.
- **Callback**: motif returning with changed meaning.
- **A&R judgment**: commercial/artistic gate: would this earn a place on the project?

## What non-expert agents usually get wrong

- They mistake “specific adjectives” for musical control. “Dark, cinematic, emotional” is not enough. Add groove, vocal delivery, drums/bass, harmony, and arrangement.
- They write lyrics like poetry instead of singable text.
- They make every song verse/chorus/verse/chorus/bridge/chorus even when the style needs a different form.
- They overstuff MiniMax prompts with lore and under-specify the actual sound.
- They preserve style labels but lose the style mechanics.
- They mistake technical cleanliness for quality; a clean song with no hook is not a keeper.
- They sequence by mood similarity rather than album function and contrast.

## Minimum quality test

Before any stage passes, answer:

1. What is the listener meant to remember?
2. What musical mechanism creates that memory?
3. What style fingerprint is being preserved?
4. What exact artifact proves this is ready?
5. What is the most likely failure mode in MiniMax?
6. What would a professional producer or songwriter reject here?
