# ADC TEST CODE
# TEST 1: to check if the ADC's I2C interface is working, at
# the command line type : sudo i2cdetect -y 1
# This will scan the I2C bus, returning active addresses. If
# the ADC is work address 0x21 will be listed.
# First words of advice : ** READ THE ADC's DATA SHEET **
# When you have done this consider the Python code below.
# I would suggest using the ADC in mode 2. A description is
# on page 29. To read an input you must first write a command
# word to the ADC, triggering the conversion. Then the
# converted value can be read back. HOWEVER, the 16 bit value
# read back contains additional information, as described on
# page 20.

def convert2position(number):
	val = (number-950)/159
	val = max(0, val)
	print(val)

import smbus
import time

I2CADDR = 0x21
CMD_CODE = 0x10	# identify this from the data sheet

bus = smbus.SMBus(1)

while True:
	bus.write_byte( I2CADDR, CMD_CODE )
	tmp = bus.read_word_data( I2CADDR, 0x00 )
	#print(tmp)
	binaryVal = '{0:016b}'.format(tmp)
	reversedBits = binaryVal[8:] + binaryVal[:8]
	#print(reversedBits)
	#print(binaryVal)
	decimalVal = str(reversedBits)[4:]
	#print(decimalVal)
	finalVal = int(decimalVal, 2)
	print("Decimal value = " + str(finalVal))
	convert2position(finalVal)
	#time.sleep(0.2)

# The value in the variable tmp needs further processing.

# Problem 1: the ADC returns the converted value back to
# the Pi in the wrong byte order. The Pi is expecting
# HIGH BYTE : LOW BYTE, but is receives LOW BYTE : HIGH BYTE.
# Therefore the bytes in the 16bit value in tmp must be
# swapped.

# Problem 2: as described on page 20. The top four bits of the
# received packet do not contain numerical data. Therefore,
# these bits must be zeroed.

# Second words of advice : Bitwise functions

# Final words of advice  : ** READ THE ADC's DATA SHEET **
