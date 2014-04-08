
# Game of Life

'''
  This is an Implementation by Bergur Thorgeirsson, It seems to be the standard Game of Life Algorithm.
'''

import random
import time
import os
import sys


CELL = 'O' # The cell character
CELL2 = 'Z'
BK = '+'   # The background Character
DED = 'X'  # The dead cell character
CELLS = [' ','O','Z'] 


def getNewBoard():
	# Create a  new 200X60 data structure
	board = []
	for x in range(100):
		board.append([])
		for y in range(60):
			board[x].append(BK)

	return board


def randomPopulateBoard(board):

	for x in range(1,99):
		for y in range(1, 59):
			if random.randint(0, 1) == 1:
				board[x][y] = CELL


def smallRandomPop(board):

	for x in range(40,50):
		for y in range(40,50):
			if random.randint(0,1) ==1:
				board[x][y] = CELL


def drawBoard(board):
	
	hline = '    '
	for i in range(1, 10):
		hline += (' ' * 9) + str(i)
	
	print(hline)
	print('   ' + ('0123456789' * 10))

	for i in range(60):
		if i < 10 :
			extraSpace = ' '
		else:
			extraSpace = ''

		print('%s%s %s %s' % (extraSpace, i, getRow(board,i), i))

	print()
	print('   ' + ('0123456789' * 10))
	print(hline)




def getRow(board, row):
	# Return a string from the board data structure at a certain row.
	boardRow = ''
	for i in range(100):
		boardRow += board[i][row]
	return boardRow


def getBoardCopy(board):
	dupeBoard = []
	for x in board:
		dupeBoard.append(x)
	return dupeBoard

def insertCell(board, cell, x, y):
	board[x][y] = cell


def shouldLive(board, cell, x, y):
	liveN = 0 #liveN stands for Live Neighbors
	EnN = 0  #Enemy neigbors
	if (board[x-1][y-1] == cell):
		liveN += 1
	if (board[x][y-1] == cell):
		liveN += 1
	if (board[x+1][y-1] == cell):
		liveN += 1
	if (board[x-1][y] == cell):
		liveN += 1
	if (board[x+1][y] == cell):
		liveN += 1
	if (board[x-1][y+1] == cell):
		liveN += 1
	if (board[x][y+1] == cell):
		liveN += 1
	if (board[x+1][y+1] == cell):
		liveN += 1
	
	if (board[x-1][y-1] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x][y-1] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x+1][y-1] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x-1][y] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x+1][y] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x-1][y+1] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x][y+1] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1
	if (board[x+1][y+1] != cell) and board[x-1][y-1] in CELLS:
		EnN += 1

	if (liveN < 2):
		return '+'
	if (liveN == 2 and board[x][y] != cell):
		return '+'
	if (liveN+EnN > 3):
		return '+'
	else:
		return cell


def shouldBeNext(board, x, y):
	Neibs = [board[x-1][y-1],board[x][y-1],board[x+1][y-1],board[x-1][y],board[x+1][y],board[x-1][y+1],board[x][y+1],board[x+1][y+1]]
	if board[x][y] in CELLS:
		cell = board[x][y]
		
		liveN = 0 #liveN stands for Live Neighbors
		EnN = 0  #Enemy neigbors
		if (board[x-1][y-1] == cell):
			liveN += 1
		if (board[x][y-1] == cell):
			liveN += 1
		if (board[x+1][y-1] == cell):
			liveN += 1
		if (board[x-1][y] == cell):
			liveN += 1
		if (board[x+1][y] == cell):
			liveN += 1
		if (board[x-1][y+1] == cell):
			liveN += 1
		if (board[x][y+1] == cell):
			liveN += 1
		if (board[x+1][y+1] == cell):
			liveN += 1
		'''	
		if (board[x-1][y-1] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x][y-1] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x+1][y-1] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x-1][y] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x+1][y] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x-1][y+1] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x][y+1] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		if (board[x+1][y+1] != cell) and board[x-1][y-1] in CELLS:
			EnN += 1
		'''
		if (liveN < 2):
			return '+'
		if (liveN == 2 and board[x][y] != cell):
			return '+'
		if (liveN+EnN > 3):
			return '+'
		else:
			return cell

	else:
		adjCount = []
		for i in range(len(CELLS)):
			adjCount.append(0)
		for i in range(len(Neibs)):
			for u in range(len(CELLS)):
				if Neibs[i] == CELLS[u]:
					adjCount[u] += 1

		# Next we evaluate the species, see who wins to determine the cell speicies or lack there of.
		highestPlace = (-1)
		for i in range(len(adjCount)):
			if adjCount[i] > highestPlace:
				highestPlace = i 

		equals = 0
		for i in range(len(adjCount)):
			if adjCount[i] == adjCount[highestPlace]:
				equals += 1

		if equals > 1:
			return '+'

		elif ( (4 > adjCount[highestPlace] > 2) and (sum(adjCount) < 4)):
			return CELLS[highestPlace]
		
		else:
			return '+'

def iterate(board):
	newB = getNewBoard()
	for x in range(1,99):
		for y in range(1,59):
			newB[x][y] = shouldBeNext(board, x, y)
	return newB



# Testing 1
'''
theBoard = getNewBoard()
drawBoard(theBoard)
insertCell(theBoard, 10,50)
drawBoard(theBoard)
newB = getBoardCopy(theBoard)
print('Drawing duplicateBoard')
drawBoard(newB)
insertCell(newB, 11,50)
insertCell(newB, 12,50)
insertCell(newB, 11,51)
insertCell(newB, 11,49)
drawBoard(newB)
print('Do you want to iterate')
input()
print()
print(CELL)
print()
print(newB[11][49])
print()
if newB[11][49] == CELL:
	print('bla')
print()
newB2 = iterate(newB)
drawBoard(newB2)
input()
while True:
	print('Iterate again?')
	input()
	newB2 = iterate(newB2)
	drawBoard(newB2)
	input()


'''

# Testing 2


mswindows = (sys.platform == "win32")
clear = 'clear' # This is what linux uses to clear cmd screen.
if mswindows:
	clear = 'cls'   # This is what windows uses to clear the screen.

theBoard = getNewBoard()
smallRandomPop(theBoard)
drawBoard(theBoard)
print("This is a randomly generated board.")
input()

while True:
	theBoard = iterate(theBoard)
	os.system(clear)
	drawBoard(theBoard)
	time.sleep(0.25)






