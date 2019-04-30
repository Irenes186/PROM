STATE_IN_PLAY = 0
STATE_SERVE = 1

ROWS = 24 
COLUMNS = 80 
SERVES = 5

COLOURS = {
    "BlueBat": 46,
    "BlueScore": 34,
    "RedBat": 41,
    "RedScore": 30,
    "Reset": 0
}

PINS = {
    "Buzzer": 12, # Needs to be a PWM pin
    "7-Seg Low": 0,
    "7-Seg High": 0,
    "7-Seg Enable": 0,
    "IO Expander SCL": 0,
    "IO Expander SDA": 0,
    }

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
