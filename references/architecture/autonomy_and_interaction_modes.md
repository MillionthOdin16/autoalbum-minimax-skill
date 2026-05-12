# Autonomy and Interaction Modes

AutoAlbum should be useful both for users who want full automation and users who want creative checkpoints. The default is autonomous execution.

## Modes

### autonomous_full_pipeline
Use when the user asks for a full track, EP, or album. Make sensible defaults, document assumptions, and proceed.

### collaborative_checkpoints
Use only when the user asks to approve concepts, style, lyrics, renders, or sequence. Suggested checkpoints: seed, style map, tracklist, first renders, final sequence.

### packet_only
Use when the user wants MiniMax-ready prompts/lyrics/payloads but does not expect audio generation inside the current run.

### render_review_only
Use when the user supplies generated audio or render metadata for critique, selection, or regeneration.

### release_package_only
Use when selected audio already exists and the user needs final metadata, credits, sequence, cover direction, and public-facing materials.

## Clarification rule
Ask a question only when not asking would materially damage the result. Otherwise infer and document.

Examples of safe assumptions:
- Direct MiniMax API unless provider is specified.
- English style prompt.
- 44.1 kHz / high bitrate candidate profile.
- 10 tracks for a standard album; 5 for EP; 1 for track.

Examples that may require clarification:
- explicit vocal gender or language when central to user intent,
- whether existing user lyrics may be rewritten,
- whether to use supplied audio as cover source,
- whether explicit content is desired when genre conventions conflict with user context.
