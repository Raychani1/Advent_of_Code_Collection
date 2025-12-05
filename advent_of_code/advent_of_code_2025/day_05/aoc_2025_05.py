
from typing import List, Tuple

import numpy as np
from aocd.models import Puzzle
from termcolor import colored


class AOC2025D05:

    def __init__(self) -> None:
        """Initializes the AOC2025D05 Class."""
        self.year: int = 2025
        self.day: int = 5
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__fresh_ranges, self.__ingredient_ids = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Tuple[List[Tuple[int, int]], List[int]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[List[Tuple[int, int]], List[int]]: Processed Puzzle Input.
        """
        split_data = self.__puzzle.input_data.split('\n\n')
        fresh_ranges = [
            tuple(
                int(range_limit) for range_limit in fresh_range.split('-')
            ) for fresh_range in split_data[0].split('\n')
        ]
        ingredient_ids = [
            int(ingredient) for ingredient in split_data[1].split('\n')
        ]

        return fresh_ranges, ingredient_ids

    def __in_range(self, ingredient_id: int,) -> bool:
        """Checks wether a given `ingredient_id` is in any of the ranges.

        Args:
            ingredient_id (int): Ingredient ID to check for ranges.

        Returns:
            bool: `True` if given `ingredient_id` is in any of the ranges, else
                `False`.
        """
        # OR: return any(range_start <= ingredient_id <= range_end for range_start, range_end in self.__fresh_ranges)
        for range_start, range_end in self.__fresh_ranges:
            if range_start <= ingredient_id <= range_end:
                return True
        return False

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of available fresh ingredient IDs.
        """
        is_fresh_id_v = np.vectorize(self.__in_range, otypes=[bool])      

        return sum(is_fresh_id_v(self.__ingredient_ids))

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of ingredient IDs considered fresh by the system.
        """
        sorted_ranges = sorted(self.__fresh_ranges, key=lambda r: r[0])
        fresh_ids = 0
        largest_fresh_id = 0

        for range_start, range_end in sorted_ranges:
            # If the range was already processed skip it
            if largest_fresh_id >= range_end:
                continue
            
            # If the largest ID is inside new range change the range start
            if range_start <= largest_fresh_id < range_end:
                range_start = largest_fresh_id + 1

            # Add number of elements and save the largest fresh ID
            fresh_ids += (range_end - range_start) + 1
            largest_fresh_id = range_end

        return fresh_ids    

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Number of available fresh ingredient IDs:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'Number of ingredient IDs considered fresh by the system:',
                'green'
            ),
            self.solve_puzzle_2(),
        )
