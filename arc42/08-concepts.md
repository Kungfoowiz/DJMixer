---
id: DJMixer
chapter: 08
title: Concepts
status: assessed
confidence: high
last_verified: 2026-08-20
verified_by: unverified
---

# 8. Concepts

Three patterns recur across DJ Mixer's firmware and integration script and should be followed
consistently if the system is extended.

## 8.1 Continuous polling loop

The firmware has no interrupts or callbacks - one loop drives everything.

### Rules

- Every component exposes a parameterless `monitor()` method.
- `monitor()` must return quickly and never block, since every component shares one loop.

### Implementation

- `main.py`'s `while True` loop calls `monitor()` on each of MidiKnob (x2), MidiButton (x2)
  and VolumeLED in sequence.

### Where it shows up

- Building block: Pico Firmware (CircuitPython)
- Scenario: 6.1 DJ adjusts master volume
- Scenario: 6.2 DJ engages headphone cue

## 8.2 Change-only MIDI emission

Both the knob and button components track their last-sent value and only emit a MIDI
message when it actually changes.

### Rules

- A knob only sends when the change exceeds `potentiometerSensitivity` (jitter guard).
- A button only sends on an actual state transition, never on a steady state.

### Implementation

- `MidiKnob.potentiometerLastValue` and `MidiButton.lastState`, compared on every
  `monitor()` call.

### Configuration

- `potentiometerSensitivity` (default 2) controls how large a knob movement must be before
  it is treated as real rather than jitter - see chapter 7 for where it is set.

### Where it shows up

- Building block: MidiKnob
- Building block: MidiButton
- Scenario: 6.1 DJ adjusts master volume

## 8.3 Fixed MIDI channel/CC mapping

Every physical control's MIDI address is hardcoded and must be mirrored exactly on the
Mixxx side.

### Rules

- A physical control's MIDI channel and CC/note number is fixed at construction time in
  `main.py` and must match `DJMixer.midi.xml` exactly.
- Changing one side without the other silently breaks that control, with no error raised.

### Implementation

- `main.py` constructor arguments <-> `AppData/Local/Mixxx/controllers/DJMixer.midi.xml`.

### Where it shows up

- Building block: Pico Firmware (CircuitPython)
- Building block: DJMixer (Mixxx Controller Script)
- Decision: ADR-0002 (see chapter 9)

## Open questions for SME

- [ ] Is silent breakage on a mapping mismatch (concept 8.3) an accepted risk, or should the firmware validate its own mapping against something at boot?

## Provenance & confidence log

| Claim | Source | Confidence | Evidence |
|---|---|---|---|
| Continuous polling loop concept | code | high | CPT-001 |
| Change-only MIDI emission concept | code | high | CPT-002 |
| Fixed MIDI channel/CC mapping concept | code | high | CPT-003 |
