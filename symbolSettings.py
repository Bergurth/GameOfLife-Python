CELL = 'O' # The cell character
CELL2 = 'Z' 
BK = ' '   # The background Character
BK_HAN = '  '
DED = 'X'  # The dead cell character
CELLS = ['#','O','Z','S','~'] 

try:
    get_char = unichr
except NameError:
    get_char = chr


#HAN = get_char(0x4DFF)
HAN = get_char(0x7121)  # nothing chinease
#HAN = get_char(0x3080)  # nothin japanease



"""
BOARDWIDTH = 100
BOARDHEIGHT = 48
"""
import console
(BOARDWIDTH, BOARDHEIGHT) = console.getTerminalSize()

EAST_ASIAN_BOARDWIDTH = BOARDWIDTH / 2

# delta is the width of populations
DELTA1 = 10

CHAR_INCLUDE_RANGE = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
        
    ]

CHINEASE = [
        ( 0x4E00, 0x9FFF ),
#        ( 0x3400, 0x4DFF ),
    ]

# 3040-309f and 30a0-30ff
JAPANEASE = [
    #(0x4e00,0x9fbf),
    #(0x3400,0x4DFF),
    #(0x30a0,0x30ff),
    (0x30a0, 0x30ff),
]

KOREAN = [
    (0xAC00,0xD7AF),
    (0x1100,0x11FF),
]

LANGUAGES = {"chinease":CHINEASE, "japanease":JAPANEASE, "korean":KOREAN}
"""

    Japanese-style punctuation ( 3000 - 303f)
    Hiragana ( 3040 - 309f)  <----- pretty japanease looking
    Katakana ( 30a0 - 30ff)  <----- even more japanease looking
    Full-width roman characters and half-width katakana ( ff00 - ffef)
    CJK unifed ideographs - Common and uncommon kanji ( 4e00 - 9faf)
    

"""
