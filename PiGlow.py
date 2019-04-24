import time
from PyGlow import PyGlow

pyglow = PyGlow()
	
def blueWin():
	for i in range(0, 5):
		pyglow.color("white", 50)
		pyglow.color("blue", 200)
		pyglow.color("green", 80)
		pyglow.color("yellow", 50)
		time.sleep(0.15)
		pyglow.all(0)
		time.sleep(0.15)

def redWin():
	for i in range(0, 5):
			pyglow.color("white", 50)
			pyglow.color("orange", 100)
			pyglow.color("yellow", 50)
			pyglow.color("red", 200)
			time.sleep(0.15)
			pyglow.all(0)
			time.sleep(0.15)
