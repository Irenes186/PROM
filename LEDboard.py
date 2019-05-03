import time
import RPi.GPIO as GPIO
import smbus

LED_ON = 0x00
LED_OFF = 0xFF
I2C = 0x38
bus = smbus.SMBus(1)

bus.write_byte(0x38, 0xFF)

pins = [0xFE, 0xFD, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F]

def updateBoard(position):
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
