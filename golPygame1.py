 #Game of Life

'''
  This is an Implementation by Bergur Thorgeirsson, It seems to be the standard Game of Life Algorithm, at its base.
  The inovation is the additon of different spiecies of cell.  As it is the living cells are not affected directly 
  by the cells of different spiecies, only the dead cells, so static cell structures are not vulnerable to attack from
  cells of other spiecies, only the pulsars and moving blobs are affected. (This may be subject to change in later 
  versions of the program).
'''

import random
import time
import os
import sys
import pygame

from pygame.locals import *

from settingsPygame import *
from golService import *

pygame.init()

dispWidth = 800
dispHeight = 600

cellSizeX =   dispWidth / BOARDWIDTH 
cellSizeY =   dispHeight / BOARDHEIGHT
fps = 30


def drawCell(coords, color):
	for coord in coords:
		x = coord['x']*cellSizeX
		y = coord['y']*cellSizeY
		makeCell = pygame.Rect(x,y,cellSizeX, cellSizeY)
		pygame.draw.rect(setDisplay, color, makeCell)

def drawBoardPy(board, boardwidth, boardheight):
	for x in range(boardwidth):
		for y in range(boardheight):
			drawCell([{'x':x, 'y':y}],board[x][y])
			print board[x][y]


def runGame():

	#coords = [{'x':startx, 'y':starty}]

	# setup
	theBoard = getNewBoard(BOARDWIDTH, BOARDHEIGHT, BK)
	smallRandomPop(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[1], DELTA1)
	smallRandomPop2(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[2], DELTA1)
	smallRandomPop3(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[0], DELTA1)
	smallRandomPop4(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[3], DELTA1)
	drawCell([{'x':3,'y':4}],(255,25,25))
	pygame.display.update()
	#drawBoard(theBoard,BOARDWIDTH,BOARDHEIGHT)
	drawBoardPy(theBoard,BOARDWIDTH,BOARDHEIGHT)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			else:
				fpsTime.tick(fps)
				theBoard = iterate(theBoard, BOARDWIDTH, BOARDHEIGHT, BK, CELLS)
				drawBoardPy(theBoard,BOARDWIDTH,BOARDHEIGHT)
				pygame.display.update()
					


"""
			else:




			coords.insert(0, newCell)
			setDisplay.fill(bg)
			drawCell(coords)
			setDisplay.blit(catImages[cImageNum], (coords[0]['x'] * cheetaSpeed ,coords[0]['y'] * cheetaSpeed))
			pygame.display.update()
			fpsTime.tick(fps)
			IMAGENUM += 1
			if (IMAGENUM % 3 == 0):
				cImageNum += 1
				cImageNum = cImageNum % 8
				catImage = catImages[cImageNum]
"""

while True:
	global fpsTime
	global setDisplay


	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_caption('Python Pygame of Life')
	runGame()

# olden stuff
"""
mswindows = (sys.platform == "win32")
clear = 'clear' # This is what linux uses to clear cmd screen.
if mswindows:
	clear = 'cls'   # This is what windows uses to clear the screen.

theBoard = getNewBoard(BOARDWIDTH, BOARDHEIGHT, BK)
smallRandomPop(theBoard, BOARDWIDTH, BOARDHEIGHT, CELL, DELTA1)
smallRandomPop2(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[2], DELTA1)
smallRandomPop3(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[0], DELTA1)
smallRandomPop4(theBoard, BOARDWIDTH, BOARDHEIGHT, CELLS[3], DELTA1)
drawBoard(theBoard, BOARDWIDTH, BOARDHEIGHT)
print("This is a randomly generated board.")
# input()

while True:
	theBoard = iterate(theBoard, BOARDWIDTH, BOARDHEIGHT, BK, CELLS)
	os.system(clear)
	drawBoard(theBoard, BOARDWIDTH, BOARDHEIGHT)
	time.sleep(0.25)
"""
