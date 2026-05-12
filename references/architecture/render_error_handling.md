# Render Error Handling

## Purpose
Define failure states and recovery actions for MiniMax/API render operations so the agent does not lose work, silently skip failed generations, or mislabel incomplete renders as candidates.

## Required render statuses

```text
QUEUED
SUBMITTED
COMPLETED_RESPONSE_RECEIVED
DOWNLOADED
DOWNLOAD_VERIFIED
FAILED_INVALID_PAYLOAD
FAILED_PROVIDER_REJECTED
FAILED_TIMEOUT
FAILED_EXPIRED_URL
FAILED_DOWNLOAD
FAILED_CORRUPT_FILE
FAILED_UNKNOWN
RETRY_SCHEDULED
ABANDONED_WITH_REASON
```

## Required recovery policy
- Invalid payload: repair packet/payload, do not retry blindly.
- Provider rejection: inspect response, revise prompt/lyrics/fields, record rejected payload.
- Timeout: retry once with same payload, then mark provider instability if repeated.
- Expired URL: regenerate or request new render; do not claim candidate exists.
- Download failure: retry immediately; verify checksum after download.
- Corrupt file: mark failed, keep response archive, regenerate candidate.
- Unknown failure: record full response, block release readiness until resolved.

## State requirement
Every failed render must create a render-log entry and a state event. A track cannot be marked reviewed if its selected audio is not `DOWNLOAD_VERIFIED`.
