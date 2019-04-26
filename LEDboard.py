import smbus
import time
I2C_ADDR = [0x10, 0x11, 0x12, 0x14, 0x16, 0x17, 0x19, 0x20]
LED_ON = 0x00
LED_OFF = 0xFF
bus = smbus.SMBus(1)
     
def updateboard(GameState, position):
    for i in range(0, len(I2C_ADD)):
        bus.write_byte(I2C_ADD[i], LED_OFF)

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
