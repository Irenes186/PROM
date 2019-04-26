import smbus
import time
I2C_ADDR = 0x20
LED_ON = 0x00
LED_OFF = 0xFF
bus = smbus.SMBus(1)

while True:
     bus.write_byte( I2C_ADDR, LED_ON )
     time.sleep(1)
     bus.write_byte( I2C_ADDR, LED_OFF )
     time.sleep(1)
