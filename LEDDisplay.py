#switching LEDS on and off
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#to be changed with the actual value
pin_list = [5, 6, 12, 13, 16, 19, 20, 26]
#the following pins will be used as outputs

for i in range(0, len(pin_list)):
    GPIO.setup(pin_list[i], GPIO.OUT)


#turns on a LED every 3 seconds/ 8 LEDs time

for i in range(0, len(pin_list)):
    GPIO.output(pin_list[i], True)
    time.sleep(1)

    GPIO.output(pin_list[i], False)
