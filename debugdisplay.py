import serialprint

def printHardwareDebugHeader():
    print("\f")
    print_at(1, 1, "Diagnostic Information:",)
    print_at(2, 1, "|A ADC | A1 | A2 | Bat Pos | Size |")
    print_at(3, 1, "|-------------------------------------|\r\n")
    print_at(5, 1, "|B ADC | B1 | B2 | Bat Pos | Size |")
    print_at(6, 1, "|-------------------------------------|\r\n")

def printHardwareDisplay(aval, a1, a2, bval, b1, b2):
    print_at(4, 1, "| " + str(aval).rjust(3, " ") + "% |  " + str(a1) + " |  " + str(a2) + " |  ")
    print_at(7, 1, "| " + str(bval).rjust(3, " ") + "% |  " + str(b1) + " |  " + str(b2) + " |\r")
