import serialprint

def printHardwareDebugHeader(aval, a1, a2, apos, asize, bval, b1, b2, bpos, bsize):
    print("\033[2J")
    serialprint.print_at(1, 1, "Diagnostic Information:", CONSOLE=True)
    serialprint.print_at(2, 1, "| A RAW ADC | A1 | A2 | Bat Pos | Size |", CONSOLE=True)
    serialprint.print_at(3, 1, "|--------------------------------------|", CONSOLE=True)

    serialprint.print_at(5, 1, "|--------------------------------------|", CONSOLE=True)
    serialprint.print_at(6, 1, "| B RAW ADC | B1 | B2 | Bat Pos | Size |", CONSOLE=True)
    serialprint.print_at(7, 1, "|--------------------------------------|", CONSOLE=True)

    serialprint.print_at(9, 1, "|--------------------------------------|", CONSOLE=True)

def printHardwareDisplay(aval, a1, a2, apos, asize, bval, b1, b2, bpos, bsize):
    serialprint.print_at(4, 1, "|  " + str(aval).rjust(7) + " |  " + str(a1) + " |  " + str(a2) + " | " + str(apos).rjust(6) + "/" + str(25-asize).ljust(2) + "  | " + str(asize).rjust(3) + "  |", CONSOLE=True)
    serialprint.print_at(8, 1, "|  " + str(bval).rjust(7) + " |  " + str(b1) + " |  " + str(b2) + " | " + str(bpos).rjust(6) + "/" + str(25-bsize).ljust(2) + "  | " + str(bsize).rjust(3) + "  |", CONSOLE=True)
