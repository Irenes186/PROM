import serialprint

def printHardwareDebugHeader():
    serialprint.print_at(1, 1, "Diagnostic Information")
    serialprint.print_at(2, 1, "| A ADC | A1 | A2 | Bat Pos | Size |")
    serialprint.print_at(3, 1, "|----------------------------------|")
    serialprint.print_at(4, 1, "|  " + str(aval).rjust(3) + "% |  " + str(a1) + " |  " + str(a2) + " | " + str(apos).rjust(3) + "/" + str(20-asize).ljust(2) + "  | " + str(asize).rjust(3) + "  |")
    serialprint.print_at(5, 1, "|----------------------------------|")
    serialprint.print_at(6, 1, "| B ADC | B1 | B2 | Bat Pos | Size |")
    serialprint.print_at(7, 1, "|----------------------------------|")
    serialprint.print_at(8, 1, "|  " + str(bval).rjust(3) + "% |  " + str(b1) + " |  " + str(b2) + " | " + str(bpos).rjust(3) + "/" + str(20-bsize).ljust(2)+ "  | " + str(bsize).rjust(3) + "  |")
    serialprint.print_at(9, 1, "|----------------------------------|")
