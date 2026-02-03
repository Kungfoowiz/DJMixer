import board # Access physical pin names
from MidiKnob import MidiVolumeKnob # Import your custom class

# Create the knob: Pin A0 [GP26 / Pin 31], MIDI Change Control #7 (Volume), MIDI Channel 1
mainVolumeKnob: MidiVolumeKnob = MidiVolumeKnob(board.A0, 7, 1)

# Main loop
while True:
    # Main Volume Knob.
    # Continuously check the physical knob for movement
    mainVolumeKnob.monitor()
