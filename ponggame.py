import serialprint
import debugdisplay
import constants

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
            serialprint.print_at(y, self.position.x, "X")

class Net:

     def __init__(self, x, length):
        self.x = x
        self.length = length

     def draw(self):
        for y in range(self.length):
            serialprint.print_at(y, self.x, "X")

class Score:

    def __init__(self, val, x, y):
        self.position = Point(x, y)
        self.value = val

    def draw(self):
        for y in range(5):
            serialprint.print_at(self.position.y + y, self.position.x, constants.DIGITS[self.value][y])

serialprint.setColor(31)

b1 = Bat(3, 3)
b2 = Bat(77, 3)
net = Net(40, 24)

s1 = Score(7, 29, 1)
s2 = Score(1, 49, 1)

#b1.draw()
#b2.draw()
#net.draw()
#s1.draw()
#s2.draw()

debugdisplay.printHardwareDebugHeader()
debugdisplay.printHardwareDisplay(1.5, 0, 1, 10, 3, 3, 0, 0, 10, 6)

while True:
    pass
