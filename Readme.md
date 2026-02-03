# DJ Mixer made with MicroPython and Raspberry Pi Pico
## [Click here to watch the DJ Mixer in action on Mixxx DJ Software](https://github.com/user-attachments/assets/c74ed593-388e-4696-b9c2-6adaca0f0c6c)  
![1dbc79e0-af80-4cbd-9cc6-678a54a26eda](https://github.com/user-attachments/assets/9eca09d0-c048-4ca1-b73f-c3cb29630cba)  
![0bc36396-f4b3-4ab6-beea-399256fcfa06](https://github.com/user-attachments/assets/6477cc51-d20f-46e7-a9d1-bdcb0fdfa294)  
![ccb899a6-bd30-4ec4-8da5-e5f0a19fa289](https://github.com/user-attachments/assets/4b0ecf65-8af4-4f4b-ade8-4411cdf3981f)  

### 1. Wiring Diagram for Raspberry Pi Pico and Volume Knob [Potentiometer] 

                           [ MICRO-USB ]
                          /             \
             ____________|_______________|____________
            | [ ] [ ] [ ]                 [ BOOTSEL ] |
      GP0 --| 1                                    40 |-- VBUS (5V USB)
      GP1 --| 2                                    39 |-- VSYS (2-5V)
      GND --| 3             [ RP2040 ]             38 |-- GND
      GP2 --| 4               (CHIP)               37 |-- 3V3_EN
      GP3 --| 5                                    36 |-- 3V3 OUT [Knob PIN 1 Positive Power]
      GP4 --| 6                                    35 |-- ADC_VREF
      GP5 --| 7              [ FLASH ]             34 |-- GP28 / A2
      GND --| 8              (MEMORY)              33 |-- GND [Knob PIN 3 Negative Power]
      GP6 --| 9                                    32 |-- GP27 / A1
      GP7 --| 10                                   31 |-- GP26 / A0 [Knob PIN 2 Signal]
      GP8 --| 11                                   30 |-- RUN (RESET)
      GP9 --| 12            [ CRYSTAL ]            29 |-- GP22
      GND --| 13                                   28 |-- GND
     GP10 --| 14                                   27 |-- GP21
     GP11 --| 15                                   26 |-- GP20
     GP12 --| 16                                   25 |-- GP19
     GP13 --| 17                                   24 |-- GP18
      GND --| 18                                   23 |-- GND
     GP14 --| 19            [ DEBUG ]              22 |-- GP17
     GP15 --| 20            (SWD PINS)             21 |-- GP16
            |_________________________________________|

### 2. Firmware for Raspberry Pi Pico
CircuitPython UF2 [Click here to download the Firmware](https://circuitpython.org/board/raspberry_pi_pico/)
1. Hold BOOTSEL
2. Plug in USB
3. Copy the CircuitPython UF2 Firmware onto the RPI-RP2 drive.
4. Raspberry Pi Pico Device will restart with your Firmware.  

### 3. MicroPython for Raspberry Pi Pico
1. Run the following comment to verify the Code is correct: python -m py_compile boot.py MidiKnob.py main.py  
2. Copy Code to the CIRCUITPY drive: boot.py, MidiKnob.py, main.py   
3. Hard Reset the Raspberry Pi Pico, replug the USB so Windows can find the DJ Mixer.  

### 4. MicroPython Code  
1. USB Device Name | boot.py [Click to view the code](https://test.com)  
2. MIDI Volume Knob | MidiKnob.py [Click to view the code](https://test.com)  
3. MIDI Device Main Code | main.py [Click to view the code](https://test.com)  


### 5. PuTTY Testing
![86577e6c-a461-44f6-8fba-a4fd0da4a37e](https://github.com/user-attachments/assets/72b99873-b96e-4c9b-8490-2b76b1a3f843)  
1. Open COM5 (for example), Speed 115200.  
2. Press Ctrl+C and you are in the Raspberry Pi Pico REPL Console.  
3. Type the following test commands.  
`import board, analogio`  
`myKnob = analogio.AnalogIn(board.GP26)`  
`print(myKnob.value)`  
4. Turn the Knob and repeat the Print Test Command to see the changing volume values.  

### 6. Mixxx (DJ Software) Configuration 
[Click to view Mixxx website](https://mixxx.org/)  
[Click here to watch the DJ Mixer being setup to control the Master Volume Gain on the Mixxx DJ Software](https://github.com/user-attachments/assets/174267b2-277f-4a17-ad45-1758d374d3d4)  
1. Preferences > Controllers  
2. Enable CircuitPython [DJ Mixer]  
3. Use the Learning Wizard to link your physical knob to the Master Volume Gain.  
