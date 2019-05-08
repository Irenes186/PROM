import RPi.GPIO as GPIO
import time
from threading import Timer
import constants
E3 = 82.41
E3 = 164.81
C3 = 130.81
G3 = 196
G = 49
A2 = 110
B2 = 123.47
Bb2 = 116.54
A3 = 220.00
F3 = 174.61
D3 = 146.83
F3H = 185


X =  [E3, E3, E3, C3, E3, G3, G, C3, G, E3, A2, 
      B2, Bb2, A2, G, E3, G3, A3, F3, G3, C3, 
      D3, B, G3, F3H, F3, D3, E3]

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

for i in range(0, len(X)):
      playSequence([[X[i], 5]])
