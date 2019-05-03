import serialprint
import constants
import inputs
import LEDDisplay
import PiGlow

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

    def draw(self, colour):
        serialprint.setColor(constants.COLOURS["Reset"])
        for y in range(self.position.y):
            serialprint.print_at(y, self.position.x, " ")

        serialprint.setColor(colour)
        for y in range(self.position.y, self.position.y + self.length):
            serialprint.print_at(y, self.position.x, " ")

        serialprint.setColor(constants.COLOURS["Reset"])
        for y in range(self.position.y + self.length, constants.ROWS):
            serialprint.print_at(y, self.position.x, " ")

class Net:
     def __init__(self, x, length):
        self.x = x
        self.length = length

     def draw(self):
        for y in range(0, self.length, 4):
            serialprint.print_at(y,   self.x, "|")
            serialprint.print_at(y+1, self.x, "|")

class Score:
    def __init__(self, x, y, val):
        self.position = Point(x, y)
        self.value = val

    def draw(self, colour):
        self.value = abs(self.value % 10)
        for y in range(5):
            for x in range(3):
                if constants.DIGITS[self.value][y][x] == "X":
                    serialprint.setColor(colour)
                else:
                    serialprint.setColor(constants.COLOURS["Reset"])

                serialprint.print_at(self.position.y + y, self.position.x + x, " ")

class Ball:
    def __init__(self, x, y):
        self.lastposition = Point(x, y)
        self.position = Point(x, y)
        self.velocity = Point(2, 1)

    def erase(self):
        serialprint.print_at(self.lastposition.y, self.lastposition.x, " ")
    def draw(self):
        #serialprint.setColor(colour)
        serialprint.print_at(self.position.y, self.position.x, "o")

# Moves the ball while a player is serving
def update_serve():
    if PLAYER_SERVE == 1:
        ball.position = Point(bat1.position.x + 1, bat1.position.y + ceil(bat1.length / 2))
    elif PLAYER_SERVE == -1:
        ball.position = Point(bat2.position.x - 1, bat2.position.y + ceil(bat2.length / 2))

def setup_serve():
    servesremaining -= 1
    if servesremaining == 0:
        servesremaining = 5
        player_serving *= -1

    game_state = constants.STATE_SERVE

def update_game():
    # Collide with the sides
    if ball.position.x >= constants.COLUMNS:
        ball.velocity.x *= -1
        score1.value += 1
        PiGlow.blueWin()
        #setupServe()

    elif ball.position.x <= 0:
        ball.velocity.x *= -1
        score2.value += 1
        PiGlow.redWin()
        #setup_serve()

    ball.lastposition = Point(ball.position.x, ball.position.y)
    ball.position.x += ball.velocity.x
    ball.position.y += ball.velocity.y

    ball.position.y = max(ball.position.y, 0)
    ball.position.y = min(ball.position.y, constants.ROWS)

    # Collide with the ceiling/floor
    if ball.position.y >= constants.ROWS - 1 or ball.position.y <= 0:
        ball.velocity.y *= -1

    if ball.position.x == bat1.position.x + 1 and ball.velocity.x < 0:
        if ball.position.y >= bat1.position.y and ball.position.y <= (bat1.position.y + bat1.length):
            ball.velocity.x *= -1

            # Calculate which 1/3 of the bat was hit, and adjust velocity accordingly.
            hitposition = (bat1.position.y - ball.position.y) / (bat1.length/3)
            ball.velocity.y = hitposition - 2

    elif ball.position.x == bat2.position.x - 1 and ball.velocity.x > 0:
        if ball.position.y >= bat2.position.y and ball.position.y <= (bat2.position.y + bat2.length):
            ball.velocity.x *= -1


def draw():

    serialprint.setColor(constants.COLOURS["Net"])
    net.draw()

    bat1.draw(constants.COLOURS["BlueBat"])
    score1.draw(constants.COLOURS["BlueScore"])

    bat2.draw(constants.COLOURS["RedBat"])
    score2.draw(constants.COLOURS["RedScore"])


    serialprint.setColor(constants.COLOURS["Reset"])
    ball.erase()
    ball.draw()


bat1 = Bat(3, 3)
bat2 = Bat(77, 3)
net = Net(int(ceil(constants.COLUMNS / 2)), constants.ROWS + 1)
ball = Ball(40 , 6)

score1 = Score(29, 2, 0)
score2 = Score(49, 2, 0)

# Which player is serving/ last served
player_serving = 1
game_state = constants.STATE_IN_PLAY

servesremaining = constants.SERVES

LEDDisplay.init()
inputs.init()
serialprint.setColor(constants.COLOURS["Reset"])
draw()
LEDDisplay.countdown7seg()

while True:
    inputs.update(bat1, bat2, game_state)

    if game_state == constants.STATE_IN_PLAY:
        update_game()

    elif game_state == constants.STATE_SERVE:
        update_serve()

    draw()
    LEDDisplay.updateBoard(ball.position.x)
    time.sleep(0.1)
