import serialprint

def printHardwareDebugHeader():
    print("\033[2J")
    serialprint.print_at(1, 1, "Diagnostic Information:", CONSOLE=True)
    serialprint.print_at(2, 1, "| A RAW ADC | Serve  | ASize  | Bat Pos | Size |", CONSOLE=True)
    serialprint.print_at(3, 1, "|----------------------------------------------|", CONSOLE=True)

    serialprint.print_at(5, 1, "|----------------------------------------------|", CONSOLE=True)
    serialprint.print_at(6, 1, "| B RAW ADC | Serve  | BSize  | Bat Pos | Size |", CONSOLE=True)
    serialprint.print_at(7, 1, "|----------------------------------------------|", CONSOLE=True)

    serialprint.print_at(9, 1, "|----------------------------------------------|", CONSOLE=True)

def printHardwareDisplay(aval, a1, a2, apos, asize, bval, b1, b2, bpos, bsize):
    serialprint.print_at(4, 1, "|  " + str(aval).rjust(8) + " |  " + str(a1).rjust(5) + " |  " + str(a2).rjust(5) + " | " + str(apos).rjust(3) + "/" + str(24-asize).ljust(2) + "  | " + str(asize).rjust(3) + "  |", CONSOLE=True)
    serialprint.print_at(8, 1, "|  " + str(bval).rjust(8) + " |  " + str(b1).rjust(5) + " |  " + str(b2).rjust(5) + " | " + str(bpos).rjust(3) + "/" + str(24-bsize).ljust(2) + "  | " + str(bsize).rjust(3) + "  |", CONSOLE=True)
