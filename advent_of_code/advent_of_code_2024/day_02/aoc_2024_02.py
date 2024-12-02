import itertools
from typing import List

import more_itertools
from aocd.models import Puzzle
from termcolor import colored


class AOC2024D02:
    def __init__(self) -> None:
        """Initializes the AOC2024D02 Class."""
        self.year: int = 2024
        self.day: int = 2
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: List[List[int]] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[int]]:
        """Processes Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input. Left and Right columns of
                input.
        """
        return [
            [int(x) for x in lst]
            for lst in list(
                map(
                    lambda x: x.split(' '), self.__puzzle.input_data.split('\n')
                )
            )
        ]

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: The number of safe reports based on the original methodology.
        """
        # OR: [list(zip(report, report[1:])) for report in self.__data]
        return sum(
            [
                # All increasing
                all(
                    (1 <= level_2 - level_1 <= 3) for level_1, level_2 in levels
                )
                or
                # All decreasing
                all(
                    (1 <= level_1 - level_2 <= 3) for level_1, level_2 in levels
                )
                for levels in [
                    list(more_itertools.windowed(report, 2))
                    for report in self.__data
                ]
            ]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: The number of safe reports based on the new methodology.
        """
        return sum(
            [
                any(
                    # All increasing
                    all(
                        (1 <= level_2 - level_1 <= 3)
                        for level_1, level_2 in levels
                    )
                    or
                    # All decreasing
                    all(
                        (1 <= level_1 - level_2 <= 3)
                        for level_1, level_2 in levels
                    )
                    for levels in [
                        list(zip(report_variant, report_variant[1:]))
                        for report_variant in (
                            [report]
                            + list(
                                itertools.combinations(report, len(report) - 1)
                            )
                        )
                    ]
                )
                for report in self.__data
            ]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Based on the original methodology', 'green'),
            self.solve_puzzle_1(),
            colored('reports were safe.', 'green'),
        )

        print(
            colored('Based on the new methodology', 'green'),
            self.solve_puzzle_2(),
            colored('reports were safe.', 'green'),
        )
