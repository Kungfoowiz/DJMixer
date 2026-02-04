import digitalio
import microcontroller
import usb_midi


class MidiButton:
    def __init__(self, pin: microcontroller.Pin, midiChangeControl: int, midiChannel: int):
        # Configure button as input with internal pull‑up
        self.button = digitalio.DigitalInOut(pin)
        self.button.switch_to_input(pull=digitalio.Pull.UP)

        # MIDI note number for this button
        # Store the Control Change (CC) number (standard for buttonss)
        self.midiChangeControl: int = midiChangeControl
        # MIDI status byte for Note On/Off on this channel
        self.statusChannel = 0x90 + (midiChannel - 1)
        # Reference index [1] of the ports, which is the standard 'MIDI Out' to computer
        self.midiOut = usb_midi.ports[1]

        # Tracks last physical state (True = not pressed)
        self.lastState = True

        
    def monitor(self) -> None:
        # Read current button state.
        currentState = self.button.value

        # Only act when state changes.
        if currentState == self.lastState:
            return

        # Button pressed.
        if currentState == True:
            velocity = 0
        # Button depressed.
        else :
            velocity = 127

        # DEBUG.
        # print("MIDI Change Control " + str(self.midiChangeControl))
        # print("----")
        # print("Current State is " + str(currentState))
        # print("Last State was " + str(self.lastState))
        # print("Velocity is " + str(velocity))
        # print("----")

        # Save the last state to check if it changes on next button press.
        self.lastState = currentState

        # Write the raw bytes specifically to the MIDI Out port.
        message = bytes([self.statusChannel, self.midiChangeControl, velocity])
        self.midiOut.write(message)

