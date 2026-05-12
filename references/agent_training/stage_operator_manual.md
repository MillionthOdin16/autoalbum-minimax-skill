# Stage Operator Manual for AutoAlbum Agents

This manual tells a non-expert agent exactly how to operate each stage without relying on unstated musical knowledge.

## Universal stage procedure

For every stage:

1. Read the stage's delegated prompt.
2. Read the required agent-training references for that stage.
3. Identify the artifact's musical purpose.
4. Produce the artifact using concrete musical language.
5. Run the stage checklist.
6. Record assumptions, scores, blockers, and next action in state/provenance.
7. Do not proceed if a hard gate fails.

## Stage 0: Intent/config

Goal: determine what the user actually wants without making the project larger or smaller than requested.

High-quality behavior:
- If the user asks for one song, run single-track mode.
- If the user asks for an album, build an album with arc and sequence.
- If the user names a style or artist/song, preserve that reference as a style anchor.
- If the user gives only a theme, infer style only when necessary and document it.

Failure signs:
- Asking unnecessary preference questions.
- Converting a single into a full album.
- Ignoring named style references.

## Stage 0B: Style resolution

Goal: convert user style language into musical controls.

Output must include:
- style lane
- reference anchors
- tempo/groove
- drums/bass
- harmony
- vocal posture
- hook mechanics
- production/mix texture
- adjacent-style differentiators

Failure signs:
- “Trap beat with emotional lyrics” without flow, 808, drum bounce, vocal posture, hook type.
- “Like Artist X” without explaining the artist's mechanics.

## Stage 1: Foundation

Goal: define the album's reason to exist and its audible DNA.

A good foundation is not a mood board. It states:
- the thesis
- the sonic world
- vocal identity
- lyric voice
- motif system
- forbidden generic moves
- how the album will evolve

Failure signs:
- Beautiful prose that does not control songs.
- A world that cannot be heard.
- Themes that could fit any project.

## Stage 2: Tracklist and musical design

Goal: design the sequence and each song's role before lyrics.

Each track needs:
- function
- emotional role
- sonic role
- hook contract
- groove/tempo feel
- energy map
- arrangement sketch
- style delta
- transition role

Failure signs:
- All tracks have similar energy.
- Track titles differ but functions do not.
- No reason a track could not be cut.

## Stage 2B: Hook/title/preproduction lab

Goal: create a central listener-memory target before writing full lyrics.

Each song needs:
- title phrase or hook nucleus
- hook type
- emotional payoff
- likely chorus delivery
- section-level energy plan
- style-specific production promise

Failure signs:
- Hook is only an abstract idea.
- Title never appears in a memorable place.
- The song has no one-sentence replay reason.

## Stage 3: Lyrics

Goal: write performable songs, not literary pages.

Lyrics must:
- use supported MiniMax section tags
- keep verses advancing
- make chorus repeatable
- leave breath space
- match style cadence
- avoid generic abstractions unless grounded in image/action

Failure signs:
- Verse 2 repeats Verse 1.
- Chorus explains the theme rather than embodying it.
- Lines are too long to sing or rap.

## Stage 3B: Prosody/topline

Goal: verify the lyric can be delivered.

Check:
- line stress
- syllable density
- breath points
- rhyme placement
- hook vowel shape
- style-specific cadence
- section contrast

Failure signs:
- Hook title lands on weak syllables.
- Every line has the same length.
- Rap lyrics have no rests or cadence variation.

## Stage 5: MiniMax packet

Goal: translate the song into a renderer-ready packet.

Prompt must include:
- style lane
- vocal identity
- groove/drum/bass behavior
- arrangement/tension behavior
- production/mix-space details
- emotional scene
- hook mechanics

Failure signs:
- Prompt is a tag pile.
- Prompt is a lore dump.
- Prompt contradicts lyrics or style card.

## Stage 7-9: Variants, render, review

Goal: search intelligently, then judge ruthlessly.

Good review compares actual audio to:
- song intent
- style fingerprint
- hook impact
- vocal identity
- lyric adherence
- album placement

Failure signs:
- First render is accepted by default.
- Review lacks timestamps.
- A stylish but unmemorable track is kept.

## Stage 10: Album assembly/release

Goal: make the album work as a sequence.

Check:
- first three tracks promise the record
- middle does not sag
- transitions make sense
- closer earns the aftertaste
- weakest track is justified, revised, or cut

Failure signs:
- Sequence follows creation order.
- All songs are similar key/tempo/texture.
- Final package lacks selected audio/provenance.
