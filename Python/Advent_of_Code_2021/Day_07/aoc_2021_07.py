from aocd import submit
from typing import List, Dict
from termcolor import colored
from aocd.models import Puzzle


class AOC2021D07:

    def __init__(self) -> None:
        """Initialize the AOC2021D07 Class."""

        self.__year: int = 2021
        self.__day: int = 7
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: List[int] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[int]:
        """Process Puzzle Input.

        Returns:
            List[int]: Processed Puzzle Input

        """

        return list(map(int, self.__puzzle.input_data.split(',')))

    def __solve_puzzle(self, constant_fuel_consumption: bool) -> int:
        """Solve both parts of the Puzzle.

        Args:
            constant_fuel_consumption (bool): Constant (1) or Increasing
                (1,2,3...) fuel consumption

        Returns:
            int: Unit of fuel needed for alignment

        """

        positions: Dict[int, int] = dict.fromkeys(
            range(min(self.__data), max(self.__data) + 1), 0
        )

        for pos in range(min(self.__data), max(self.__data) + 1):

            fuel_sum: int = 0

            for position in self.__data:

                position_diff: int = abs(position - pos)

                fuel_sum += position_diff \
                    if constant_fuel_consumption \
                    else position_diff * (position_diff + 1) // 2

            positions[pos] = fuel_sum

        return min(positions.values())

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            colored(
                'They must spend',
                'green'
            ),
            self.__solve_puzzle(constant_fuel_consumption=True),
            colored(
                'unit of fuel to align to that position.',
                'green'
            )
        )

        print(
            colored(
                'They must spend',
                'green'
            ),
            self.__solve_puzzle(constant_fuel_consumption=False),
            colored(
                'unit of fuel to align to that position.',
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
            answer=self.__solve_puzzle(constant_fuel_consumption=True)
        )
        submit(
            year=self.__year,
            day=self.__day,
            part="b",
            answer=self.__solve_puzzle(constant_fuel_consumption=False)
        )
