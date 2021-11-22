First, make sure you have both Python 3 and PyQt5 installed: https://pythonbasics.org/install-pyqt/


If you are trying to run this with the emulator, open a terminal in the "computer-translater-display-main" folder and input either 'bash run.sh' or './run.sh'. Alternatively, you may run the command 'python3 emulator_display.py' and then run 'java -jar SAP-1.jar' found in our modified version of the 8-bit computer emulator: https://github.com/8-Bit-Computer-Project-Team-I-O/SAP-1.git. Otherwise, if using with a Raspberry Pi with the GPIO pins connected to a version of an 8-Bit Computer, run raspberry_pi_display.pi.

Note that you must run the interpreter before the emulator, otherwise you will get an error telling you to run the interpreter first. Bastian's architecture does not work with the emulator display, so that value in the JSON file must be set to 'False' if running the emulator display file.

Controls:
Pressing Ctrl+C at anytime during the program will clear the values on the computer. This is a quick way to restart the display without having to exit out completely and then restarting both the emulator and the display.
