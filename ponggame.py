import serialprint
import constants
import inputs
import LEDDisplay
import PiGlow
import random
import time
import Buzzer
from math import ceil

# Which player is serving/ last served
player_serving = 1
game_state = constants.STATE_IN_PLAY
servesremaining = constants.SERVES + 1

is_winner = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bat:
    def __init__(self, xpos, length):
        self.position = Point(xpos, 0)
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
        for y in range(1, self.length, 4):
            serialprint.print_at(y,   self.x, "|")
            serialprint.print_at(y+1, self.x, "|")

class Score:
    def __init__(self, x, y, val):
        self.position = Point(x, y)
        self.value = val

    def draw(self, colour):
        printval = abs(self.value % 10)
        serialprint.setColor(colour)

        for y in range(5):
            for x in range(3):
                if constants.DIGITS[printval][y][x] == "X":
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

def setup_serve():
    global servesremaining, game_state, player_serving
    servesremaining -= 1
    if servesremaining == 0:
        servesremaining = constants.SERVES
        player_serving *= -1

    serialprint.clear()

    game_state = constants.STATE_SERVE

# Moves the ball while a player is serving
def update_serve():
    global player_serving, ball, bat1, bat2
    if player_serving == 1:
        ball.lastposition = Point(ball.position.x, ball.position.y)
        ball.position.x = bat1.position.x + 1
        ball.position.y = int(bat1.position.y + ceil(bat1.length / 2))
        ball.velocity = Point(2, 0)
    elif player_serving == -1:
        ball.lastposition = Point(ball.position.x, ball.position.y)
        ball.position.x = bat2.position.x - 1
        ball.position.y = int(bat2.position.y + ceil(bat2.length / 2))
        ball.velocity = Point(-2, 0)

def update_game():
    global servesremaining, game_state
    # Collide with the sides
    if ball.position.x >= constants.COLUMNS:
        ball.velocity.x *= -1
        score1.value += 1
        PiGlow.blueWin()
        Buzzer.playTone(constants.left_right , 0.15)
        setup_serve()

    elif ball.position.x <= 0:
        ball.velocity.x *= -1
        score2.value += 1
        PiGlow.redWin()
        Buzzer.playTone(constants.left_right, 0.15)
        setup_serve()

    ball.lastposition = Point(ball.position.x, ball.position.y)
    ball.position.x += ball.velocity.x
    ball.position.y += ball.velocity.y

    ball.position.y = max(ball.position.y, 0)
    ball.position.y = min(ball.position.y, constants.ROWS)

    # Collide with the ceiling/floor
    if ball.position.y >= constants.ROWS - 1 or ball.position.y <= 0:
        ball.velocity.y *= -1
        Buzzer.playTone(constants.up_down, 0.25)


    if ball.position.x == bat1.position.x + 1 and ball.velocity.x < 0:
        if ball.position.y >= bat1.position.y and ball.position.y < (bat1.position.y + bat1.length):
            if constants.randomSpeed:
                ball.velocity.x = random.randint(1,3)
            else:
                ball.velocity.x = 1

            Buzzer.playTone(constants.touch_bat_blue, 0.25)

            positiononbat = int(bat1.position.y - ball.position.y)

            if bat1.length == 3:
                if positiononbat == 0:
                    ball.velocity.y = -1
                elif positiononbat == -1:
                    ball.velocity.y = 0
                elif positiononbat == -2:
                    ball.velocity.y = 1
                else:
                    pass
            else:
                if (positiononbat == 0) or (positiononbat == -1):
                    ball.velocity.y = -1
                elif (positiononbat == -2) or (positiononbat == -3):
                    ball.velocity.y = 0
                elif (positiononbat == -4) or (positiononbat == -5):
                    ball.velocity.y = 1
                else:
                    pass

    elif ball.position.x == bat2.position.x - 1 and ball.velocity.x > 0:
        if ball.position.y >= bat2.position.y and ball.position.y < (bat2.position.y + bat2.length):
            if constants.randomSpeed:
                ball.velocity.x = -random.randint(1,3)
            else:
                ball.velocity.x = -1

            Buzzer.playTone(constants.touch_bat_red, 0.25)

            positiononbat = int(bat2.position.y - ball.position.y)

            if bat2.length == 3:
                if positiononbat == 0:
                    ball.velocity.y = -1
                elif positiononbat == -1:
                    ball.velocity.y = 0
                elif positiononbat == -2:
                    ball.velocity.y = 1
                else:
                    pass
            else:
                if (positiononbat == 0) or (positiononbat == -1):
                    ball.velocity.y = -1
                elif (positiononbat == -2) or (positiononbat == -3):
                    ball.velocity.y = 0
                elif (positiononbat == -4) or (positiononbat == -5):
                    ball.velocity.y = 1
                else:
                    pass

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

def checkWinner():
    global is_winner

    if score1.value >= constants.WINNER_SCORE:
		#printing function
		message = constants.WINNER[1]
		is_winner = True
    elif score2.value >= constants.WINNER_SCORE:
		#printing function
		message = constants.WINNER[0]
		is_winner = True

    if (is_winner):
        if score1.value == constants.WINNER_SCORE:
            serialprint.setColor(constants.COLOURS["BlueScore"])
        else:
            serialprint.setColor(constants.COLOURS["RedScore"])

        for y in range(5):
             for x in range(len(message[0])):
                  if message[y][x] == "X":
                   serialprint.print_at(9 + y, 24 + x, " ")


bat1 = Bat(3, 3)
bat2 = Bat(77, 3)
net = Net(int(ceil(constants.COLUMNS / 2)), constants.ROWS)
ball = Ball(40 , 6)
score1 = Score(29, 2, 0)
score2 = Score(49, 2, 0)

LEDDisplay.init()
inputs.init()
serialprint.setColor(constants.COLOURS["Reset"])
draw()
if constants.showcountdown:
    LEDDisplay.countdown7seg() #Three second timer

setup_serve()

while is_winner == False:
    inputarr = [game_state, player_serving]
    inputs.update(bat1, bat2, inputarr)
    game_state = inputarr[0]


    if game_state == constants.STATE_IN_PLAY:
        update_game()
    elif game_state == constants.STATE_SERVE:
        update_serve()

    draw()
    checkWinner()
    LEDDisplay.updateBoard(ball.position.x)
    #time.sleep(0.05)
