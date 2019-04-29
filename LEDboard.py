#import smbus
import time
import RPi.GPIO as GPIO

#I2C_ADDR = [0x10, 0x11, 0x12, 0x14, 0x16, 0x17, 0x19, 0x20]
#LED_ON = 0x00
#LED_OFF = 0xFF
#bus = smbus.SMBus(1)

GPIO.setwarnings(False) #disable runtime warnings
GPIO.setmode(GPIO.BCM) #use Broadcom GPIO names
GPIO.setup(10, GPIO.OUT) #set pin 10 as output

while True: #infinite loop
	GPIO.output(10, True) #set pin 10 high
	time.sleep(0.5) #wait 1/2 sec
	GPIO.output(10, False) #set pin 10 low
	time.sleep(0.5) #wait 1/2 sec

  
def updateBoard(position):
    for i in range(0, len(I2C_ADDR)):
        bus.write_byte(I2C_ADDR[i], LED_OFF)

	#print("LEDDisp")
    if position <= 10 :
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 10 and position <= 20:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 20 and position <= 30:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 30 and position <= 40:
        bus.write_byte( I2C_ADDR[i], LED_ON )#import smbus
import time
import RPi.GPIO as GPIO

#I2C_ADDR = [0x10, 0x11, 0x12, 0x14, 0x16, 0x17, 0x19, 0x20]
#LED_ON = 0x00
#LED_OFF = 0xFF
#bus = smbus.SMBus(1)

GPIO.setwarnings(False) #disable runtime warnings
GPIO.setmode(GPIO.BCM) #use Broadcom GPIO names
GPIO.setup(10, GPIO.OUT) #set pin 10 as output

while True: #infinite loop
	GPIO.output(10, True) #set pin 10 high
	time.sleep(0.5) #wait 1/2 sec
	GPIO.output(10, False) #set pin 10 low
	time.sleep(0.5) #wait 1/2 sec

  
def updateBoard(position):
    for i in range(0, len(I2C_ADDR)):
        bus.write_byte(I2C_ADDR[i], LED_OFF)

	#print("LEDDisp")
    if position <= 10 :
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 10 and position <= 20:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 20 and position <= 30:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 30 and position <= 40:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 40 and position <= 50:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 50 and position <= 60:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 60 and position <= 70:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    else:
        bus.write_byte( I2C_ADDR[i], LED_ON )

#updateBoard(11)
    elif position > 40 and position <= 50:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 50 and position <= 60:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    elif position > 60 and position <= 70:
        bus.write_byte( I2C_ADDR[i], LED_ON )
    else:
        bus.write_byte( I2C_ADDR[i], LED_ON )

#updateBoard(11)
