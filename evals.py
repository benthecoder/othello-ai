"""
Reference:
- https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
"""


def weighted_board_position(game, state):
    """(max player utility - min player utility) weighted by board position"""

    player = state.to_move

    weights = [
        [4, -3, 2, 2, 2, 2, -3, 4],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [4, -3, 2, 2, 2, 2, -3, 4],
    ]

    score = 0
    for row in range(game.v):
        for col in range(game.h):
            disc = state.board.get((row, col))
            if disc == player:
                score += weights[row][col]
            elif disc != player and disc is not None:
                score -= weights[row][col]
    return score


def mobility(game, state):
    """(moves of max player - moves of min player after max player's move)"""

    player_moves = len(state.moves)
    opponent_moves = 0

    for move in state.moves:
        next_state = game.result(state, move)
        opponent_moves += len(next_state.moves)

    return player_moves - opponent_moves
