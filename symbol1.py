 #Game of Life

'''
  This is an Implementation by Bergur Thorgeirsson, It seems to be the standard Game of Life Algorithm, at its base.
  The inovation is the additon of different spiecies of cell.  As it is the living cells are not affected directly 
  by the cells of different spiecies, only the dead cells, so static cell structures are not vulnerable to attack from
  cells of other spiecies, only the pulsars and moving blobs are affected. (This may be subject to change in later 
  versions of the program).
'''

"""
The goal of symbol project is to make a GOL implementation, that shows random, unicode symbols
instead of cells


"""


import random
import time
import os
import sys

from symbolSettings import *
from symbolService import *



mswindows = (sys.platform == "win32")
clear = 'clear' # This is what linux uses to clear cmd screen.
if mswindows:
	clear = 'cls'   # This is what windows uses to clear the screen.

theBoard = getNewBoard(BOARDWIDTH, BOARDHEIGHT, BK)
randomPopWholeBoard(theBoard, BOARDWIDTH, BOARDHEIGHT, CELL)
drawBoard(theBoard, BOARDWIDTH, BOARDHEIGHT)
print("This is a randomly generated board.")
# input()

while True:
	theBoard = iterate(theBoard, BOARDWIDTH, BOARDHEIGHT, BK, CHINEASE)
	os.system(clear)
	drawBoard(theBoard, BOARDWIDTH, BOARDHEIGHT)
	time.sleep(0.25)
