import analogio  # Module to read analog voltage from pins
import usb_midi  # Module to send and receive MIDI data via USB
from microcontroller import Pin # Module to define specific hardware pins

class MidiVolumeKnob:
    # This runs once when you create the knob in code.py
    def __init__(self, pin: Pin, midiChangeControl: int, midiChannel: int):
        # Initialise the analog pin to read the potentiometer
        self.potentiometer = analogio.AnalogIn(pin)
        
        # Store the Control Change (CC) number (standard for knobs/faders)
        self.midiChangeControl: int = midiChangeControl
        
        # Calculate the Status Byte for Control Change (0xB0 is CC on Channel 1)
        self.statusChannel: int = 0xB0 + (midiChannel - 1)
        
        # Set initial value to -1 so the first reading always triggers an update
        self.potentiometerLastValue: int = -1
        
        # Reference index [1] of the ports, which is the standard 'MIDI Out' to computer
        self.midiOut = usb_midi.ports[1]

    # This runs repeatedly to check for knob movements
    def monitor(self) -> None:
        # Get the Potentiometer 16-bit pin value (0-65535) and convert to the 7-bit MIDI range (0-127)
        potentiometerValue: int = self.potentiometer.value // 512
        
        # Check if the knob has moved since the last check
        if self.potentiometerLastValue != potentiometerValue :
            # Create a 3-byte Control Change (CC) message.
            message: bytes = bytes([self.statusChannel, self.midiChangeControl, potentiometerValue])
            
            # Write the raw bytes specifically to the MIDI Out port.
            self.midiOut.write(message)
            
            # Save the last Potentiometer value, to compare on the next check.
            self.potentiometerLastValue = potentiometerValue

            print(potentiometerValue)

