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
HAN = get_char(0x7121)  # nothing


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
