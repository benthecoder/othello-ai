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

This is what the game looks like:

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

## Search depth comparison

To compare the efects of increasing the search depth, we compare an agent with a fixed depth of 4, and another agent with depths [4, 5, 6].

Below are the results

| Board Size |      4       |      5       |      6       |
| :--------: | :----------: | :----------: | :----------: |
|  Depth 4   |  0:0(0.00)   | 0:10(63.49)  | 0:10(382.57) |
|  Depth 5   | 0:10(48.57)  |  0:0(0.00)   | 0:10(220.47) |
|  Depth 6   | 0:10(278.33) | 10:0(310.05) |  0:0(0.00)   |

## Eval functions comparison

The two evaluation functions I implemented are:

- static board of weights (current player's advantage in terms of their position on the board)
- mobility (current player's advantage in terms of their ability to make moves and restrict the opponent's moves)

The default utility function is coin parity (difference in number of coins/disc between the two players)

Here are the results

|   Method    |   Weights    | Coin_parity |  Mobility   |
| :---------: | :----------: | :---------: | :---------: |
|   Weights   |  0:0(0.00)   | 10:0(6.92)  | 10:0(78.31) |
| Coin_parity | 10:0(16.31)  |  0:0(0.00)  | 10:0(61.19) |
|  Mobility   | 10:0(158.96) | 10:0(21.67) |  0:0(0.00)  |
