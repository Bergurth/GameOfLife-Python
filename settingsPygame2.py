"""
   Settings file for pygame version of Game of Life
"""
#colors
white =	(255,255,255)
black =	(0,0,0)
cyan = (255,255,0)
red = (255,25,25)
green = (25,255,25)
blue = (25,25,255)
purple = (255,0,255)

CELL = 'O' # The cell character
CELL2 = 'Z' 
BK = "o"   # The background Character
DED = black  # The dead cell character
#CELLDICT maps character symbols to colors
CELLDICT = {"w":white,"r":red,"g":green,"b":blue,"c":cyan,"p":purple,"o":black}
CELLS = ["r","g","b","p","c"] 
BOARDWIDTH = 140
BOARDHEIGHT = 140
# delta is the width of the random pops
DELTA1 = 10
CELLSIZE = 10
