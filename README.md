# Othello Game Agent

- [Othello Game Agent](#othello-game-agent)
  - [How to run](#how-to-run)
  - [Search depth comparison](#search-depth-comparison)
  - [Eval functions comparison](#eval-functions-comparison)

## How to run

install numpy

```bash
  pip install numpy
```

run the game

```bash
  python main.py
```

This plays a game with a minimax agent with a depth of 3, and uses the coin parity heurstics as the utility function.

It prints the scores, who's turn it is, possible moves (denoted by `@`), and the board state.

| Note: moves are indexed by 0

```txt
=================================
B: 2, W: 2

B's turn
moves: [(2, 3), (4, 5), (5, 4), (3, 2)]
. . . . . . . .
. . . . . . . .
. . . @ . . . .
. . @ W B . . .
. . . B W @ . .
. . . . @ . . .
. . . . . . . .
. . . . . . . .

Enter move:
```

It checks for the format of input and if the move is valid.

```txt
Enter move: 1
bad format, please format as x, y

Enter move: 1, 1
illegal move, please try again
```

After playing a move, the board state is updated and the next player's turn begins.

```txt
Enter move: 2, 3

=================================
B: 4, W: 1

W's turn
moves: [(2, 4), (4, 2), (2, 2)]
. . . . . . . .
. . . . . . . .
. . @ B @ . . .
. . . B B . . .
. . @ B W . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .

=================================
B: 3, W: 3

B's turn
moves: [(5, 5), (5, 4), (5, 1), (5, 3), (5, 2)]
. . . . . . . .
. . . . . . . .
. . . B . . . .
. . . B B . . .
. . W W W . . .
. @ @ @ @ @ . .
. . . . . . . .
. . . . . . . .

Enter move:

```

## Search depth comparison

To compare the efects of increasing the search depth, we compare an agent with a fixed depth of 3, and another agent with depths [4, 5, 6].

Run the following command to compare the two agents with varying depths

```py
  python compare_agents.py --depth True
```

You'll find the results in `depth_results.txt` after running it

| Note, you might get different results due to randomness in the game

Where the format is wins:losses(average time), from the perspective of the player with the black discs.

|  Depth  |     3      |     4      |      5      |      6      |
| :-----: | :--------: | :--------: | :---------: | :---------: |
| Depth 3 | 3:2(13.66) | 1:4(34.83) | 2:3(105.32) | 2:3(587.41) |

From the results, depth 3 loses against an agent with depth 4,5 and 6, so there's an advantage to increasing the search depth with the cost of increased time.

## Eval functions comparison

The baseline for comparison is a random agent and the depths used are [1, 3, 5].

The evaluation functions compared are:

- coin parity (current player's advantage in terms of the number of discs on the board)
- static board of weights (current player's advantage in terms of their position on the board)
- mobility_corners (current player's advantage in terms of the number of possible moves and the number of corners they control)

They are implemented in [`evals.py`](evals.py)

```py
  python compare_agents.py --eval_fn True
```

You'll find the results in `eval_results.txt` after running it

|    evals     |   random   | coin_parity | mobility_corners | weighted_board_position |
| :----------: | :--------: | :---------: | :--------------: | :---------------------: |
| random (d=1) | 3:2(0.01s) | 2:3(0.17s)  |    0:5(0.32s)    |       0:5(0.23s)        |
| random (d=3) | 3:2(0.01s) | 1:4(5.04s)  |    1:4(7.28s)    |       0:5(5.94s)        |
| random (d=5) | 2:2(0.01s) | 1:4(85.94s) |   1:4(124.94s)   |       1:4(85.23s)       |

At depth 1, mobility corners and weighted board both wins all games, while coin parity loses 2 games.

At depth 3, weighted board wins all games, coin parity and mobility corners loses 1.

At depth 5, the heuristics are tied, each losing only 1 game.

Across depth, considering the wins and time taken, the weigthed board heursitics can seems to be the best choice compared to the random agent, as it takes the least time to achieve similar results.

As depth increases, and as the number of games played increases, results might differ, as randomness is introduced in the game.
