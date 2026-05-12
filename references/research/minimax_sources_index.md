# MiniMax Sources Index

This file records the sources used to construct the embedded MiniMax references. Check these sources again when updating the skill.

## Primary / official

- MiniMax API Docs: Music Generation endpoint. Documents `/v1/music_generation`, model choices, prompt/lyrics rules, structure tags, stream/output_format, lyrics_optimizer, is_instrumental, cover inputs, cover_feature_id, and response metadata.
- MiniMax API Docs: Music Generation guide. Documents text-to-song, lyrics-generation example, one-step cover, and two-step cover workflows.
- MiniMax official GitHub skill: `minimax-music-gen`. Documents `mmx` CLI usage, structured CLI flags, agent flags, basic/advanced modes, and cover commands.
- MiniMax official prompt guide. Documents vivid English sentence prompts, vocal descriptions, production details, BPM references, and genre/style vocabulary.
- MiniMax Music 2.6 product page. Documents public UI capabilities such as prompt/lyrics limits, structure tags, audio settings, instrumental mode, lyrics optimizer, cover mode, max song length, and export formats.

## Wrapper/provider references

- Replicate `minimax/music-2.6` schema.
- Cloudflare Workers AI `minimax/music-2.6` docs.
- fal.ai MiniMax Music 2.6 docs.
- AIMLAPI MiniMax Music 2.6 docs.

Use wrapper references only for that wrapper. Prefer direct MiniMax API docs for canonical behavior.

## Update rule

When MiniMax changes the API or the selected provider route changes:

1. Update `references/api/minimax_music_2_6_full_api_reference.md`.
2. Update provider capability matrix.
3. Update generation and cover schemas.
4. Update payload-export delegated prompt.
5. Add a changelog entry.


## Additional sources

- MiniMax direct API reference: https://platform.minimax.io/docs/api-reference/music-generation
- MiniMax official music generation guide: https://platform.minimax.io/docs/guides/music-generation
- MiniMax prompt guide: https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-music-gen/references/prompt_guide.md
- MiniMax music skill / mmx CLI guidance: https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-music-gen/SKILL.md
- MiniMax Music 2.6 feature page: https://www.minimax-music.com/minimax-music-2-6
- Luminate R&B/Hip-Hop streaming share context: https://luminatedata.com/blog/how-rb-hip-hop-streaming-share-could-get-its-groove-back/
- Apple Music U.S. Hip-Hop/Rap current chart mirror: https://www.top-charts.com/songs/hip-hop-rap/united-states/apple-music
- Album sequencing craft: https://matlefflerschulman.com/mastering-articles/how-to-sequence-an-album
- Energy map / tension craft: https://www.edmprod.com/tension/
- Berklee chord progression craft: https://online.berklee.edu/takenote/8-tools-to-richer-chord-progressions/
- Berklee bridge craft: https://online.berklee.edu/takenote/writing-bridges-for-your-songs-can-be-much-easier/


## Additions
- MiniMax direct API: confirms models, prompt/lyrics constraints, structure tags, `stream`, `output_format`, `audio_setting`, `lyrics_optimizer`, `is_instrumental`, cover inputs, URL expiration, and response metadata.
- MiniMax prompt guide: confirms vivid English prose over comma-separated tags.
- MiniMax Music 2.6 release note: emphasizes tension, stops/restarts, dramatic architecture, and improved musical control.
- Replicate/WaveSpeed/fal/Runware provider docs: useful for wrapper-specific controls, seed/queue behavior, structure tag variants, and cover output-format behavior. Treat wrapper claims as provider-specific, not universal direct API truth.
