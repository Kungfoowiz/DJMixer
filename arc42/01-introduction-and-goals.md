---
id: DJMixer
chapter: 01
title: Introduction and goals
status: partial
confidence: low
last_verified: 2026-08-20
verified_by: unverified
---

# 1. Introduction and goals

DJ Mixer is a self-built physical control surface for the Mixxx DJ software. It lets a DJ
operate master volume, crossfading and headphone cue directly from physical knobs, a fader
and buttons, instead of the on-screen controls, while a strip of LEDs mirrors the current
volume level back to them.

## 1.1 Requirements overview

The most important requirements:

- A DJ can raise or lower the Mixxx master volume gain by turning a physical knob.
- A DJ can see the current master volume on three physical LEDs without looking at a screen.
- A DJ can blend between two channels using a physical crossfader.
- A DJ can privately preview either channel in headphones before mixing it in.

Explicit non-goals:

- Not stated in the available sources.

## 1.2 Quality goals

| Priority | Quality | Scenario (short) | Acceptance criteria |
| -------: | :------ | :--------------- | :------------------ |
|        1 | Performance efficiency | A DJ turns the gain knob during a live set | unknown — see open questions |
|        2 | Maintainability | A hobbyist follows the build guide to wire and flash their own unit | unknown — see open questions |

## 1.3 Stakeholders

| Stakeholder | Expectations |
| :---------- | :----------- |
| DJ / builder | A working, low-latency physical control surface for Mixxx |

## Open questions for SME

- [ ] No numeric responsiveness/latency target is stated anywhere in the staged material (CTX-U01) — is one expected, or is "no noticeable lag" the only bar?
- [ ] No stakeholder beyond the DJ/builder is named (CTX-U02) — are there others (e.g. other crew, a venue) this should account for?
- [ ] No explicit non-goal is recorded anywhere in the staged sources — is that a gap in documentation, or genuinely unbounded scope?
- [ ] `CTX-006` (responsiveness as a quality goal) is `source: inferred` from the existence of a polling loop, not from any stated requirement — worth an SME confirming this is actually a driving concern rather than an assumption.

## Provenance & confidence log

| Claim | Source | Confidence | Evidence |
|---|---|---|---|
| DJ can control master volume via a physical knob | code | high | CTX-001 |
| DJ can see volume on physical LEDs | code | high | CTX-002 |
| DJ can crossfade via a physical fader | code | high | CTX-003 |
| DJ can cue a channel privately in headphones | code | high | CTX-004 |
| No explicit non-goal stated | code | low | CTX-005 |
| Responsiveness is a quality driver | inferred | low | CTX-006 |
| Setup simplicity for a hobbyist builder is a quality driver | code | medium | CTX-007 |
| DJ/builder is the primary stakeholder | code | medium | CTX-008 |
