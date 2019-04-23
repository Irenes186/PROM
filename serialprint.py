from ctypes import *
import os
import platform

if platform.system() == "Linux":
    from serial import Serial

    serialPort = Serial("/dev/ttyAMA0", 115200)

    if serialPort.isOpen() == False:
        serialPort.open()

    serialPort.write("\033[2J")


# Windows stuff
STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
COORD._fields_ = [("X", c_short), ("Y", c_short)]
# End windows stuff

# This is for windows console
# On Pi replace with ANSI escape sequence, where "\033[y;xH" moves the cursor to row y col x.
def print_at(r, c, s, CONSOLE=False):
    if platform.system() == "Windows":
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
        c = s.encode("windows-1252")
        windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
    # Linux, Hopefully also works on mac?
    else:
        if CONSOLE:
            print(u"\033[" + str(r+1) + ";" + str(c) + "H" + str(s))
        else:
            serialPort.write(u"\033[" + str(r+1) + ";" + str(c) + "H" + str(s))

# Colour only works on linux
def setColor(code):
    if platform.system() == "Linux":
        serialPort.write(u"\033[" + str(code) + "m")
