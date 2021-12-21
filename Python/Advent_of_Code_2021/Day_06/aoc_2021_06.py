from aocd import submit
from typing import List, Dict
from termcolor import colored
from aocd.models import Puzzle


class AOC2021D06:

    def __init__(self) -> None:
        """Initialize the AOC2021D06 Class."""

        self.__year: int = 2021
        self.__day: int = 6
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: List[int] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[int]:
        """Process Puzzle Input.

        Returns:
            List[int]: Processed Puzzle Input

        """

        return list(map(int, self.__puzzle.input_data.split(',')))

    def __solve_puzzle(self, days: int) -> int:
        """Solve both parts of the Puzzle.

        Returns:
            int: Number of lanternfish after given days

        """

        data: Dict[int, int] = {}

        # Load initial values to empty dictionary
        for timer in range(9):
            data[timer] = self.__data.count(timer)

        # For each day
        for _ in range(days):

            # Create new temporary dictionary
            new_data: Dict[int, int] = dict.fromkeys(data.keys(), 0)

            # Modify values
            new_data[8] = data[0]

            for i in range(1, 9):
                new_data[i-1] = data[i]

            new_data[6] += new_data[8]

            # Update the original dictionary
            data: Dict[int, int] = new_data

            # Remove temporary dictionary
            del new_data

        # Return the number of lanternfish
        return sum(data.values())

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            colored(
                'There are',
                'green'
            ),
            self.__solve_puzzle(days=80),
            colored(
                'lanternfish after 80 days.',
                'green'
            )
        )

        print(
            colored(
                'There are',
                'green'
            ),
            self.__solve_puzzle(days=256),
            colored(
                'lanternfish after 256 days.',
                'green'
            )
        )

    def solve_and_submit_puzzles(self) -> None:
        """Solve both Puzzles and Submit the Solution to the Advent of Code
            Website.

        """

        submit(
            year=self.__year,
            day=self.__day,
            part="a",
            answer=self.__solve_puzzle(days=80)
        )
        submit(
            year=self.__year,
            day=self.__day,
            part="b",
            answer=self.__solve_puzzle(days=256)
        )
