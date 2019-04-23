#switching LEDS on and off
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#to be changed with the actual value
pin_list = [11,12, 13, 14, 15, 16, 17, 18]
#the following pins will be used as outputs
GPIO.setup(pin_list[0], GPIO.OUT)
GPIO.setup(pin_list[1], GPIO.OUT)
GPIO.setup(pin_list[2], GPIO.OUT)
GPIO.setup(pin_list[3], GPIO.OUT)
GPIO.setup(pin_list[4], GPIO.OUT)
GPIO.setup(pin_list[5], GPIO.OUT)
GPIO.setup(pin_list[6], GPIO.OUT)
GPIO.setup(pin_list[7], GPIO.OUT)


#turns on a LED every 3 seconds/ 8 LEDs time

for i in range(0, len(pin_list)):
    GPIO.output(pin_list[i], GPIO.HIGH)
    time.sleep(0.375)

    GPIO.output(pin_list[i], GPIO.LOW)
