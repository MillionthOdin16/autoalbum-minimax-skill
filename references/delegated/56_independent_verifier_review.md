
# Delegated: Independent Verifier Review

## Task
Review source artifacts as if written by someone else. Ignore previous scores and praise. Do not use earlier self-evaluations as evidence.

## Required verifier points
- Lyrics verifier: current lyrics, style card, prosody report, line polish report.
- Packet verifier: current prompt, current lyrics, generation packet, provider profile, prompt budget report.
- Completion verifier: project config, state, manifest, payloads, validators, reviews, and output goal.

## Output
Write the relevant file:
- `tracks/tr_NN/lyrics_verifier_review.json`
- `tracks/tr_NN/prompt_packet_verifier_review.json`
- `reviews/completion_verifier_review.json`

## Required evidence
Every blocker must cite a file path and exact evidence. Every quoted lyric/prompt line must exist in the current evaluated artifact.

## Authority
Verifier failure overrides self-evaluation pass. If self-eval says 8.7 but the verifier finds clunky hook lines, stale reviews, or invalid packets, the project is not ready.
