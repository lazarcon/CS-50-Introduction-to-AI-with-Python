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
    for row in range(0, len(board)):
        for col in range(0, len(board)):
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
    for row in range(0, len(board)):
        if board[row][0] is not EMPTY \
            and board[row][0] == board[row][1] \
            and board[row][0] == board[row][2]:
                return board[row][0]

    for col in range(0, len(board)):
        if board[0][col] is not EMPTY \
            and board[0][col] == board[1][col] \
            and board[0][col] == board[2][col]:
                return board[0][col]

    if board[0][0] is not EMPTY \
        and board[0][0] == board[1][1] \
        and board[0][0] == board[2][2]:
            return board[0][0]

    if board[2][0] is not EMPTY \
        and board[2][0] == board[1][1] \
        and board[2][0] == board[0][2]:
            return board[2][0]

    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Game is over if there is a winner
    if winner(board):
        return True

    # Game is not over if there is no winner and at least an empty field
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            if board[row][col] is EMPTY:
                return False

    # No winner and no fields left thus, the game is over.
    return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    outcome = winner(board)
    if outcome == X:
        return 1
    elif outcome == O:
        return -1
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    """
        - The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
        - The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).
    """
    if player(board) == X:
        actions = actions(board)

    #raise NotImplementedError

def max_value(board):
    # v = -∞
    v = -99
    
    # if Terminal(state):
    if terminal(board):
        #return Utility(state)
        return utility(board)

    #for action in Actions(state):
    for action in actions(board):
        #v = Max(v, Min-Value(Result(state, action)))
        v = max(v, min_value(result(board, action)))
    #return v
    return v

def min_value(board):
    # v = -∞
    v = 99

    # if Terminal(state):
    if terminal(board):
        #return Utility(state)
        return utility(board)

    #for action in Actions(state):
    for action in actions(board):
        #v = Min(v, Max-Value(Result(state, action)))
        v = min(v, max_value(result(board, action)))
    #return v
    return v

def dummy(board):
    """
    Returns the optimal action for the current player on the board.
    """
    moves = actions(board)
    return moves[random.randrange(0, len(moves))]
    #raise NotImplementedError
