# DJ Mixer made with MicroPython and Raspberry Pi Pico
[Click here to watch the DJ Mixer in action on Mixxx DJ Software](https://github.com/user-attachments/assets/1c553f8c-8dd1-4aad-b94b-343613790a40)  
  
![1dbc79e0-af80-4cbd-9cc6-678a54a26eda](https://github.com/user-attachments/assets/9eca09d0-c048-4ca1-b73f-c3cb29630cba)  
![0bc36396-f4b3-4ab6-beea-399256fcfa06](https://github.com/user-attachments/assets/6477cc51-d20f-46e7-a9d1-bdcb0fdfa294)  
![ccb899a6-bd30-4ec4-8da5-e5f0a19fa289](https://github.com/user-attachments/assets/4b0ecf65-8af4-4f4b-ade8-4411cdf3981f)  

### 1. Wiring Diagram for Raspberry Pi Pico, Volume Knob [Potentiometer], Headphone Cue [Button]  
  
                          [ MICRO-USB ]  
                          /             \  
             ____________|_______________|____________  
            | [ ] [ ] [ ]                 [ BOOTSEL ] |  
      GP0 --| 1                                    40 |-- VBUS (5V USB)  
      GP1 --| 2                                    39 |-- VSYS (2-5V)  
      GND --| 3             [ RP2040 ]             38 |-- GND  
      GP2 --| 4               (CHIP)               37 |-- 3V3_EN  
      GP3 --| 5                                    36 |-- 3V3 OUT (POT PIN 1)  
      GP4 --| 6                                    35 |-- ADC_VREF  
      GP5 --| 7              [ FLASH ]             34 |-- GP28 / A2  
      GND --| 8              (MEMORY)              33 |-- GND (POT PIN 3)  
      GP6 --| 9                                    32 |-- GP27 / A1  
      GP7 --| 10                                   31 |-- GP26 / A0 (POT WIPER)  
      GP8 --| 11                                   30 |-- RUN (RESET)  
      GP9 --| 12            [ CRYSTAL ]            29 |-- GP22  
      GND --| 13                                   28 |-- GND  
     GP10 --| 14                                   27 |-- GP21  
     GP11 --| 15                                   26 |-- GP20  
     GP12 --| 16                                   25 |-- GP19  
     GP13 --| 17                                   24 |-- GP18  
      GND --| 18                                   23 |-- GND  

     GP14 --| 19  <-- Cue Button CH1 (left leg)  
            |         Cue Button CH1 (right leg) --> GND  

     GP15 --| 20  <-- Cue Button CH2 (left leg)  
            |         Cue Button CH2 (right leg) --> GND  

            |                                   22 |-- GP17  
            |                                   21 |-- GP16  
            |_________________________________________|  

  
### 2. Firmware for Raspberry Pi Pico
CircuitPython UF2 [Click here to download the Firmware](https://circuitpython.org/board/raspberry_pi_pico/)
1. Hold BOOTSEL
2. Plug in USB
3. Copy the CircuitPython UF2 Firmware onto the RPI-RP2 drive.
4. Raspberry Pi Pico Device will restart with your Firmware.  

### 3. MicroPython for Raspberry Pi Pico
1. Copy Code to the CIRCUITPY drive: boot.py, MidiKnob.py, main.py   
3. Reset the Raspberry Pi Pico by replugging in the USB to Windows to find the DJ Mixer.  

### 4. MicroPython Code  
1. MIDI Main Code | main.py [Click to view the code](https://github.com/Kungfoowiz/DJMixer/blob/main/main.py)  
2. MIDI Knob | MidiKnob.py [Click to view the code](https://github.com/Kungfoowiz/DJMixer/blob/main/MidiKnob.py)
3. MIDI Button | MidiButton.py [Click to view the code](https://github.com/Kungfoowiz/DJMixer/blob/main/MidiButton.py)

### 5. PuTTY Testing
![86577e6c-a461-44f6-8fba-a4fd0da4a37e](https://github.com/user-attachments/assets/72b99873-b96e-4c9b-8490-2b76b1a3f843)  
1. Open COM5 (for example), Speed 115200.  
2. Press Ctrl+C and you are in the Raspberry Pi Pico REPL Console.  
3. Type the following test commands.  
`import board, analogio`  
`myKnob = analogio.AnalogIn(board.GP26)`  
`print(myKnob.value)`  
4. Turn the Knob and repeat the Print Test Command to see the changing volume values.  

### 6. Mixxx (DJ Software) Install  
[Click to view Mixxx website](https://mixxx.org/)  

### 7. Master Volume Gain Configuration   
[Click here to watch the DJ Mixer being setup to control the Master Volume Gain on the Mixxx DJ Software](https://github.com/user-attachments/assets/feb887bd-2f77-4693-9b00-1f7e95c94420)  
  
1. Preferences > Controllers  
2. Enable CircuitPython [DJ Mixer]  
3. Use the Learning Wizard to link your physical knob to the Master Volume Gain.  

### 8. Headphone Cue Configuration 
[Click here to watch the DJ Mixer being setup for Headphone Cues on the Mixxx DJ Software](https://github.com/user-attachments/assets/59d0e264-92cb-4635-8caf-5a2e17bedcf7)  
  
![Headphone Cue Buttons working](https://github.com/user-attachments/assets/45569a21-6c4b-425c-a57b-c6715b0c6437)  
![Headphone Cue Buttons wiring](https://github.com/user-attachments/assets/b031b12a-3a67-4521-af70-4b56131af691)  
  
1. Preferences > Sound Hardware  
2. Go to Headphones > Output
3. Set it to output to Speaker/Headphones [Headphone Jack] instead of Primary Sound Driver.
  
#### Headphone Cue Usage  
1. Plug Head-/Earphones into your Audio Jack.
2. When mixing Music from Left to Right, press Headphone Cue Button 2 and you will hear it in your Headphones, but not the audience.
7. When mixing from Right to Left, use Headphone Cue Button 1.
