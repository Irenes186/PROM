import serialprint
import debugdisplay
import constants
import os 

rows = 24 
columns = 80 
serves = 0 

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
         
class Ball:   
    def __init__(self, x, y):
        self.position = Point(x, y)
        self.velocity = Point(1.0, 1, 1)
    def draw(self):
        if serves < 6: #left player starts
            # x would be 4 rows across
            # y would be xpos + 5
            serialprint.print(b1.position.y + (0.5*b1.length) , 4, ".")
        else: #right player starts
            serialprint.print_at(b2.position.y + (0.5*b2.length), columns - 8, ".")
    
        
       
   
serialprint.setColor(31)



b1 = Bat(3, 3)
b2 = Bat(77, 3)
net = Net(40, 24)
ball = Ball(40 , 6)

s1 = Score(7, 29, 1)
s2 = Score(1, 49, 1)

#b1.draw()
#b2.draw()
#net.draw()
#s1.draw()
#s2.draw()

#collision with any of the 4 walls
def collision_with_wall(ball):
    if ball.position.x == rows:
        ball.velocity.x = -1
    if ball.position.x == 0:
        ball.velocity.x = 1
    if ball.position.y == columns:
       ball.velocity.y = -1
    if ball.position.y == 0:
       ball.velocity.y = 1
    return ball.velocity


debugdisplay.printHardwareDebugHeader()
debugdisplay.printHardwareDisplay(1.5, 0, 1, 10, 3, 3, 0, 0, 10, 6)

while True:
    pass
