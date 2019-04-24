#switching LEDS on and off
import RPi.GPIO as GPIO
import time
import ponggame

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#to be changed with the actual value
pin_list = [5, 6, 12, 13, 16, 19, 20, 26]
#the following pins will be used as outputs

for i in range(0, len(pin_list)):
    GPIO.setup(pin_list[i], GPIO.OUT)


#turns on a LED every 3 seconds/ 8 LEDs time

"""for i in range(0, len(pin_list)):
    GPIO.output(pin_list[i], True)
    time.sleep(1)

    GPIO.output(pin_list[i], False)
"""

while  GameState == constants.STATE_IN_PLAY:
    if constants.COLUMNS <= 10 :
        GPIO.output(pin_list[0], True)
    else if constants.COLUMNS > 10 and constants.COLUMNS <= 20:
        GPIO.output(pin_list[1], True)
    else if constants.COLUMNS > 20 and constants.COLUMNS <= 30:
        GPIO.output(pin_list[2], True)
    else if constants.COLUMNS > 30 and constants.COLUMNS <= 40:
        GPIO.output(pin_list[3], True)
    else if constants.COLUMNS > 40 and constants.COLUMNS <= 50:
        GPIO.output(pin_list[4], True)
    else if constants.COLUMNS > 50 and constants.COLUMNS <= 60:
        GPIO.output(pin_list[5], True)
    else if constants.COLUMNS > 60 and constants.COLUMNS <= 70:
        GPIO.output(pin_list[6], True)
    else:
        GPIO.output(pin_list[7], True)
