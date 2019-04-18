
def printHardwareDebugHeader():
    print("Diagnostic Information:\r\n")
    print("|A ADC | A1 | A2 | B ADC | B1 | B2 |\r\n")
    print("|----------------------------------|\r\n")

def printHardwareDisplay(aval, a1, a2, bval, b1, b2):
    print("| " + str(aval).zfill(3) + "% |  " + str(a1) + " |  " + str(a2) + " |  " + str(bval).zfill(3) + "% |  " + str(b1) + " |  " + str(b2) + " |\r")