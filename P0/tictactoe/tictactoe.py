"""
Tic Tac Toe Player
"""
import pdb
import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
def player(board):
    xs = sum(row.count(X) for row in board)
    os = sum(row.count(O) for row in board)
    if xs > os:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = deepcopy(board)
    if newboard[action[0]][action[1]] != EMPTY:
        raise Exception 

    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows and cols
    for i in range(3):
        row = board[i]
        col = [None]*3
        for j in range(3):
            col[j] = board[j][i]

        if row[0] == row[1] and row[1] == row[2] and row[0] != EMPTY:
            return row[0]
        if col[0] == col[1] and col[1] == col[2] and col[0] != EMPTY:
            return col[0]
    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        if actions(board) == []:
            return True
        return False
    else:
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    pot_actions = actions(board)
    utilities = [0]*len(pot_actions)

    for i in range(len(pot_actions)):
        utilities[i] = rec_utility(result(board,pot_actions[i]))

    if player(board) == X:
        return pot_actions[utilities.index(max(utilities))]
    else:
        return pot_actions[utilities.index(min(utilities))]


def rec_utility(board):
    if terminal(board):
        return utility(board)
    else:
        pot_actions = actions(board)
        utilities = [0]*len(pot_actions)
        for i in range(len(pot_actions)):
            utilities[i] = rec_utility(result(board,pot_actions[i]))
        if player(board) == X:
            return max(utilities)
        else:
            return min(utilities)
