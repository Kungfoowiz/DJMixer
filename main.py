import board

from MidiKnob import MidiKnob # Import your custom class
from MidiButton import MidiButton # Import your custom class

from VolumeLED import VolumeLED

# Master Volume Gain Knob: Pin A0 [GP26 / Pin 31], MIDI Change Control #7 (Volume), MIDI Channel 1
mainVolumeKnob: MidiKnob = MidiKnob(board.A0, 7, 1)

# Headphone Cue Button 1 on GP14, MIDI Change Control #20, MIDI Channel 1
headphoneCue1: MidiButton = MidiButton(board.GP14, 20, 1)
# Headphone Cue Button 2 on GP15, MIDI Change Control #21, MIDI Channel 1
headphoneCue2: MidiButton = MidiButton(board.GP15, 21, 1)

# Crossfader: Pin A1 [GP27 / Pin 31], MIDI Change Control #8 (Volume), MIDI Channel 1
crossfader: MidiKnob = MidiKnob(board.A1, 8, 1)

# Volume LEDs.
volumeLED = VolumeLED()

# Main loop
while True:
    # Main Volume Knob.
    # Continuously check the physical knob for movement.
    mainVolumeKnob.monitor()

    # Headphone Cue Buttons.
    # Continuously check the physical buttons for presses.
    headphoneCue1.monitor()
    headphoneCue2.monitor()

    # Crossfader.
    # Continuously check the physical fader for movement.
    crossfader.monitor()

    # Volume LEDs.
    # Continuously check for Master Gain Volume messages from DJ Mixx.
    volumeLED.monitor()


