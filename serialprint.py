from ctypes import *
import os

from serial import Serial

serialPort = Serial("/dev/ttyAMA0", 115200)

if serialPort.isOpen() == False:
    serialPort.open()

# Clear the screen
serialPort.write("\033[2J")

# Hide the cursor
serialPort.write("\033[?25l")

# "\033[y;xH" moves the cursor to row y col x"
def print_at(r, c, s):
    #if CONSOLE:
     #   print(u"\033[" + str(r+1) + ";" + str(c) + "H" + str(s))
    #else:
    serialPort.write(u"\033[" + str(r+1) + ";" + str(c) + "H" + str(s))

def setColor(code):
    serialPort.write(u"\033[" + str(code) + "m")
