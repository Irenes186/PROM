import time
import RPi.GPIO as GPIO
import smbus

LED_ON = 0x00
LED_OFF = 0xFF
I2C = 0x38
bus = smbus.SMBus(1)
  
bus.write_byte(0x38,LED_OFF)
time.sleep(1)

pins = [0xF1,0xF2, 0xF4, 0xF8,0x1F, 0x2F, 0x4F, 0x8F]
  

def updateBoard(position):
	#test
    for i in range(0, len(pins)):
        bus.write_byte(0x38, pins[i])
	#game functionality
    if position <= 10 :
        bus.write_byte(0x38, pins[0])
    elif position > 10 and position <= 20:
        bus.write_byte(0x38, pins[1])
    elif position > 20 and position <= 30:
        bus.write_byte(0x38, pins[2])
    elif position > 30 and position <= 40:
        bus.write_byte(0x38, pins[3])
    elif position > 40 and position <= 50:
        bus.write_byte(0x38, pins[4])
    elif position > 50 and position <= 60:
        bus.write_byte(0x38, pins[5])
    elif position > 60 and position <= 70:
        bus.write_byte(0x38, pins[6])
    else:
        bus.write_byte(0x38, pins[7])
