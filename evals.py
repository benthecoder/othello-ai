"""
Reference:
- https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
"""


def weighted_board_position(game, state):
    """(max player utility - min player utility) weighted by board position"""

    player = state.to_move

    weights = [
        [120, -20, 20, 5, 5, 20, -20, 120],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [120, -20, 20, 5, 5, 20, -20, 120],
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
    """(moves of max player - moves of min player)"""

    player = state.to_move
    opponent = "B" if player == "W" else "W"

    player_m = len(game._get_legal_moves(state.board, player))
    opp_m = len(game._get_legal_moves(state.board, opponent))

    return (player_m - opp_m) / (player_m + opp_m + 1)


def mobility_corners(game, state):
    """(moves of max player - moves of min player after max player's move)"""

    def count_corners(board, player):

        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        count = 0
        for corner in corners:
            if board.get(corner) == player:
                count += 1
        return count

    player = state.to_move
    opponent = "B" if player == "W" else "W"

    player_m = len(game._get_legal_moves(state.board, player))
    opp_m = len(game._get_legal_moves(state.board, opponent))

    player_c = count_corners(state.board, state.to_move)
    opp_c = count_corners(state.board, opponent)

    return 10 * (player_c - opp_c) + ((player_m - opp_m) / (player_m + opp_m + 1))
