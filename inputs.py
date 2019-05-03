import constants
import debugdisplay
import platform
import smbus
import time

I2CADDR = 0x21
CMD_CODE = 0x10	# identify this from the data sheet
bus = smbus.SMBus(1)

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
