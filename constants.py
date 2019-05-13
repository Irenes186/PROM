STATE_IN_PLAY = 0
STATE_SERVE = 1

ROWS = 24
COLUMNS = 80
SERVES = 5
WINNER_SCORE = 10

showcountdown = False
randomSpeed = True

#######SOUNDS#########
winner = 850
up_down = 440
left_right = 330
touch_bat_blue = 1000
touch_bat_red = 1200

#########ADC#########

ADC_lowend = 950
ADC_highend = 3100
ADC_levelsrequired = 22

#########ADC#########

COLOURS = {
    "BlueBat": 46,
    "BlueScore": 104,
    "RedBat": 41,
    "RedScore": 101,
    "Net" : 92,
    "Reset": 0
}

PINS = {
    "Buzzer": 10, # Needs to be a PWM pin
    "7-Seg Low": 0,
    "7-Seg High": 0,
    "7-Seg Enable": 0,
    "IO Expander SCL": 0,
    "IO Expander SDA": 0,
    }


WINNER = [
    [
        "  XX  XXX XX     X   X XXX X   X",
        "  X X X   X X    X   X X X XX  X",
        "  XX  XXX X X    X   X X X X X X",
        "  X X X   X X    X X X X X X  XX",
        "  X X XXX XX     XX XX XXX X   X"
    ],
    [
        "XXX X   X X XXX   X   X XXX X   X",
        "X X X   X X X     X   X X X XX  X",
        "XX  X   X X XX    X   X X X X X X",
        "X X X   X X X     X X X X X X  XX",
        "XXX XXX XXX XXX   XX XX XXX X   X",
    ],
    ]

DIGITS = [
    [
        "XXX",
        "X X",
        "X X",
        "X X",
        "XXX",
    ],
    [
        " X ",
        "XX ",
        " X ",
        " X ",
        "XXX",
    ],
    [
        "XXX",
        "  X",
        "XXX",
        "X  ",
        "XXX",
    ],
    [
        "XXX",
        "  X",
        " XX",
        "  X",
        "XXX",
    ],
    [
        "X X",
        "X X",
        "XXX",
        "  X",
        "  X",
    ],
    [
        "XXX",
        "X  ",
        "XXX",
        "  X",
        "XXX",
    ],
    [
        "XXX",
        "X  ",
        "XXX",
        "X X",
        "XXX",
    ],
    [
        "XXX",
        "  X",
        "  X",
        "  X",
        "  X",
    ],
    [
        "XXX",
        "X X",
        "XXX",
        "X X",
        "XXX",
    ],
    [
        "XXX",
        "X X",
        "XXX",
        "  X",
        "  X",
    ],
]
