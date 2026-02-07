var DJMixer = {};

DJMixer.init = function (id, debugging) {
}

DJMixer.shutdown = function () {
}

// When the Master Volume Gain is turned, this function is called.
// It sends a MIDI value (0 to 127), representing the Volume Level.
// It sends a MIDI message to Channel 1, Change Control 7.
// This MIDI message is checked by Raspbery Pi Pico [VolumeLED.py] code.
const masterVolumeGainCallback = function (value, group, control) {
    // Mixxx DJ software middle and maximum Master Volume gain values.
    const midGainValue = 1.0;
    const maxGainValue = 5.011872336272724;

    // Normalise the Master Volume gain to a value between 0 and 1 (floating point).
    // It is logarithmic, so we regard the middle value as less than 50% of the range.
    let normalisedGain =
        (value <= midGainValue)
            // 0 → 0.0, 1.0 → 0.5
            ? (value / (2 * midGainValue))
            // 1.0 → 0.5, 5.0 → 1.0
            : (0.5 + (value - midGainValue) / (2 * (maxGainValue - midGainValue)));

    // Set the MIDI Value (0 → 127) based on the Normalised Gain Value (0.0 → 1.0).
    let midiValue = Math.min(127, Math.max(0, Math.round(normalisedGain * 127)));

    // Update the Raspberry Pi Pico [VolumeLED.py] so it can light the LEDs according to the volume.
    midi.sendShortMsg(176, 7, midiValue);
};

// Connect the Master Gain Volume Mixxx knob to this callback function.
const syncVolumeGain = engine.makeConnection('[Master]', 'gain', masterVolumeGainCallback);


