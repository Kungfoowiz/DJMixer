---
id: DJMixer
chapter: 02
title: Architecture constraints
status: partial
confidence: high
last_verified: 2026-08-20
verified_by: unverified
---

# 2. Architecture constraints

Non-negotiables that shape the design space.

| Constraint | Type | Rationale | Impact on design | Reference |
| :--------- | :--- | :-------- | :--------------- | :-------- |
| Must integrate with Mixxx via its documented MIDI controller-scripting mechanism (JS + XML mapping) | integration | Mixxx is third-party software; this is the only extension point it exposes | Every physical control's behaviour must be expressible as a MIDI CC or Note message - no other transport or richer API is available | Mixxx DJ Software controller scripting API |

Notes:

- No exception path exists or is evidenced - the MIDI scripting boundary applies to every control without exception.
- Reference points to Mixxx's own scripting API, not a document staged in this repo.

## Open questions for SME

- [ ] Is the DJ's PC required to be Windows specifically? The `%LOCALAPPDATA%` install path implies it, but no OS constraint is stated anywhere (RUN-U01).
- [ ] Are there any licensing, safety or hobbyist-electronics standards this build is expected to follow? None were evidenced.

## Provenance & confidence log

| Claim | Source | Confidence | Evidence |
|---|---|---|---|
| Must integrate via Mixxx's MIDI controller scripting API | code | high | CTX-009 |
