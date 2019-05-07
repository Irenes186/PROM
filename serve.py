import RPi.GPIO as GPIO
import time
import constants
import math

pins = [0xFE, 0xFD, 0xFB, 0xF7]
bus = smbus.SMBus(1)


def serve_from_bat(position):
    bus.write_byte(0x38, pins[int(lvl)])
