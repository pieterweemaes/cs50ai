from minesweeper import *

board = []
for i in range(3):
	row = []
	for j in range(3):
		row.append(False)
	board.append(row)

mines = set()
while len(mines) != 3:
    i = random.randrange(3)
    j = random.randrange(3)
    if not board[i][j]:	
        mines.add((i, j))
        board[i][j] = True

ASentence = Sentence([(1,1)],0)
ASentence.mark_mine((1,1))