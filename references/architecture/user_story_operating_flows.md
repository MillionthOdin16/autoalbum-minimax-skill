# User Story Operating Flows

This file validates that AutoAlbum works for real users, not just idealized album-generation tasks. The agent must route every request through one of these flows.

## Universal intake questions the agent answers internally

```text
1. What is the user trying to receive: concept, lyrics, MiniMax packets, generated candidates, final sequence, release package, or critique?
2. Is the scope one track, a lead single, EP, full album, mixtape, instrumental project, cover/re-render, or revision?
3. Is a style/reference request present? If yes, how strict?
4. Does the request require current style research/catalog refresh?
5. Are lyrics needed, supplied, generated, revised, or disabled?
6. Is MiniMax rendering expected now, later, or outside the current environment?
7. What assumptions can be safely made without bothering the user?
```

## Story 1: User gives only an album concept

Example: “Make me a dark rap album about leaving home and becoming famous.”

Required flow:

```text
intent intake
→ project_config
→ style selection
→ album style map
→ foundation
→ skeleton tracklist
→ track style cards
→ refined tracklist
→ lyrics/songcraft
→ MiniMax packets
→ variants
→ parameter audit
→ generation plan
→ render review when audio exists
→ final sequence/release package
```

Pass condition: the user can start from a vague concept and receive a complete, generation-ready album project without needing to understand the pipeline.

Fragile areas to guard:
- broad style requests becoming generic,
- tracklist generated before style resolution,
- albums stopping at lyrics without MiniMax packets,
- no distinction between generation-ready and release-ready.

## Story 2: User asks for one track

Example: “Create a single in a melodic trap style about texting someone you should block.”

Required flow:

```text
intent intake
→ project_scope = single_track or lead_single
→ compact foundation
→ one track style card
→ lyrics
→ songcraft eval
→ MiniMax packet
→ variants
→ parameter audit
→ render/review if possible
```

Do not force album-only artifacts such as twelve-track arc, closer rationale, or first-three-track promise.

## Story 3: User asks for a specific artist or song lane

Example: “Track 4 should sound like current Playboi Carti rage rap.”

Required flow:

```text
preserve raw request
→ catalog profile lookup
→ currentness check if time-sensitive
→ artist/song fingerprint
→ adjacent-style differentiators
→ track style card
→ MiniMax prompt capsule
→ style fidelity eval
```

Pass condition: the output controls are specific enough that an evaluator can distinguish the requested lane from adjacent artists or subgenres.

## Story 4: User gives multiple styles for one album

Example: “Mostly R&B, but with one Memphis rap banger and one acoustic closer.”

Required flow:

```text
style selection
→ album_style_map with shared DNA
→ per-track style deltas
→ transition plan
→ non-confusion rules
→ style-fidelity eval per track
```

Pass condition: variety feels authored, not random. Shared DNA must be named and audible; deltas must be justified by album function.

## Story 5: User supplies lyrics

Example: “Here are my lyrics. Turn this into a MiniMax-ready single.”

Required flow:

```text
intent intake
→ preserve user lyrics
→ singability/structure check
→ optional revision brief
→ MiniMax tag formatting
→ style card
→ prompt packet
→ generation variants
```

Do not rewrite supplied lyrics unless the user requested improvement or the lyrics fail a MiniMax/singability gate. When rewriting, preserve the user’s central images and hook.

## Story 6: User supplies generated audio

Example: “Here are three MiniMax renders. Pick the best and tell me what to regenerate.”

Required flow:

```text
render_review_only mode
→ read packets/logs if available
→ candidate comparison
→ style and songcraft evaluation
→ keep/reject/regenerate decisions
→ regeneration briefs
→ sequence implications
```

Pass condition: the agent can decide based on audio evidence, not only prompt theory.

## Story 7: User wants a cover/re-render

Example: “Use this demo and make a harder club version.”

Required flow:

```text
cover_or_rerender scope
→ source audio registry
→ cover packet
→ source audio compliance check
→ one-step or two-step cover workflow
→ render log
→ post-cover review
```

Pass condition: source audio handling, cover_feature_id validity, lyric extraction/replacement, and style target are all explicit.

## Story 8: User wants a current-trend rap album

Example: “Make it sound like what is hot in rap right now.”

Required flow:

```text
refresh current rap catalog
→ select current lanes
→ style map
→ track cards
→ strict non-genericity checks
```

Pass condition: the catalog uses current evidence and does not default to outdated 2018 trap or generic rap signifiers.

## Story 9: User wants professional release package

Example: “Now make this ready to release.”

Required flow:

```text
selected renders present
→ final sequence
→ metadata
→ lyrics
→ credits
→ cover direction
→ liner notes
→ press release
→ final A&R review
```

Pass condition: no release package is declared final without selected audio and render metadata unless the user explicitly asks for a pre-render release plan.
