
from tictactoe import X, O, EMPTY, winner


if __name__=="__main__":
    board = [
        [EMPTY, X, EMPTY],
        [EMPTY, X, O],
        [EMPTY, X, O]
    ]

    result = winner(board)
    assert result == X, f"Winner returned {result}. Expected 'X'."

