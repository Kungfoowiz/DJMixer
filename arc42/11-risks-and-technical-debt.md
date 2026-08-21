---
id: DJMixer
chapter: 11
title: Risks and technical debt
status: partial
confidence: high
last_verified: 2026-08-20
verified_by: unverified
---

# 11. Risks and technical debt

Risks are phrased as: *what could hurt us* + *why it matters* + *what we will do about it*.

| Risk / debt item | Why it matters | Mitigation / decision | Owner |
| :----------------- | :---------------- | :------------------------ | :----- |
| No app card or CMDB record exists for this system | Nothing about it is independently tracked; this analysis is the only record | Stage a manifest-row.yaml or app card if this needs programme-level tracking | unknown |

## Known technical debt

- No automated deployment for either the firmware or the Mixxx script → acceptable for a
  single hobbyist build today; revisit if this is ever distributed to other users — owner: unknown
- No health/liveness signal from either the firmware or the Mixxx script → acceptable at
  current scale; revisit if reliability during live sets becomes a reported problem — owner: unknown

## Open questions for SME

- [ ] Who, if anyone, owns this system going forward? No owner is named anywhere in the staged material.

## Provenance & confidence log

| Claim | Source | Confidence | Evidence |
|---|---|---|---|
| No app card/CMDB record exists | inferred | medium | CTX-010 |
| No automated deployment | code | high | RUN-007 |
| No health/liveness signal | code | medium | RUN-008 |
