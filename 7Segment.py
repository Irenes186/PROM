import constants
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(constants.PINS["7-Seg High"], GPIO.OUT)
GPIO.setup(constants.PINS["7-Seg Low"], GPIO.OUT)
GPIO.setup(constants.PINS["7-Seg Enable"], GPIO.OUT)


def enable(value):
    if (int(value / 2) % 2 == 1):
        GPIO.output(constants.PINS["7-Seg High"], True)
    if (value % 2 == 1):
        GPIO.output(constants.PINS["7-Seg Low"], True)

    GPIO.output(constants.PINS["7-Seg Enable"], True)


def disable():
    GPIO.output(constants.PINS["7-Seg Enable"], False)
    GPIO.output(constants.PINS["7-Seg Low"], False)
    GPIO.output(constants.PINS["7-Seg High"], False)
