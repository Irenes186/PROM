import RPi.GPIO as GPIO
import time
import constants

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
count = 0

inputs = [0, 0, 0, 0, 0]

def insum():
	return inputs[0] + inputs[1] + inputs[2] + inputs[3] + inputs[4]

while True:
	print(count)
	count += 1
	while insum() == 0:
		inputs[0] = GPIO.input(15)
		inputs[1] = GPIO.input(14)
		inputs[2] = GPIO.input(11)
		inputs[3] = GPIO.input(9)
		inputs[4] = GPIO.input(10)
	print(inputs)
	time.sleep(0.5)

#def readADC():
	
