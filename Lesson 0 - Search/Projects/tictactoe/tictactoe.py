"""
Tic Tac Toe Player
"""

import math
import random

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
    """
    Returns player who has the next turn on a board.
    """
    empty_fields = 0
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] is EMPTY:
                empty_fields += 1

    if empty_fields % 2 == 1:
        return X
    else:
        return O

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    i = 0
    for row in range(0, 2):
        for col in range(0, 2):
            if board[row][col] is EMPTY:
                actions.append((row, col))
    return actions
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board
    #raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in range(0, 2):
        if board[row][0] is not EMPTY \
            and board[row][0] == board[row][1] \
            and board[row][0] == board[row][2]:
            print("Three in a row")
            return board[row][0]
    
    for col in range(0, 2):
        if board[0][col] is not EMPTY \
            and board[0][col] == board[1][col] \
            and board[0][col] == board[2][col]:
            print("Three in a col")
            return board[0][col]

    if board[0][0] is not EMPTY \
        and board[0][0] == board[1][1] \
        and board[0][0] == board[2][2]:
        print("Diagonal 1")
        return board[0][0]

    if board[2][0] is not EMPTY \
        and board[2][0] == board[1][1] \
        and board[2][0] == board[0][2]:
        print("Diagonal 2")
        return board[2][0]

    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in range(0, 2):
        for col in range(0, 2):
            if board[row][col] is EMPTY:
                return False
    return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    moves = actions(board)
    return moves[random.randrange(0, len(moves))]
    #raise NotImplementedError
