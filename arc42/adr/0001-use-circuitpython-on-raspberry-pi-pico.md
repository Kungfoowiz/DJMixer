---
status: accepted
date: unknown
decision-makers: [unknown]
consulted: []
informed: []
provenance: inferred
confidence: low
---

# Use CircuitPython on Raspberry Pi Pico as the controller platform

## Context and problem statement

No record of this decision was found; this is a reading of the solution structure and should
be confirmed by an SME. A physical DJ control surface needed a microcontroller platform capable
of reading analog and digital inputs and speaking USB MIDI.

## Decision drivers

- Need to read potentiometers, buttons and drive LEDs from GPIO
- Need native USB MIDI support
- Hobbyist build, likely favouring low cost and easy firmware iteration

## Considered options

- No alternatives were recorded.

## Decision outcome

Chosen option: "CircuitPython on Raspberry Pi Pico", because the staged firmware is written
entirely in CircuitPython targeting Pico-specific pin names (`board.A0`, `board.GP14`, etc.).

### Consequences

- Good, because full control over pin mapping and MIDI behaviour was achieved with minimal
  code.
- Bad, because firmware install and updates are entirely manual - drag-and-drop onto a
  USB mass-storage drive, with no automation.

### Confirmation

Not evidenced - no test or validation process was found for this choice.

## Pros and cons of the options

### CircuitPython on Raspberry Pi Pico

- Good: Simple, readable Python-like firmware code
- Neutral: Requires the board to appear as a USB mass-storage device for programming
- Bad: No package manager or dependency management evidenced
