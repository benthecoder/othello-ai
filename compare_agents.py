from games import Othello, alpha_beta_cutoff_search
from evals import mobility, weighted_board_position, mobility_corners
import functools
from pprint import pprint
from time import perf_counter
from tqdm import tqdm
import argparse


NUM_GAMES = 5


def alpha_beta_player(game, state, d=4, eval_fn=None, verbose=False):
    return alpha_beta_cutoff_search(state, game, d=d, eval_fn=eval_fn, verbose=verbose)


def play_game(B_player, W_player, verbose=False):
    game = Othello()
    result = game.play_game(B_player, W_player, verbose=verbose)
    return result


def compare_agents(
    compare_type, params, depth_baseline=3, eval_baseline="random", eval_depth=3
):
    results = {}
    baseline = depth_baseline if compare_type == "depth" else eval_baseline

    for w_param in params:
        if isinstance(w_param, int):
            param_name = str(w_param)

        elif w_param is None:
            param_name = "coin"
        elif w_param == "random":
            param_name = "random"
        else:
            param_name = w_param.__name__

        if compare_type == "depth":
            B_player = functools.partial(alpha_beta_player, d=depth_baseline)
            W_player = functools.partial(alpha_beta_player, d=w_param)
        elif compare_type == "eval":
            B_player = functools.partial(
                alpha_beta_player, d=eval_depth, eval_fn=eval_baseline
            )
            W_player = functools.partial(
                alpha_beta_player, d=eval_depth, eval_fn=w_param
            )

        total_time = 0
        wins = 0
        losses = 0
        with tqdm(total=NUM_GAMES) as t:
            for i in range(1, NUM_GAMES + 1):
                t.set_description(f"{baseline} vs {param_name}")
                t.set_postfix_str(f"Game {i}")
                start = perf_counter()
                res = play_game(B_player, W_player)
                end = perf_counter()
                if res == 1:
                    wins += 1
                elif res == 0:
                    losses += 1
                total_time += end - start
                t.update(1)

        results[param_name] = {
            "wins": wins,
            "loss": losses,
            "avg_time": round(total_time / NUM_GAMES, 2),
        }

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare agents",
    )
    parser.add_argument("--depth")
    parser.add_argument("--eval_fn")
    args = parser.parse_args()

    if args.depth:
        baseline = 3
        depths = [3, 4, 5, 6]
        depth_results = compare_agents("depth", depths, depth_baseline=baseline)

        with open("depth_results.txt", "w") as f:
            for eval, results in depth_results.items():
                f.write(
                    f"{baseline} vs {eval}: {results['wins']}:{results['loss']} ({results['avg_time']}s) \n"
                )

    elif args.eval_fn:
        baseline = "random"
        eval_depth = [1, 3, 5]
        eval_fns = ["random", None, mobility_corners, weighted_board_position]

        for eval_depth in eval_depth:
            eval_results = compare_agents(
                "eval", eval_fns, eval_baseline=baseline, eval_depth=eval_depth
            )

            with open("eval_results.txt", "a") as f:
                f.write(f"Depth: {eval_depth} \n")
                for eval, results in eval_results.items():

                    f.write(
                        f"{baseline} vs {eval}: {results['wins']}:{results['loss']} ({results['avg_time']}s) \n"
                    )

    ## play a game between weighted_board_position and mobility
    # B_player = functools.partial(alpha_beta_player, d=4, eval_fn="random")
    # W_player = functools.partial(alpha_beta_player, d=4, eval_fn=mobility)

    # res = play_game(B_player, W_player, verbose=True)

    # if res == 1:
    #    print("Black wins")
