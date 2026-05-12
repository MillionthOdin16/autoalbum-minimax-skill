
# V23 Verification Hardening Plan

This upgrade closes the failure modes discovered from a real v22 output project.

## Problems addressed

- File-existence gates passed while artifacts were stale or schema-invalid.
- Reviews quoted lyrics that were not present in the current lyric file.
- Style resolution named non-catalog project artifacts as catalog files.
- Scope-specific runs inherited album-only criteria.
- Tournaments selected lower-scoring winners without explicit overrides.
- Variants were deltas instead of renderable generation packets.
- Completion reports summarized success instead of trying to break the output.
- Prompt budget checks used the wrong provider limit model.

## New standard

A phase is complete only when required artifacts are:

1. present,
2. valid JSON/JSONL when applicable,
3. valid against known schemas,
4. current relative to the source artifact hashes they reviewed,
5. grounded in exact quotes when they criticize lines,
6. style-catalog grounded when a style is selected,
7. renderable if they are generation packets or variants,
8. independently verified at lyric, packet, and completion gates.

## Score caps

Objective failures cap scores regardless of prose praise:

- stale review: reviewed dimension max 4.0;
- quoted line missing from current artifact: reviewer score max 3.0;
- non-renderable variant: packet readiness max 5.0;
- invalid style catalog references: style resolution max 5.0;
- prompt lint blocker: MiniMax readiness max 6.0;
- clunky/nonsensical hook or first-verse line: lyric quality max 7.4;
- state says `not_started` after packets exist: completion fit max 6.0.
