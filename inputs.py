import constants
import debugdisplay
import platform
import smbus
import time
import serialprint
from threading import Timer

pins = [0xFE, 0xFD, 0xFB, 0xF7]
I2CADDR = 0x21
CMD_CODE = 0x10    # identify this from the data sheet
I2C_ADC_ADDR = 0x22
PORT_ON = 0xFF
I2C_buttons_ADDR = 0x39
bus = smbus.SMBus(1)

pin_list = [0xFE, 0xFD, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F, 0x7F]
pin_values = [False]

###################Buttons###################
controller_one_debounce = 0
controller_one_debounce_on = False
controller_two_debounce = 0
controller_two_debounce_on = False


b1sizecharges = 2
b2sizecharges = 2

def batreset(bat):
    bat.length = 3

#############################################
def init():
    print("Init")
    debugdisplay.printHardwareDebugHeader()

def convertToPosition(ADC_Value, bat_size):
    ADC_Step = (constants.ADC_highend - constants.ADC_lowend)/(constants.ROWS - (bat_size - 1))
    val = (ADC_Value - constants.ADC_lowend) / ADC_Step
    val = max(0, val)
    val = min((constants.ROWS - (bat_size)), val)
    return val

def update(bat1, bat2, state):
    global controller_one_debounce, controller_one_debounce_on, controller_two_debounce, controller_two_debounce_on, b1sizecharges, b2sizecharges
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

    ########################Hardware_ADC###########################
    bus.write_byte(I2C_ADC_ADDR, PORT_ON )
    readData = bus.read_byte(I2C_ADC_ADDR)
    bat2.position.y = 217 - readData + 24
    bat2.position.y = max(bat2.position.y, 0)
    bat2.position.y = min(bat2.position.y, 24-bat2.length)

    ######################################################

    bus.write_byte( I2C_buttons_ADDR, PORT_ON )
    readValue = bus.read_byte(I2C_buttons_ADDR)
    #print(readValue)
    binaryVal = '{0:04b}'.format(readValue)[-4:]
    #print(binaryVal)

    b1serve = b1size = b2serve = b2size = False

    if binaryVal[0] == "0" and controller_one_debounce_on == False:
        controller_one_debounce_on = True
        controller_one_debounce = 5
    if controller_one_debounce_on:
        controller_one_debounce -= 1

    if controller_one_debounce > 0:
        b1serve = True
    elif controller_one_debounce == 0:
        controller_one_debounce_on = False

    if binaryVal[1] == "0" and controller_two_debounce_on == False:
        controller_two_debounce_on = True
        controller_two_debounce = 5

    if controller_two_debounce_on:
        controller_two_debounce -= 1

    if controller_two_debounce > 0:
        b2serve = True
    elif controller_two_debounce == 0:
        controller_two_debounce_on = False

    b1size = (binaryVal[2] == "0")
    b2size = (binaryVal[3] == "0")

    if b1size and bat1.length == 3 and b1sizecharges > 0:
        bat1.length = 6
        b1sizecharges -= 1
        t = Timer(15, batreset, args=[bat1])
        t.start() 
    
    if b2size and bat2.length == 3 and b2sizecharges > 0:
        bat2.length = 6
        b2sizecharges -= 1
        t = Timer(15, batreset, args=[bat2])
        t.start()

    if state[0] == constants.STATE_SERVE:
        if state[1] == 1:
            if b1serve:
                state[0] = constants.STATE_IN_PLAY
        elif state[1] == -1:
            if b2serve:
                state[0]= constants.STATE_IN_PLAY


    ########################################################

    debugdisplay.printHardwareDisplay(finalVal, b1serve, b1size, bat1.position.y, bat1.length, readData, b2serve, b2size, bat2.position.y, bat2.length)
