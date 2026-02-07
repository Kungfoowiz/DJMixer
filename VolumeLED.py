import usb_midi
import board, digitalio

class VolumeLED:
    def __init__(self):
        # Setup GP0 to GP2 as LED outputs.
        self.led0 = digitalio.DigitalInOut(board.GP0) 
        self.led0.direction = digitalio.Direction.OUTPUT

        self.led1 = digitalio.DigitalInOut(board.GP1)
        self.led1.direction = digitalio.Direction.OUTPUT

        self.led2 = digitalio.DigitalInOut(board.GP2)
        self.led2.direction = digitalio.Direction.OUTPUT

        # TEST.
        # self.led3 = digitalio.DigitalInOut(board.GP3)
        # self.led3.direction = digitalio.Direction.OUTPUT

        # self.led4 = digitalio.DigitalInOut(board.GP4)
        # self.led4.direction = digitalio.Direction.OUTPUT

        # Standard MIDI In
        self.midi = usb_midi.ports[0]

    def monitor(self):
        midiMessage = self.midi.read()

        # Invalid MIDI message.
        if not midiMessage or len(midiMessage) < 3:
            return
        
        # Get the MIDI Status, Change Control and Value.
        midiStatus = midiMessage[0]
        midiChangeControl = midiMessage[1]
        midiValue = midiMessage[2]

        # MIDI Channel 1 (0xB0 / 176), Change Control 7 (0x07 / 7).
        if midiStatus == 176 and midiChangeControl == 7:
            # DEBUG
            # print("MIDI Status = " + str(midiStatus) + 
            # " MIDI Change Control = " + str(midiChangeControl) + 
            # " MIDI Value = " + str(midiValue))

            # Find the MIDI percent (1 → 10)
            midiPercent = int((midiValue / 127) * 100)

            self.led0.value = midiPercent > 0
            self.led1.value = midiPercent > 33
            self.led2.value = midiPercent > 66

