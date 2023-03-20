from games import Othello, alpha_beta_cutoff_search


def query_player(game, state):
    """Make a move by querying standard input."""

    game.display(state)

    move = None
    available_moves = game.actions(state)

    # if there are available moves, ask for input
    if available_moves:
        while not move:
            move_string = input("\nEnter move: ")

            try:
                x, y = move_string.split(",")
                move = int(x), int(y)
            except ValueError:
                print("bad format, please format as x, y")
                continue

            # check for available moves
            if move not in available_moves:
                print("illegal move, please try again")
                move = None
    else:
        print("no legal moves: passing turn to next player")
    return move


def alpha_beta_player(game, state):
    return alpha_beta_cutoff_search(state, game, verbose=True)


if __name__ == "__main__":

    game = Othello()

    B_player = query_player
    W_player = alpha_beta_player

    win = game.play_game(B_player, W_player)
