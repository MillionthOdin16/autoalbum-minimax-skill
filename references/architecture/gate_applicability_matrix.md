# Gate Applicability Matrix

The skill aims for professional quality without wasting effort or forcing album-only artifacts onto single-track or packet-only projects. This matrix determines which gates are required.

Legend:

- **R** = Required
- **C** = Conditional / required when risk or style/output goal calls for it
- **O** = Optional quality escalation
- **S** = Skip unless user specifically asks

## By scope/output goal

| Gate | single_track packet_only | lead_single | EP/mixtape | album/concept_album | cover/rerender | render_review_only | release_package |
|---|---:|---:|---:|---:|---:|---:|---:|
| Intent/config | R | R | R | R | R | R | R |
| Concept tournament | C | C | R | R | S | S | C |
| Style resolution | C | C | C | C | C | S | C |
| Style/voice trials | C | R | R | R | C | S | C |
| Foundation | C | R | R | R | C | S | C |
| Album canon | C | C | R | R | C | S | R |
| Tracklist/arc | S | C | R | R | S | S | R |
| Track style card | R | R | R | R | C | S | R |
| Motif plant/payoff ledger | S | C | R | R | S | S | R |
| Hook/title tournament | C | R | R for key tracks | R for key tracks | S | S | C |
| Hook/form/energy review | R | R | R | R | C | S | C |
| Lyric/songcraft evaluation | R for vocal | R for vocal | R for vocal | R for vocal | C | S | C |
| Prosody/topline | R for vocal | R for vocal | R for vocal | R for vocal | C | S | C |
| Preproduction brief | R | R | R | R | C | S | C |
| Adversarial song/preproduction edit | C | R | R | R | C | S | C |
| MiniMax packet compilation | R unless review-only | R | R | R | C | S | C |
| Prompt budget/compression | R | R | R | R | C | S | C |
| Adversarial prompt/packet edit | C | R | R | R | C | S | C |
| Packet/style/parameter evaluation | R | R | R | R | C | S | C |
| Unified evaluation | R | R | R | R | C | C | R |
| Variants | C | R | R for key tracks | R for key tracks | C | S | C |
| Payload/render logistics | C | C | C | C | C | S | C |
| Candidate comparison | S unless rendered | R if rendered | R if rendered | R if rendered | R if rendered | R | R |
| Listener panel | O | C | C | C | O | C | R for major release |
| Post-audio rebuild | S | S | R if multiple tracks | R if multiple tracks | S | S | R |
| Final audio QC | S | C | C | C | C | C | R |
| Executive producer loop | S | C | C | R | S | C | R |
| User-story fit check | R | R | R | R | R | R | R |

## Quality mode overrides

### scratch

May skip concept tournament, listener panel, executive producer loop, post-audio rebuild, and final audio QC unless user asks.

### high_rigor

Enable concept tournament for vague concepts, style/voice trials for style-sensitive projects, hook tournament for lead/key tracks, adversarial passes, and unified evaluation.

### release_grade

Require all applicable high-rigor gates plus candidate comparison, final audio QC, user-story fit check, and executive producer review loop.

### style_strict

Available as a `quality_mode`. Require style resolution, style/voice trials, style cards, style-fidelity evaluation, and style-purist listener panel when renders exist.

### packet_only

Stop after approved generation packets, prompt-budget report, packet/style/parameter evaluation, and user-story fit. Do not require render review, post-audio rebuild, final audio QC, or release metadata unless requested.

## Risk triggers

Run additional gates when any risk trigger appears:

- user asks for “best possible,” “professional,” “major release quality,” or “as close as possible” style fidelity;
- style reference is specific artist/song/era/producer;
- hook, chorus, or title feels generic;
- lyrics read like poetry rather than performance text;
- prompt exceeds ideal density or contains too many controls;
- two adjacent tracks feel similar;
- render does not follow lyrics/structure/style;
- revisions change upstream artifacts.


## Controller interpretation

The machine-readable source of truth is `references/controller/phase_applicability.json`. This markdown file is explanatory. If the two disagree, update the JSON first and then mirror the explanation here.

Conditional (`C`) does not mean optional decoration. It means the agent must decide whether the risk trigger applies. If the user asks for professional quality, specific style fidelity, a release package, or major-artist-grade output, most conditional quality gates should be treated as active.


## Applicability precedence

Controller applicability is resolved in this order: project scope baseline → quality-mode escalation → output-goal override. Output goal is applied last so packet-only, review-only, or candidate-only projects do not accidentally require release-stage artifacts just because the quality mode is strict.
