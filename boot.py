# boot.py -- runs before main.py on MicroPython
# Keep this file minimal. Add board initialization here if needed.

# Example: disable automatic REPL on UART0 (uncomment to use)
# import sys
# sys.stdin = None
# sys.stdout = None
# sys.stderr = None

import usb_midi

# This sets the MIDI-specific interface name
usb_midi.set_internal_name("DJ Mixer")

