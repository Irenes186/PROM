import RPi.GPIO as GPIO
import time
from threading import Timer

import constants


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(constants.PINS["Buzzer"], OUTPUT)

buzzerPin = GPIO.PWM(constants.PINS["Buzzer"], 10)
  
def stopNote():
    buzzerPin.stop(0)

def playSequence(sequence):
    for note in sequence:
        t = Timer()
        playSound(note[0], note[1])

def playSequence(sequence):
    buzzerPin.stop()
    if len(sequence) == 0:
        return

    buzzerPin.changeDutyCycle(constants.NOTES[sequence.pop(0)])
    buzzerPin.start(50)
    t = Timer(duration, playSequence, args=sequence)
    t.start()
