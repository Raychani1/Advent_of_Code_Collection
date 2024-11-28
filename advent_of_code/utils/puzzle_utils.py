from typing import Any, Dict, List

from aocd import submit


def solve_and_submit_puzzles(year: int, day: int, solutions: List[Any]) -> None:
    """Solves both Puzzles and Submits the Solution to the Advent of Code
    Website.

    Args:
        year (int): Puzzle Year.
        day (int): Puzzle Day.
        solutions (List[Any]): Puzzle Solutions.
    """
    for i, solution in enumerate(solutions):
        submit(year=year, day=day, part=chr(ord('a') + i), answer=solution())


def run_aoc(aoc_config: Dict[str, List[Any]], submit: bool = False) -> None:
    """Solve every puzzle for given configuration.

    Args:
        aoc_config (Dict[str, List[Any]]): AOC Solution Configuration.
        submit (bool, optional): Submit answers. Defaults to False.
    """
    for year in sorted(aoc_config.keys()):
        for day, aoc in enumerate(aoc_config[year]):
            aoc.solve_and_display_puzzles()

            # Submit only the last day to lower unnecessary AOC Site traffic
            if (day == len(aoc_config[year]) - 1) and submit:
                solve_and_submit_puzzles(
                    year=int(year),
                    day=(day + 1),
                    solutions=[aoc.solve_puzzle_1, aoc.solve_puzzle_2],
                )
