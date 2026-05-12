# Genre Templates: Hip-Hop and Rap

Use these profiles whenever the user asks for rap, hip-hop, trap, drill, crunk, emo rap, melodic rap, boom bap, rage, or related lanes. Generic “rap” is never specific enough for a strong album. Choose a lane.

## Global rap controls

- **Lyrics field**: must support flow. Use shorter lines, internal rhyme, repeated hooks, and clear section tags.
- **Prompt field**: carry the beat, vocal posture, regional/era lane, bass, ad-libs, and mix space.
- **MiniMax tags**: `[Intro]`, `[Verse]`, `[Hook]`, `[Chorus]`, `[Bridge]`, `[Break]`, `[Outro]`, `[Inst]`.
- **Common failure**: the renderer sings too much when the target is rap. Fix by specifying “rapped verses, chant-like hook” or “mostly rap with only a sung hook.”

---

## genre.trap_modern_atlanta

**Use when user says:** trap, Atlanta trap, modern rap, hard 808 rap, street trap, club trap.

**Tempo:** 130–170 BPM counted fast; 65–85 BPM half-time feel.

**Groove:** half-time bounce, snare/clap on beat 3 or heavy backbeat, rapid hi-hat rolls, triplets, stutters, occasional open-hat lifts.

**Drums:** clipped 808 kick/sub, crisp snare/clap, rapid hats, rim or perc accents.

**Bass:** tuned 808s, slides, drops, root-note dominance, kick-sub interplay.

**Harmony:** minor-key loops, sparse piano/bell/pluck/synth melodies, simple 2–4 chord loops.

**Vocal:** confident rap, melodic hooks optional, ad-libs in gaps, call-response.

**Lyric posture:** flex, ambition, struggle, luxury, paranoia, survival, nightlife.

**MiniMax prompt fragment:**

```text
A modern Atlanta-style trap track with a dark minor-key loop, heavy tuned 808s, rapid triplet hi-hats, and a half-time bounce. The verses should be rapped with confident rhythmic pockets, while the hook is short, repetitive, and instantly chantable.
```

**Avoid:** glossy pop drums, rock guitars unless requested, long poetic verses without hook repetition.

---

## genre.memphis_crunk_trap

**Use when user says:** Juicy J, Three 6 Mafia, Memphis rap, crunk, horror-crunk, dark Southern club rap, phonk roots.

**Tempo:** 70–85 BPM half-time, or 140–170 BPM double-time perception.

**Groove:** hypnotic loop, syncopated hats, 808/cowbell pulse, strong downbeat, chant space.

**Drums:** TR-808-style kicks, sharp snares/claps, cowbell, sparse percussion, looped intensity.

**Bass:** powerful sub, usually simple, repetitive, and physical.

**Harmony:** eerie minor synths, horror-film colors, simple piano/bell loops, dark pads.

**Vocal:** shouted commands, triplet/double-time pockets, repetitive group hooks, short ad-libs, crowd-call energy.

**Lyric posture:** club command, menace, hustle, intoxicated nightlife, dark humor, street bravado.

**MiniMax prompt fragment:**

```text
A raw Memphis crunk-trap anthem in the lane of Juicy J and Three 6 Mafia, built on a slow half-time bounce with thick tuned 808s, sharp digital snares, syncopated hi-hats, and a persistent cowbell pulse over an eerie minor synth loop. The vocal should be commanding, shouted, chant-like, and full of short ad-libs, with a repetitive hook built for a crowd.
```

**Best album uses:** opener, club single, rupture track, villain-energy track, mid-album energy spike.

**Avoid:** over-sung R&B chorus, polite drums, too many chord changes, glossy EDM drop.

---

## genre.boom_bap_golden_age

**Use when user says:** boom bap, 90s NY hip-hop, DJ Premier lane, sample-based rap, underground rap.

**Tempo:** 86–100 BPM.

**Groove:** head-nod swing, kick/snare emphasis, acoustic sampled drum feel, MPC/SP-style pocket.

**Drums:** crunchy sampled kicks, snappy snares, vinyl noise, chopped drum breaks, minimal extras.

**Bass:** upright/electric bass sample or filtered low-end from sample; not usually sliding 808s.

**Harmony:** jazz/soul/funk sample loops, dusty piano, horns, strings, chopped fragments.

**Vocal:** clear rapping, bar-focused, internal rhyme, punchlines, narrative skill.

**Lyric posture:** observational, street reportage, battle rap, memory, craft, social commentary.

**MiniMax prompt fragment:**

```text
A dusty 90s boom-bap hip-hop track with swung head-nod drums, crunchy sampled kick and snare, vinyl-textured jazz/soul loop, and sparse bass. Keep the arrangement minimal so the rap sits up front, with clear verses, internal rhyme, and a short scratched-or-chanted hook.
```

**Avoid:** modern trap hi-hat rolls, shiny EDM synths, over-singing, excessive low-end slides.

---

## genre.drill_chicago_uk_ny

**Use when user says:** drill, UK drill, NY drill, Chicago drill, dark aggressive street rap.

**Tempo:** 138–150 BPM, often half-time feel.

**Groove:** sliding 808 bass, syncopated snare/clap, rolling hats, dark/off-center rhythmic pockets.

**Drums:** hard snares, aggressive hats, sparse kicks, tension-building pauses.

**Bass:** sliding/gliding 808s, melodic sub movement, menace.

**Harmony:** dark minor piano, choir, strings, bells, reversed textures.

**Vocal:** aggressive rap, clipped phrasing, rhythmic threats/bravado, little singing unless melodic drill.

**MiniMax prompt fragment:**

```text
A dark drill track with sliding 808 bass, syncopated trap-style hi-hats, heavy snares, and a cold minor-key piano or string loop. The vocal should be aggressive, clipped, rhythmically precise rap with tense pauses and a hook that feels ominous rather than melodic-pop.
```

**Avoid:** sunny chords, over-sung chorus, soft R&B drums.

---

## genre.emo_rap_melodic_trap

**Use when user says:** Juice WRLD, emo rap, melodic trap, SoundCloud heartbreak rap, sad trap, pop-punk rap.

**Tempo:** 140–170 BPM or 70–85 half-time.

**Groove:** trap drums under melodic vocals; hi-hats active but not necessarily aggressive.

**Drums:** 808 kicks, claps/snares, soft trap hats; sometimes pop-punk drum energy.

**Bass:** 808 root notes with simple slides, warm sub under guitar/piano.

**Harmony:** minor guitar/piano loops, pop-punk or emo chord color, simple progressions with high emotional clarity.

**Vocal:** sung-rap, melodic freestyled feel, wounded but catchy; lines should be easy to phrase.

**Lyric posture:** heartbreak, anxiety, addiction, late-night confession, emotional self-contradiction, vulnerability.

**Hook mechanics:** title phrase in chorus, repeated emotional thesis, open vowels, easy singalong.

**MiniMax prompt fragment:**

```text
A melodic emo-rap track in the Juice WRLD lane, with a minor-key guitar or piano loop, warm 808 sub, crisp trap drums, and sung-rap vocals that feel vulnerable, spontaneous, and catchy. The chorus should be simple and addictive, turning heartbreak and anxiety into a melodic hook.
```

**Avoid:** overly technical rap, dense poetry, cheerful pop gloss, long unsingable lines.

---

## genre.conscious_jazz_rap

**Use when user says:** Kendrick Lamar, conscious rap, jazz rap, political rap, concept rap, literary hip-hop.

**Tempo:** 78–100 BPM for narrative/jazz rap; can vary widely by section.

**Groove:** live-feeling drums, funk pocket, jazz swing, West Coast bounce, or deliberately sparse cinematic beat.

**Drums:** live kit or sampled drums, percussion layers, groove variations, sometimes minimal percussion for spoken-word intensity.

**Bass:** electric bass, upright-like movement, funk/jazz basslines, or tight 808 depending on era lane.

**Harmony:** jazz, funk, soul, modal colors, unexpected changes; can support spoken-word or narrative scenes.

**Vocal:** highly rhythmic rap, character voices, perspective shifts, spoken-word passages, intensity changes.

**Lyric posture:** social critique, moral conflict, autobiography, inner dialogue, community, faith, trauma, accountability.

**MiniMax prompt fragment:**

```text
A cinematic conscious jazz-rap track in a Kendrick Lamar lane, blending West Coast hip-hop with live-feeling jazz, funk, and soul textures. The beat should leave space for detailed storytelling, perspective shifts, and spoken-word intensity, with bass and drums reacting dynamically rather than looping flatly.
```

**Avoid:** vague activism slogans, generic “deep” lines, no hook, no musical movement.

---

## genre.rage_rap_opium_synth

**Use when user says:** Playboi Carti, rage, Opium, Ken Carson, Destroy Lonely, hypertrap, punk trap.

**Tempo:** 140–170 BPM.

**Groove:** aggressive trap bounce, relentless energy, distorted synth riffs, mosh-pit feel.

**Drums:** hard trap drums, distorted 808s, bright digital hats, compressed impact.

**Bass:** saturated 808s, aggressive sub, sometimes clipping/distorted edge.

**Harmony:** bright saw/square synth riffs, minimal chord movement, video-game/sci-fi color, minor or modal vamp.

**Vocal:** phrase-based, repetitive, high-energy, ad-lib-heavy, sometimes high-pitched or rasped; persona over dense lyricism.

**Lyric posture:** flex, chaos, alien confidence, punk attitude, minimal text with high sound value.

**MiniMax prompt fragment:**

```text
A high-energy rage-rap track in the Playboi Carti/Opium lane, with distorted 808s, bright serrated synth riffs, compressed trap drums, and a punk mosh-pit feeling. The vocal should be repetitive, ad-lib-heavy, phrase-based, and more about energy and persona than dense storytelling.
```

**Avoid:** thoughtful slow verses, acoustic instrumentation, overly clean pop mixing.

---

## genre.cloud_rap_ethereal

**Use when user says:** cloud rap, dreamy rap, ambient trap, Lil B/A$AP Rocky cloud-lane, ethereal SoundCloud.

**Tempo:** 65–85 half-time or 130–160 double-time.

**Groove:** relaxed trap/rap pocket, less aggressive hats, floating beat.

**Drums:** soft 808s, smeared snares, airy hats.

**Bass:** rounded sub, not too punchy.

**Harmony:** pads, plucks, vaporous synths, reverb-heavy samples, dreamlike loops.

**Vocal:** laid-back rap, melodic fragments, ad-libs drenched in reverb/delay.

**Lyric posture:** luxury, dissociation, space, memory, style, melancholy flex.

**MiniMax prompt fragment:**

```text
A dreamy cloud-rap track with hazy pads, soft 808s, relaxed trap drums, and reverb-heavy vocal layers. The rap should feel laid-back and atmospheric, with melodic fragments and a floating hook over a vaporous minor-key loop.
```

---

## genre.west_coast_gfunk_modern

**Use when user says:** West Coast rap, G-funk, California rap, lowrider, modern West Coast bounce.

**Tempo:** 85–105 BPM.

**Groove:** laid-back bounce, swing, pocketed drums, rideable bass.

**Drums:** crisp claps/snares, funky percussion, sometimes live-feeling or 808-assisted.

**Bass:** melodic synth bass, Moog-like lines, elastic low end.

**Harmony:** funk chords, talkbox/synth lead, sunny or menacing California color.

**Vocal:** confident rap, conversational swagger, call-response hooks.

**MiniMax prompt fragment:**

```text
A modern West Coast hip-hop track with a laid-back G-funk bounce, crisp claps, elastic melodic bassline, and warm synth leads. Keep the rap confident and conversational, with a hook that feels like a ride-through-the-city anthem.
```
