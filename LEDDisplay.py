#switching LEDS on and off
import RPi.GPIO as GPIO
import time
import constants

pin_list = [5, 6, 12, 13, 16, 19, 20, 26]

def init():
	print("INIT TEST!!!")
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	#to be changed with the actual value

	#the following pins will be used as outputs

	for i in range(0, len(pin_list)):
		GPIO.setup(pin_list[i], GPIO.OUT)


	#turns on a LED every 3 seconds/ 8 LEDs time
"""for i in range(0, len(pin_list)):
    GPIO.output(pin_list[i], True)
    time.sleep(1)

    GPIO.output(pin_list[i], False)
"""

def update(GameState, position):
    for i in range(0, len(pin_list)):
        GPIO.output(pin_list[i], False)

	#print("LEDDisp")
    if position <= 10 :
        GPIO.output(pin_list[0], True)
    elif position > 10 and position <= 20:
        GPIO.output(pin_list[1], True)
    elif position > 20 and position <= 30:
        GPIO.output(pin_list[2], True)
    elif position > 30 and position <= 40:
        GPIO.output(pin_list[3], True)
    elif position > 40 and position <= 50:
        GPIO.output(pin_list[4], True)
    elif position > 50 and position <= 60:
        GPIO.output(pin_list[5], True)
    elif position > 60 and position <= 70:
        GPIO.output(pin_list[6], True)
    else:
        GPIO.output(pin_list[7], True)
