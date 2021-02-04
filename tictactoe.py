"""
Tic Tac Toe Player
"""

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
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        turns_taken = 0
        for line in board:
            for sq in line:
                if sq:
                    turns_taken += 1

        if turns_taken % 2 == 0:
            return X
        else:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_squares = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_squares.add((i, j))
    print(empty_squares)
    return empty_squares


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception

    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for r in board:
        if len(set(r)) == 1:
            return r[0]
    
    if len(set([board[i][i] for i in range(3)])) == 1:
        return board[0][0]
    
    if len(set([board[i][-(i + 1)] for i in range(3)])) == 1:
        return board[0][-1]

    rotated = board.copy()
    for r in range(3):
        for c in range(3):
            rotated[c][r] = board[r][c]
    
    for r in rotated:
        if len(set(r)) == 1:
            return r[0]
            
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for r in board:
        if EMPTY in r:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result is not None:
        if result == X:
            return 1
        else:
            return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    possible_moves = actions(board)
    move = possible_moves.pop()
    return move
