
# Delegated: Completion Adversarial Audit

## Task
Before claiming the project complete, try to disprove completion.

## Output
Write `reviews/completion_adversarial_audit.md`.

## Required questions
- Does `state.json` match the actual artifacts?
- Does `project_manifest.json` include the current files?
- Do all JSON artifacts validate against known schemas?
- Are any reviews stale relative to current source hashes?
- Do any reviews quote lines that do not exist?
- Did style resolution use actual catalog files?
- Are tournaments internally consistent or explicitly overridden?
- Are variants complete renderable packets?
- Are provider-ready API payloads exported when the output goal requires them?
- Does the prompt contain lint blockers such as non-English characters in an English-only project?
- Does the completion claim exactly match the user's requested output goal?

## Pass/fail
Fail if any blocker remains unresolved or hidden behind a positive summary.
