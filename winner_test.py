from tictactoe import X, O, EMPTY, winner

if __name__=="__main__":
    boards = [
        [
            [EMPTY, X, EMPTY],
            [EMPTY, X, O],
            [EMPTY, X, O]
        ],
        [
            [X, EMPTY, EMPTY],
            [O, O, O],
            [X, X, EMPTY]
        ],
        [
            [O, X, X],
            [X, O, X],
            [X, X, O]
        ],
        [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    ]

    answers = [X, O, O, None]

    for ind, board in enumerate(boards):
        assert winner(board) == answers[ind], f"Winner returned {winner(board)}. Expected {answers[ind]}."

    print("Tests complete.")
