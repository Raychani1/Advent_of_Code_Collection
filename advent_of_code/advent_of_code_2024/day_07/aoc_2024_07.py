from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored

from advent_of_code.advent_of_code_2024.day_07.structures import (
    build_tree,
    get_tree_values,
)


class AOC2024D07:
    def __init__(self) -> None:
        """Initializes the AOC2024D07 Class."""
        self.year: int = 2024
        self.day: int = 7
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()
        self.__middle_out_values, self.__middle_in_values = self.__build_trees()

    def __process_puzzle_input(
        self,
    ) -> List[Tuple[int, List[int]]]:
        """Processes Puzzle Input.

        Returns:
            List[Tuple[int, List[int]]]: Processed Puzzle Input.
        """
        return [
            (
                int(value.split(':')[0]),
                list(map(int, value.split(':')[1].strip().split(' '))),
            )
            for value in self.__puzzle.input_data.split('\n')
        ]

    def __build_trees(
        self,
    ) -> Tuple[List[Tuple[int, List[int]]], List[Tuple[int, List[int]]]]:
        """Builds Math Expression Tree for each entry, and parses them to
        'middle out' and 'middle in' pairs.

        Returns:
            Tuple[List[Tuple[int, List[int]]], List[Tuple[int, List[int]]]]:
                'Middle out' and 'Middle in' pairs of each entry.
        """
        middle_out_values = []
        middle_in_values = []

        for key, values in self.__data:
            root = build_tree(numbers=values)
            middle_out_values.append((key, get_tree_values(node=root)))
            middle_in_values.append(
                (key, get_tree_values(node=root, fetch_middle=True))
            )

        return middle_out_values, middle_in_values

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: The total calibration result using sum and multiplication.
        """
        return sum(
            [key for key, values in self.__middle_out_values if key in values]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: The total calibration result using sum, concatenation and
                multiplication.
        """
        return sum(
            [key for key, values in self.__middle_in_values if key in values]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored(
                'The total calibration result using sum and multiplication:',
                'green',
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'The total calibration result using sum, concatenation and '
                'multiplication:',
                'green',
            ),
            self.solve_puzzle_2(),
        )
