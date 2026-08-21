---
id: DJMixer
chapter: 04
title: Solution strategy
status: partial
confidence: low
last_verified: 2026-08-20
verified_by: unverified
---

# 4. Solution strategy

DJ Mixer's design is shaped by two things: it has to speak Mixxx's language, and it has to
stay simple enough for one person to build, wire and reason about on a single microcontroller.

- **Bridge to Mixxx exclusively through its documented MIDI controller-scripting mechanism.**
  Mixxx exposes no other integration surface, so every physical control's behaviour is
  expressed as a MIDI CC or Note message rather than any richer or more direct API. This keeps
  the integration simple to build but caps what the controller can ever influence - only what
  MIDI can carry.
  Traces to: chapter 2 constraint "Must integrate with Mixxx via its documented MIDI
  controller-scripting mechanism (JS + XML mapping)"

- **Drive every input through one continuous, non-blocking polling loop rather than
  interrupts.** A single loop calling `monitor()` on each component keeps the firmware's
  control flow easy to follow on constrained hardware, at the cost of responsiveness being
  bounded by how long every component's `monitor()` call takes, since nothing can pre-empt
  another component mid-loop.
  Traces to: chapter 1 quality goal "Performance efficiency"

## Open strategy questions

- **Question:** Was an interrupt-driven or event-based architecture considered and rejected, or was polling simply the default starting point?
  Why it matters: it directly bounds how responsive the controller can ever be, which is the system's only stated performance concern.
  Next step / owner: unknown - ask the original builder.

## Open questions for SME

- [ ] No record exists of either strategic choice being deliberated - both are read from the code's shape alone (CPT-004, CPT-005), not from any design note.

## Provenance & confidence log

| Claim | Source | Confidence | Evidence |
|---|---|---|---|
| Integration is via Mixxx's MIDI scripting mechanism only | code | high | CTX-009 |
| Polling loop drives responsiveness trade-off | inferred | low | CPT-001, CTX-006 |
