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

from settingsPygame2 import *
from golService import *

pygame.init()

dispWidth = 600
dispHeight = 600

cellSizeX =   dispWidth / BOARDWIDTH 
cellSizeY =   dispHeight / BOARDHEIGHT
fps = 5 


def drawCell(coords, color):
	for coord in coords:
		x = coord['x']*cellSizeX
		y = coord['y']*cellSizeY
		makeCell = pygame.Rect(x,y,cellSizeX, cellSizeY)
		pygame.draw.rect(setDisplay, color, makeCell)

def drawBoardPy(board, boardwidth, boardheight):
	for x in range(boardwidth):
		for y in range(boardheight):
			drawCell([{'x':x, 'y':y}],CELLDICT[board[x][y]])
			


def runGame():

	# setup
	theBoard = getNewBoard(BOARDWIDTH, BOARDHEIGHT, "o")
	smallRandomPop(theBoard, BOARDWIDTH, BOARDHEIGHT, "r", DELTA1)
	smallRandomPop2(theBoard, BOARDWIDTH, BOARDHEIGHT, "g", DELTA1)
	smallRandomPop3(theBoard, BOARDWIDTH, BOARDHEIGHT, "b", DELTA1)
	smallRandomPop4(theBoard, BOARDWIDTH, BOARDHEIGHT, "p", DELTA1)
	
	
	drawBoardPy(theBoard,BOARDWIDTH,BOARDHEIGHT)
	pygame.display.update()

	gameLoop = True
	pause = False
	while gameLoop:
		for event in pygame.event.get():
			if event.type == QUIT:
				gameLoop = False
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
					if event.key == K_p:
						pause = not pause
				
		fpsTime.tick(fps)
		if(not pause):
			theBoard = iterate(theBoard, BOARDWIDTH, BOARDHEIGHT, BK, CELLS)
		drawBoardPy(theBoard,BOARDWIDTH,BOARDHEIGHT)
		pygame.display.update()
					


while True:
	global fpsTime
	global setDisplay


	fpsTime = pygame.time.Clock()
	setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
	pygame.display.set_caption('Python Pygame of Life')
	runGame()
