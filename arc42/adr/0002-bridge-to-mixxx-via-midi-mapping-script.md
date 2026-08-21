---
status: accepted
date: unknown
decision-makers: [unknown]
consulted: []
informed: []
provenance: inferred
confidence: low
---

# Bridge to Mixxx via a MIDI mapping script rather than a native plugin

## Context and problem statement

No record of this decision was found; this is a reading of the solution structure and should
be confirmed by an SME. The controller needed some way to influence Mixxx DJ Software's
internal state (gain, crossfader, PFL) from external hardware.

## Decision drivers

- Mixxx exposes a documented MIDI controller-scripting API (JS + XML mapping)
- No native/compiled Mixxx plugin exists in the staged material

## Considered options

- No alternatives were recorded.

## Decision outcome

Chosen option: "MIDI controller-scripting mechanism", because `DJMixer.js` and
`DJMixer.midi.xml` are staged, using exactly Mixxx's documented scripting mechanism, with no
trace of any alternative integration approach.

### Consequences

- Good, because no changes to Mixxx's own source are required, and the mechanism is
  officially supported.
- Bad, because the integration is limited to whatever the MIDI scripting API exposes - no
  deeper access to Mixxx's internals is possible.

### Confirmation

Not evidenced.

## Pros and cons of the options

### MIDI controller-scripting mechanism

- Good: Officially supported, no Mixxx source changes needed
- Neutral: Requires exact agreement between the JS/XML mapping and the firmware's hardcoded
  MIDI addresses (see concept 8.3)
- Bad: Limited to the MIDI vocabulary Mixxx's scripting API exposes
