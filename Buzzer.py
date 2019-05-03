import RPi.GPIO as GPIO
import time
from threading import Timer
import constants


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(constants.PINS["Buzzer"], GPIO.OUT)

buzzerPin = GPIO.PWM(constants.PINS["Buzzer"], 500)

def playSequence(sequence):
    print(sequence)
    buzzerPin.stop()
    if len(sequence) > 0:
        note = sequence.pop(0)
        buzzerPin.ChangeFrequency(note[0])
        buzzerPin.start(50)
        t = Timer(note[1], playSequence, args=[sequence])
        t.start()

playSequence([[440, 5]])
