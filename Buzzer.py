import RPi.GPIO as GPIO
import time
from threading import Timer
import constants



#part1= [[76, 12], [76, 12], [20, 12], [76, 12], [20, 12], [72, 12], [76, 12], [20, 12], [79, 12], [20, 36], [67, 12], [20, 36] ]

#part2 = [[72, 12], [20, 24], [67, 12], [20, 24], [64, 12], [20, 24], [69, 12], [20, 12], [71, 12], [20, 12], [70, 12], [69, 12], [20, 12], [67, 16], [76, 16], [79, 16], [81, 12], [20, 12], [77, 12], [79, 12], [20, 12], [76, 12], [20, 12], [72, 12], [74, 12], [71, 12], [20, 24]]
#
#part3 = [ [48, 12], [20, 12], [79, 12], [78, 12], [77, 12], [75, 12], [60, 12], [76, 12], [53, 12], [68, 12], [69, 12], [72, 12], [60, 12], [69, 12], [72, 12], [74, 12], [48, 12], [20, 12], [79, 12], [78, 12], [77, 12], [75, 12], [55, 12], [76, 12], [20, 12], [84, 12], [20, 12], [84, 12], [84, 12] ]

#part4 = [55, 12, 20, 12, 48, 12, 20, 12, 79, 12, 78, 12, 77, 12, 75, 12, 60, 12, 76, 12, 53, 12, 68, 12, 69, 12, 72, 12, 60, 12, 69, 12, 72, 12, 74, 12, 48, 12, 20, 12, 75, 24, 20, 12, 74, 24, 20, 12, 72, 24, 20, 12, 55, 12, 55, 12, 20, 12, 48, 12 ]

#part5 = [ [72, 12], [72, 12], [20, 12], [72, 12], [20, 12], [72, 12], [74, 12], [20, 12], [76, 12], [72, 12], [20, 12], [69, 12], [67, 12], [20, 12], [43, 12], [20, 12], [72, 12], [72, 12],[20, 12], [72, 12], [20, 12], [72, 12], [74, 12], [76, 12], [55, 12], [20, 24], [48, 12], [20, 24], [43, 12], [20, 12], [72, 12], [72, 12], [20, 12], [72, 12],[ 20, 12], [72, 12], [74, 12], [20, 12], [76, 12], [72, 12], [20, 12], [69, 12], [67, 12], [20, 12], [43, 12], [20, 12], [76, 12], [76, 12], [20, 12], [76, 12], [20, 12], [72, 12], [76, 12], [20, 12], [79, 12], [20, 36], [67, 12], [20, 36] ]

#part6 = [ [76, 12], [72, 12], [20, 12], [67, 12], [55, 12], [20, 12], [68, 12], [20, 12], [69, 12], [77, 12],[53, 12], [77, 12], [69, 12], [60, 12], [53, 12], [20, 12], [71, 16], [81, 16], [81, 16], [81, 16], [79, 16], [77, 16], [76, 12], [72, 12], [55, 12], [69, 12], [67, 12], [60, 12], [55, 12], [20, 12], [76, 12], [72, 12], [20, 12], [67, 12], [55, 12], [20, 12], [68, 12], [20, 12], [69, 12], [77, 12], [53, 12], [77, 12], [69, 12], [60, 12], [53, 12], [20, 12], [71, 12], [77, 12], [20, 12], [77, 12], [77, 16], [76, 16], [74, 16], [72, 12], [64, 12], [55, 12], [64, 12], [60, 12], [20, 36] ]

#part7 = [ [72, 12], [20, 24], [67, 12], [20, 24], [64, 24], [69, 16], [71, 16], [69, 16], [68, 24], [70, 24], [68, 24], [67, 12], [65, 12], [67, 48], [72, 12], [20, 24], [67, 12], [20, 24], [64, 12], [20, 24], [69, 12], [20, 12], [71, 12], [20, 12], [70, 12], [69, 12], [20, 12], [67, 16], [76, 16], [79, 16], [81, 12], [20, 12], [77, 12], [79, 12], [20, 12], [76, 12], [20, 12], [72, 12], [74, 12], [71, 12], [20, 24]]


#X = [part1, part2, part2, part3, part3, part5, part2, part2, part6, part6, part5, part6, part7]
#Y = [[76, 12], [76, 12], [20, 12], [76, 12], [20, 12], [72, 12], [76, 12], [20, 12], [79, 12], [20, 36], [67, 12], [20, 36] ]

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
         
for sequence in range(0, len(Y)) :
    Y[sequence][0] = (float) (2**((Y[sequence][0] -21)/12))*27.5
    Y[sequence][1] =   Y[sequence][1]/10

playSequence(Y)

