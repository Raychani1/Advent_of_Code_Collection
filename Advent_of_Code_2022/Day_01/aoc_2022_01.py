from typing import List

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D01:

    def __init__(self) -> None:
        """Initialize the AOC2022D01 Class."""
        self.year: int = 2022
        self.day: int = 1
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: List[List[int]] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[int]]:
        """Process Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input.
        """
        return [
            list(map(int, x))
            for x in list(
                map(str.split, self.__puzzle.input_data.split('\n\n'))
            )
        ]

    def __calories_carried_by_top_elves(self, top: int) -> int:
        """Calculate the sum of Calories carried by Top Elves with most 
        Calories.

        Args:
            top (int): Number of Top Elves.

        Returns:
            int: Calories carried by the Top Elves with most Calories.
        """
        return sum(sorted(list(map(sum, self.__data)))[-top:])

    def solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: Calories carried by the Elf with most Calories.
        """
        return self.__calories_carried_by_top_elves(top=1)

    def solve_puzzle_2(self) -> int:
        """Solve the second part of the Puzzle.

        Returns:
            int: Calories carried by the TOP 3 Elves with most Calories.
        """
        return self.__calories_carried_by_top_elves(top=3)

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""
        print(
            colored(
                'The Elf with the most Calories is carrying',
                'green'
            ),
            self.solve_puzzle_1(),
            colored(
                'Calories.',
                'green'
            )
        )

        print(
            colored(
                'Top 3 Elves with the most Calories are carrying',
                'green'
            ),
            self.solve_puzzle_2(),
            colored(
                'Calories together.',
                'green'
            )
        )
