from typing import Any

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D01:
    def __init__(self) -> None:
        """Initializes the AOC2024D01 Class."""
        self.year: int = 2024
        self.day: int = 1
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: Any = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Any:
        """Processes Puzzle Input.

        Returns:
            Any: Processed Puzzle Input.
        """
        pass

    def solve_puzzle_1(self) -> Any:
        """Solves the first part of the Puzzle.

        Returns:
            Any: _description_
        """
        pass

    def solve_puzzle_2(self) -> Any:
        """Solves the second part of the Puzzle.

        Returns:
            Any: _description_
        """
        pass

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('TODO', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('TODO', 'green'),
            self.solve_puzzle_2(),
        )
