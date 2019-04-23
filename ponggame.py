import serialprint
import constants
import inputs

import time
from math import ceil

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
        for y in range(0, self.length, 4):
            serialprint.print_at(y,   self.x, "X")
            serialprint.print_at(y+1, self.x, "X")

class Score:
    def __init__(self, x, y, val):
        self.position = Point(x, y)
        self.value = val

    def draw(self):
        self.value = abs(self.value % 10)
        for y in range(5):
            serialprint.print_at(self.position.y + y, self.position.x, constants.DIGITS[self.value][y])
         
class Ball:   
    def __init__(self, x, y):
        self.lastposition = Point(x, y)
        self.position = Point(x, y)
        self.velocity = Point(2, 1)

    def erase(self):
        serialprint.print_at(self.lastposition.y, self.lastposition.x, " ")
    def draw(self):
        serialprint.print_at(self.position.y, self.position.x, "o")

# Moves the ball while a player is serving
def update_serve():
    if PLAYER_SERVE == 1:
        ball.position = Point(bat1.position.x + 1, bat2.position.y + ceil(bat2.length / 2))
    elif PLAYER_SERVE == 2:
        ball.position = Point(bat2.position.x - 1, bat1.position.y + ceil(bat1.length / 2))

def update_game():
    # Collide with the sides
    if ball.position.x >= constants.COLUMNS:
        ball.velocity.x *= -1
        score1.value += 1
    elif ball.position.x <= 0:
        ball.velocity.x *= -1
        score2.value += 1

    # Collide with the ceiling/floor
    if ball.position.y >= constants.ROWS - 1 or ball.position.y <= 0:
        ball.velocity.y *= -1

    if ball.position.x == bat1.position.x + 1 and ball.velocity.x < 0:
        if ball.position.y >= bat1.position.y and ball.position.y <= (bat1.position.y + bat1.length):
            ball.velocity.x *= -1
    elif ball.position.x == bat2.position.x - 1 and ball.velocity.x < 0:
        if ball.position.y >= bat2.position.y and ball.position.y <= (bat2.position.y + bat2.length):
            ball.velocity.x *= -1

    ball.lastposition = Point(ball.position.x, ball.position.y)
    ball.position.x += ball.velocity.x
    ball.position.y += ball.velocity.y


def draw():
    ball.erase()
    bat1.draw()
    bat2.draw()
    net.draw()
    score1.draw()
    score2.draw()
    ball.draw()


bat1 = Bat(3, 3)
bat2 = Bat(77, 3)
net = Net(int(ceil(constants.COLUMNS / 2)), constants.ROWS + 1)
ball = Ball(40 , 6)

score1 = Score(29, 2, 0)
score2 = Score(49, 2, 0)

# Which player is serving/ last served
PLAYER_SERVE = 1
GameState = constants.STATE_IN_PLAY

inputs.init()

while True:
    inputs.update(bat1, bat2, GameState)

    if GameState == constants.STATE_IN_PLAY:
        update_game()
    elif GameState == STATE_SERVE:
        update_serve()

    draw()

    time.sleep(0.1)
