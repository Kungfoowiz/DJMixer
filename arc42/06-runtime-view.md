---
id: DJMixer
chapter: 06
title: Runtime view
status: assessed
confidence: high
last_verified: 2026-08-20
verified_by: unverified
---

# 6. Runtime view

## 6.1 Scenario: DJ adjusts master volume

The DJ turns the physical gain knob; Mixxx applies the new gain and echoes it back so the
LEDs reflect the current level.

- *Intention:* Change the audible output level and show it on the LEDs.
- *Trigger:* DJ turns the Master Volume Gain knob.
- *Participants:* DJ, MidiKnob, Mixxx DJ Software, DJMixer (Mixxx Controller Script), VolumeLED.

```mermaid
sequenceDiagram
    autonumber
    actor dj as DJ
    participant knob as MidiKnob
    participant mixxx as Mixxx DJ Software
    participant script as DJMixer (Mixxx Controller Script)
    participant led as VolumeLED
    dj->>knob: turn gain knob
    knob->>mixxx: MIDI CC7 value
    mixxx->>script: gain engine callback fires
    script->>mixxx: normalise gain to 0-127
    mixxx->>led: MIDI CC7 (echoed)
    led-->>dj: light 0-3 LEDs
```

**Exceptions and alternatives:**

- No failure or disconnect handling is implemented anywhere in this flow (STR-U01). If the
  USB link drops mid-turn, the knob's last-known value is simply never sent again once
  reconnected until it changes further - there is no resync.

## 6.2 Scenario: DJ engages headphone cue

The DJ presses a cue button; Mixxx routes that channel to the headphone output.

- *Intention:* Preview a channel privately before mixing it in.
- *Trigger:* DJ presses Headphone Cue Button 1 or 2.
- *Participants:* DJ, MidiButton, Mixxx DJ Software.

```mermaid
sequenceDiagram
    autonumber
    actor dj as DJ
    participant button as MidiButton
    participant mixxx as Mixxx DJ Software
    dj->>button: press cue button
    button->>mixxx: MIDI Note On (note 20 or 21, velocity 127)
    dj->>button: release cue button
    button->>mixxx: MIDI Note Off (velocity 0)
```

**Exceptions and alternatives:**

- No failure or disconnect handling is implemented (STR-U01). A dropped Note Off message
  would leave Mixxx believing the button is still held, with no correction mechanism.

## Open questions for SME

- [ ] Is the lack of any resync/recovery behaviour after a USB disconnect an accepted limitation, or an actual gap worth fixing?

## Provenance & confidence log

| Claim | Source | Confidence | Evidence |
|---|---|---|---|
| Master volume flow sequence | code | high | STR-008 |
| Headphone cue flow sequence | code | high | STR-009 |
| No failure/recovery handling exists | code | high | STR-U01 |
