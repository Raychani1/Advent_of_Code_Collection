from collections import Counter
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D01:
    def __init__(self) -> None:
        """Initializes the AOC2024D01 Class."""
        self.year: int = 2024
        self.day: int = 1
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__left, self.__right = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Tuple[List[int], List[int]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[List[int], List[int]]: Processed Puzzle Input. Left and Right
                columns of input.
        """
        individual_numbers = list(
            map(lambda x: x.split('   '), self.__puzzle.input_data.split('\n'))
        )

        left = sorted([int(sub_list[0]) for sub_list in individual_numbers])
        right = sorted([int(sub_list[1]) for sub_list in individual_numbers])

        return left, right

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: The total distance between the left and right list.
        """
        return sum(
            [abs(x - y) for x, y in list(zip(self.__left, self.__right))]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: The similarity score of the left and right list.
        """
        occurrence = Counter(self.__right)
        return sum([x * occurrence[x] for x in self.__left])

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('The total distance between the two columns:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('The similarity score of the two columns:', 'green'),
            self.solve_puzzle_2(),
        )
