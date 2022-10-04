from tictactoe import *


def print_results(board, player):
    result = winner(board)
    if not terminal(board):
        print("Winner:\t", result)
        print("isTerminal:\t", terminal(board))
        exit()

    if winner(board) != player:
        print("Winner:\t", result)
        print("outcome:", utility(board))
        exit()

def main():
    """
    for player in [X, O]:
        print("First Row")
        board = [
            [player,    player,   player],
            [EMPTY,     EMPTY,    EMPTY],
            [EMPTY,     EMPTY,    EMPTY]
        ]
        print_results(board, player)

        print("Second Row")
        board = [
            [EMPTY,    EMPTY,    EMPTY],
            [player,   player,   player],
            [EMPTY,    EMPTY,    EMPTY]
        ]
        print_results(board, player)

        print("Third Row")
        board = [
            [EMPTY,    EMPTY,    EMPTY],
            [EMPTY,    EMPTY,    EMPTY],
            [player,   player,   player]
        ]
        print_results(board, player)

        print("First Col")
        board = [
            [player,    EMPTY,    EMPTY],
            [player,    EMPTY,    EMPTY],
            [player,    EMPTY,    EMPTY]
        ]
        print_results(board, player)

        print("Second Col")
        board = [
            [EMPTY,    player,    EMPTY],
            [EMPTY,    player,    EMPTY],
            [EMPTY,    player,    EMPTY]
        ]
        print_results(board, player)

        print("Third Col")
        board = [
            [EMPTY,    EMPTY,    player],
            [EMPTY,    EMPTY,    player],
            [EMPTY,    EMPTY,    player]
        ]
        print_results(board, player)

        print("Right-To-Left")
        board = [
            [EMPTY,     EMPTY,  player],
            [EMPTY,     player, EMPTY],
            [player,    EMPTY,  EMPTY]
        ]
        print_results(board, player)

        print("Left-To-Right")
        board = [
            [player,    EMPTY,  EMPTY],
            [EMPTY,     player, EMPTY],
            [EMPTY,     EMPTY,  player]
        ]
        print_results(board, player)
    """
    print("Tie?")
    board = [
        [X,    O,  EMPTY],
        [O,     O, EMPTY],
        [EMPTY, X,     X]
    ]
    print_results(board, player)

if __name__ == "__main__":
    main();