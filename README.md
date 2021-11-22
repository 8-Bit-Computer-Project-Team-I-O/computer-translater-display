First, make sure you have both Python 3 and PyQt5 installed: https://pythonbasics.org/install-pyqt/
Next, ensure you have the latest Java SE Development Kit installed: https://www.oracle.com/java/technologies/downloads/



If you are trying to run this with the emulator:

Linux/Mac Users: Open a terminal in the "computer-translater-display-main" folder and input either 'bash run.sh' or 'sh run.sh' or './run.sh'. Ensure the bash script has executable permissions using 'chmod +x run.sh'.

Windows Users: Double click the 'run.bat' file in the "computer-translater-display-main" folder.

All Users: Alternatively, using the Terminal on Linux and Mac or Command Prompt on Windows, you may run 'python3 emulator_display.py' and then run 'java -jar SAP-1.jar' found in our modified version of the 8-bit computer emulator: https://github.com/8-Bit-Computer-Project-Team-I-O/SAP-1.git. Note that you must run the interpreter before the emulator, otherwise you will get an error telling you to run the interpreter first. Additionally, Bastian's architecture does not work with the emulator display, so that value in the JSON file must be set to 'False' if running the emulator display file.

Otherwise, if using with a Raspberry Pi with the GPIO pins connected to a version of an 8-Bit Computer, run 'python3 raspberry_pi_display.py'.



Controls:
Pressing Ctrl+C at anytime during the program will clear the values on the computer. This is a quick way to restart the display without having to exit out completely and then restarting both the emulator and the display.
