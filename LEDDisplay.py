import smbus
import RPi.GPIO as GPIO
import time
import constants
import math

bus = smbus.SMBus(1)

pin_list = [5, 6, 12, 13, 16, 19, 20, 26, 26]
#pins = [0xFE, 0xFD, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F, 0x7F]
pins = [0x7F, 0x7F, 0xBF, 0xDF, 0xEF, 0xF7, 0xFB, 0xFD, 0xFE]

def init():
	print("INIT TEST!!!")
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	for i in range(0, len(pin_list)):
		GPIO.setup(pin_list[i], GPIO.OUT)

def write7Seg(value):
    bus.write_byte(0x39, ((int(value / 2) % 2) * 0x10) + ((value % 2) * 0x20) + 0x40)

def countdown7seg():
    for i in range(3, -1, -1):
        write7Seg(i)
        time.sleep(1)
        bus.write_byte(0x39, 0x00)

def updateBoard(position):
    for i in range(0, len(pin_list)):
        GPIO.output(pin_list[i], False)

    lvl = math.floor(float(position)/10)
    #print(lvl)
    bus.write_byte(0x38, pins[int(lvl)])
    GPIO.output(pin_list[int(lvl)], True)
