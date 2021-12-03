from typing import List
from aocd import submit
from termcolor import colored
from aocd.models import Puzzle


class AOC2021D01:

    def __init__(self) -> None:
        """Initialize the AOC2021D01 Class."""

        self.__year: int = 2021
        self.__day: int = 1
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: List[int] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[int]:
        """Process Puzzle Input.

        Returns:
            List[int]: Processed Puzzle Input

        """

        return list(map(int, self.__puzzle.input_data.split('\n')))

    def __solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: Number of measurements that are larger than the previous
                measurement

        """

        increased: int = 0

        for i in range(1, len(self.__data)):
            if self.__data[i] - self.__data[i - 1] > 0:
                increased += 1

        return increased

    def __solve_puzzle_2(self) -> int:
        """Solve the second part of the Puzzle.

        Returns:
            int: Number of sums of 3 that are larger than the previous sum of 3

        """

        increased: int = 0
        previous_window: int = sum(self.__data[0:3])

        for i in range(1, len(self.__data) - 2):
            current_window: int = sum(self.__data[i:i + 3])

            if current_window - previous_window > 0:
                increased += 1

            previous_window = current_window

        return increased

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            self.__solve_puzzle_1(),
            colored(
                'measurements are larger than the previous measurement.',
                'green'
            )
        )

        print(
            self.__solve_puzzle_2(),
            colored(
                'sums are larger than the previous sum.',
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
            answer=self.__solve_puzzle_1()
        )
        submit(
            year=self.__year,
            day=self.__day,
            part="b",
            answer=self.__solve_puzzle_2()
        )
