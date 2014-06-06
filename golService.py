"""


Core service functions


"""
import random


def getNewBoard(boardwidth, boardheight, backgroundChar):
	# Create a  new 200X60 data structure
	board = []
	for x in range(boardwidth):
		board.append([])
		for y in range(boardheight):
			board[x].append(backgroundChar)

	return board


def drawBoard(board, boardwidth, boardheight):

	#print '\n' * 5
	hline = '    '
	for i in range(boardwidth / 10):
		hline += (' ' * 9) + str(i)
	
	print(hline)
	print('   ' + ('0123456789' * (boardwidth / 10)))

	for i in range(boardheight):
		if i < 10 :
			extraSpace = ' '
		else:
			extraSpace = ''

		print('%s%s %s %s' % (extraSpace, i, getRow(board,i,boardwidth), i))

	print('   ' + ('0123456789' * (boardwidth / 10)))
	print(hline)


def getRow(board, row, boardwidth):
	# Return a string from the board data structure at a certain row.
	boardRow = ''
	for i in range(boardwidth):
		boardRow += board[i][row]
	return boardRow


def getBoardCopy(board):
	dupeBoard = []
	for x in board:
		dupeBoard.append(x)
	return dupeBoard

def shouldBeNext(board, x, y, cells, backgroundChar):
	Neibs = [board[x-1][y-1],board[x][y-1],board[x+1][y-1],board[x-1][y],board[x+1][y],board[x-1][y+1],board[x][y+1],board[x+1][y+1]]
	if board[x][y] in cells:
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
		if (board[x-1][y-1] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x][y-1] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x+1][y-1] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x-1][y] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x+1][y] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x-1][y+1] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x][y+1] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		if (board[x+1][y+1] != cell) and board[x-1][y-1] in cells:
			EnN += 1
		'''
		if (liveN < 2):
			return backgroundChar
		if (liveN == 2 and board[x][y] != cell):
			return backgroundChar
		if (liveN+EnN > 3):
			return backgroundChar
		else:
			return cell

	else:
		adjCount = []
		for i in range(len(cells)):
			adjCount.append(0)
		for i in range(len(Neibs)):
			for u in range(len(cells)):
				if Neibs[i] == cells[u]:
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
			return backgroundChar

		elif ( (4 > adjCount[highestPlace] > 2) and (sum(adjCount) < 4)):
			return cells[highestPlace]
		
		else:
			return backgroundChar


def iterate(board, boardwidth, boardheight, backgroundChar, cells):
	newB = getNewBoard(boardwidth, boardheight, backgroundChar)
	for x in range(boardwidth - 1):
		for y in range(boardheight - 1):
			newB[x][y] = shouldBeNext(board, x, y, cells, backgroundChar)
	return newB

"""
pOPULATIONS
"""

def smallRandomPop(board, boardwidth, boardheight, cell, delta):

    placeX = boardwidth / 4 
    placeY = boardheight / 4
    for x in range(placeX, placeX + delta):
	    for y in range(placeY, placeY + delta):
		    if random.randint(0,1) ==1:
			    board[x][y] = cell


def smallRandomPop2(board, boardwidth, boardheight, cell, delta):
	placeX = 3 * boardwidth / 4
	placeY = 3 * boardheight / 4
	for x in range(placeX,placeX+delta):
		for y in range(placeY,placeY+delta):
			if random.randint(0,1) ==1:
				board[x][y] = cell

def smallRandomPop3(board, boardwidth, boardheight, cell, delta):
	placeX = 3 * boardwidth / 4
	placeY = boardheight / 4
	for x in range(placeX,placeX+delta):
		for y in range(placeY,placeY+delta):
			if random.randint(0,1) ==1:
				board[x][y] = cell

def smallRandomPop4(board, boardwidth, boardheight, cell, delta):
	placeX = boardwidth / 4
	placeY = 3 * boardheight / 4
	for x in range(placeX,placeX+delta):
		for y in range(placeY,placeY+delta):
			if random.randint(0,1) ==1:
				board[x][y] = cell