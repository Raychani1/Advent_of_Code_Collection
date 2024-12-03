import re
from functools import reduce
from operator import mul
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D03:
    def __init__(self) -> None:
        """Initializes the AOC2024D03 Class."""
        self.year: int = 2024
        self.day: int = 3
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        (
            self.__part_one_data,
            self.__part_two_data,
        ) = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Tuple[List[List[int]], List[List[int]]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[List[List[int]], List[List[int]]]: Processed Puzzle Input.
        """
        part_one_data = [
            list(map(int, sub_list))
            for sub_list in list(
                map(
                    lambda x: x.split(','),
                    re.findall(r'mul\((\d*,\d*)\)', self.__puzzle.input_data),
                )
            )
        ]

        part_two_data = [
            list(map(int, sub_list))
            for sub_list in list(
                map(
                    # Clean `mul(`, and `)` from the valid ranges
                    lambda x: x[4:-1].split(','),
                    self.__filter_irrelevant_ranges(
                        data=re.findall(
                            r"do\(\)|don't\(\)|mul\(\d*,\d*\)",
                            self.__puzzle.input_data,
                        )
                    ),
                )
            )
        ]

        return part_one_data, part_two_data

    @staticmethod
    def __filter_irrelevant_ranges(data: List[str]) -> List[str]:
        """Filters and cleans up multiplication operations between `don't()`
        and `do()`.

        Args:
            data (List[str]): Problem relevant data.

        Returns:
            List[str]: Filtered data.
        """
        # Find all the indices of `don't()`
        dont_indices = [i for i, x in enumerate(data) if x == "don't()"]

        # Find all the indices of `do()` and filter the ones which are
        # before the first `don't()`
        do_indices = list(
            filter(
                lambda num: num >= dont_indices[0],
                [i for i, x in enumerate(data) if x == 'do()'],
            )
        )

        ranges: List[Tuple[int, int]] = []

        for do_element_index in do_indices:
            for dont_element_index in dont_indices:
                # Valid range between `do()` and `don't()`
                if dont_element_index > do_element_index:
                    # Range is saved if it is either the first one or
                    # not overlapping with the previous one
                    if not ranges or dont_element_index != ranges[-1][1]:
                        ranges.append((do_element_index, dont_element_index))
                    break

        # Select all the elements before the first `don't()`
        valid_ranges = data[: dont_indices[0]]

        # Select all the other valid values
        for start, end in ranges:
            valid_ranges.extend(data[start + 1 : end])

        # Filter all the residual `do()`-s from overlapping ranges
        return list(filter(lambda val: val != 'do()', valid_ranges))

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: The result of all multiplications.
        """
        return sum([reduce(mul, numbers) for numbers in self.__part_one_data])

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: The result of the enabled multiplications.
        """
        return sum([reduce(mul, numbers) for numbers in self.__part_two_data])

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('The result of all multiplications:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('The result of the enabled multiplications:', 'green'),
            self.solve_puzzle_2(),
        )
