# Fragility Register

This register captures known weak points and the required mitigation.

## 1. Style-card / tracklist circularity
Risk: style cards need track roles, while track planning needs style cards.
Mitigation: two-pass planning. Create skeleton tracklist first, then style cards, then refined tracklist.

## 2. Packet-only vs completed-album confusion
Risk: agent declares an album complete when only prompts/lyrics exist.
Mitigation: distinguish output_goal: minimax_ready_packets, generated_candidates, selected_album_sequence, release_package.

## 3. Single-track bloat
Risk: user asks for one song and agent creates album-only artifacts.
Mitigation: project_scope modes; single_track uses compact foundation and one-song arc.

## 4. Generic style collapse
Risk: “rap,” “R&B,” or artist requests become generic prompts.
Mitigation: style request protocol, strictness, style cards, non-confusion rules, style-fidelity eval.

## 5. Overloaded MiniMax prompts
Risk: prompt becomes a compressed world bible.
Mitigation: prompt compiler keeps vivid creative brief under 2000 chars with only audible controls.

## 6. Lyrics that read well but sing poorly
Risk: poetic density harms generation.
Mitigation: songcraft eval must check line length, breath, vowel shape, hook repeatability, section contrast.

## 7. Unused API controls
Risk: stream/output_format/audio_profile/instrumental/optimizer/cover fields are ignored.
Mitigation: MiniMax parameter audit must mark every parameter used, unsupported, or intentionally omitted.

## 8. Current-style staleness
Risk: current rap or pop profiles become outdated.
Mitigation: refresh when project depends on currentness; preserve source date and confidence.

## 9. Over-constrained rendering
Risk: hard constraints overwhelm MiniMax and flatten results.
Mitigation: split hard constraints vs soft guidance; use variants to explore.

## 10. Under-reviewed render selection
Risk: first acceptable render is kept.
Mitigation: candidate comparison and post-generation review required for completed albums.

## 11. Reference policy drift
Risk: configuration contradicts user’s desired strict style adherence.
Mitigation: preserve raw references and use style strictness to control how aggressively the fingerprint is encoded.

## 12. Release packaging before audio exists
Risk: public-facing materials are built around hypothetical songs.
Mitigation: release_package_only requires selected renders; otherwise produce a draft release plan only.
