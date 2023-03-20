from games import Othello, alpha_beta_cutoff_search
from evals import mobility, weighted_board_position
import functools
from pprint import pprint
from time import perf_counter
from tqdm import tqdm
import argparse


def alpha_beta_player(game, state, d=4, eval_fn=None, verbose=False):
    return alpha_beta_cutoff_search(state, game, d=d, eval_fn=eval_fn, verbose=verbose)


def play_game(B_player, W_player, verbose=False):
    game = Othello()
    result = game.play_game(B_player, W_player, verbose=verbose)
    return result


def compare_agents(compare_type, params):
    num_games = 10
    results = {
        (b_param.__name__, w_param.__name__): {"wins": 0, "loss": 0, "avg_time": 0}
        for b_param in params
        for w_param in params
    }

    with tqdm(total=num_games * len(results)) as t:
        for b_param in params:
            for w_param in params:
                if b_param == w_param:
                    continue
                if compare_type == "depth":
                    B_player = functools.partial(alpha_beta_player, d=b_param)
                    W_player = functools.partial(alpha_beta_player, d=w_param)
                    t.set_description(f"Depth {b_param} vs {w_param}")
                elif compare_type == "eval":
                    B_player = functools.partial(alpha_beta_player, eval_fn=b_param)
                    W_player = functools.partial(alpha_beta_player, eval_fn=w_param)
                    t.set_description(
                        f"Eval_fn {b_param.__name__ if b_param else 'coin_parity'} vs {w_param.__name__ if w_param else 'coin_parity'}"
                    )

                total_time = 0
                for i in range(1, num_games + 1):
                    t.set_postfix_str(f"Game {i}")
                    start = perf_counter()
                    res = play_game(B_player, W_player)
                    end = perf_counter()
                    if res == 1:
                        results[(b_param, w_param)]["wins"] += 1
                    else:
                        results[(b_param, w_param)]["loss"] += 1
                    total_time += end - start
                    t.update(1)
                results[(b_param, w_param)]["avg_time"] = round(
                    total_time / num_games, 2
                )

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare agents",
    )
    parser.add_argument("--depth")
    parser.add_argument("--eval_fn")
    args = parser.parse_args()

    if args.depth:
        depths = [4, 5, 6]
        depth_results = compare_agents("depth", depths)
        with open("depth_results.txt", "w") as f:
            pprint(depth_results, stream=f)

    elif args.eval_fn:
        eval_fns = [None, mobility, weighted_board_position]
        eval_results = compare_agents("eval", eval_fns)
        with open("eval_results.txt", "w") as f:
            pprint(eval_results, stream=f)

    ## play a game between weighted_board_position and mobility
    # B_player = functools.partial(alpha_beta_player, verbose=True)
    # W_player = functools.partial(alpha_beta_player, verbose=True)

    # res = play_game(B_player, W_player, verbose=True)
    # print(res)
