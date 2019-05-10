import RPi.GPIO as GPIO
import time
from threading import Timer
import constants


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(constants.PINS["Buzzer"], GPIO.OUT)

buzzerPin = GPIO.PWM(constants.PINS["Buzzer"], 500)

def playTone(frequency, time):
    t = Timer(0.5, delay, args=[frequency, time])
    t.start()

def delay(frequency, time):
    buzzerPin.ChangeFrequency(frequency)
    buzzerPin.start(50)
    t = Timer(time, stop)
    t.start()
    
def stop():
    buzzerPin.stop()
    
