import constants
import debugdisplay
import platform
import smbus
import time

pins = [0xFE, 0xFD, 0xFB, 0xF7]
I2CADDR = 0x21
CMD_CODE = 0x10	# identify this from the data sheet
I2C_ADDR_1 = 0x20
PORT_ON = 0xFF
bus = smbus.SMBus(1)

pin_list = [0xFE, 0xFD, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F, 0x7F]
pin_values = [False]

def init():
	print("Init")
	debugdisplay.printHardwareDebugHeader()

def convertToPosition(ADC_Value, bat_size):
	ADC_Step = (constants.ADC_highend - constants.ADC_lowend)/(constants.ROWS - (bat_size - 1))
	val = (ADC_Value - constants.ADC_lowend) / ADC_Step
	val = max(0, val)
	val = min((constants.ROWS - (bat_size)), val)
	return val

def update(bat1, bat2, GameState):
	bus.write_byte( I2CADDR, CMD_CODE )
	tmp = bus.read_word_data( I2CADDR, 0x00 )
	binaryVal = '{0:016b}'.format(tmp)
	reversedBits = binaryVal[8:] + binaryVal[:8]
	decimalVal = str(reversedBits)[4:]
	finalVal = int(decimalVal, 2)
	#print("Decimal value = " + str(finalVal))
	bat1.position.y = convertToPosition(finalVal, bat1.length)
	#print(bat1.position.y)
	#time.sleep(0.2)
	debugdisplay.printHardwareDisplay(finalVal, 0, 1, bat1.position.y, bat1.length, 3, 0, 0, bat2.position.y, bat2.length)
	
	
bus.write_byte(I2C_ADDR_1, PORT_ON )

A= bus.read_byte(I2C_ADDR_1, pin_list[])
B= bus.read_byte(I2C_ADDR_1, pin_list[])
C= bus.read_byte( I2C_ADDR_1, pin_list[]) 
D= bus.read_byte( I2C_ADDR_1, pin_list[])
E= bus.read_byte( I2C_ADDR_1, pin_list[])
F= bus.read_byte( I2C_ADDR_1, pin_list[])
G= bus.read_byte( I2C_ADDR_1, pin_list[])
H= bus.read_byte( I2C_ADDR_1, pin_list[])

result = A*1 + B*2 + C*4 + D*8 + E*16 + F*32 + G*64 + H*128
	
