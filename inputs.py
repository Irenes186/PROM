import constants
import debugdisplay

import platform

def init():
    debugdisplay.printHardwareDebugHeader()


def update(bat1, bat2, GameState):
    
    if platform.system() == "Linux":
        # Code for reading pot positions
        # & Software debounce for buttons
        pass
    else:
        # Do some key bindings for testing
        pass
    
    debugdisplay.printHardwareDisplay(1.5, 0, 1, bat1.position.y, bat1.length, 3, 0, 0, bat2.position.y, bat2.length)
