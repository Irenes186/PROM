from ctypes import *
import os

STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]

# This is for windows console
# On Pi replace with ANSI escape sequence, where "\033[y;xH" moves the cursor to row y col x.
def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bat:
   
    def __init__(self, xpos, length):
        self.position = Point(xpos, 10)
        self.length = length
        
    def draw(self):
        for y in range(self.position.y, self.position.y + self.length):
            print_at(y, self.position.x, "X")

class Net:

     def __init__(self, x, length):
        self.x = x
        self.length = length

     def draw(self):
        for y in range(0, self.length):
            print_at(y, self.x, "X")

class Score:

    def __init__(self, val, x, y):
        self.position = Point(x, y)
        self.value = val

    def draw(self):
        pass


b1 = Bat(3, 3)
b2 = Bat(77, 3)
net = Net(40, 24)

b1.draw()
b2.draw()
net.draw()

while True:
    pass
