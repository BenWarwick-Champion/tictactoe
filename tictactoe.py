"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from utils import measure_perf

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
    # check rows
    for r in board:
        if len(set(r)) == 1:
            return r[0]
    
    # check diagonals
    dia1, dia2 = [], []
    for i in range(3):
        dia1.append(board[i][i])
        dia2.append(board[i][2-i])
    if len(set(dia1)) == 1:
        return board[0][0]
    elif len(set(dia2)) == 1:
        return board[0][2]

    # check columns
    for i in range(3):
        if (board[0][i] is not None
        and board[0][i] == board[1][i]
        and board[1][i] == board[2][i]):
            return board[0][i]
            
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
            return 10
        else:
            return -10
    return 0

@measure_perf
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    curr_player = player(board)
    best_move = (0, 0)
    if board == initial_state():
        return best_move

    best_score, alpha, beta = -math.inf, -math.inf, math.inf
    for move in actions(board):
        score = minimax_helper(result(board, move), curr_player, 0, alpha, beta)
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

def minimax_helper(board, plyr, depth, alpha, beta):

    if terminal(board):
        if plyr == X:
            return utility(board)
        else:
            return -utility(board)

    # Maximizing Player
    if plyr == player(board):
        best_score = -math.inf
        for move in actions(board):
            score = minimax_helper(result(board, move), plyr, depth+1, alpha, beta) - depth
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score
    # Minimizing Player
    else:
        best_score = math.inf
        for move in actions(board):
            score = minimax_helper(result(board, move), plyr, depth+1, alpha, beta) + depth
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score
