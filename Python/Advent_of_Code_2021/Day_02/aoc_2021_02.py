from aocd import submit
from termcolor import colored
from typing import List, Union
from aocd.models import Puzzle


class AOC2021D02:

    def __init__(self) -> None:
        """Initialize the AOC2021D02 Class."""

        self.__year: int = 2021
        self.__day: int = 2
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: List[List[Union[str, int]]] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[Union[str, int]]]:
        """Process Puzzle Input.

        Returns:
            List[List[Union[str, int]]]: Processed Puzzle Input

        """

        input_list: List[List[str]] = [
            x.split() for x in self.__puzzle.input_data.split('\n')
        ]

        for element in input_list:
            element[1] = int(element[1])

        return input_list

    def __solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: The product of the Horizontal Position and Depth

        """

        # Position of the Submarine ( Horizontal Position and Depth )
        position: List[int] = [0, 0]

        for data in self.__data:
            if data[0] == 'down':
                position[1] += data[1]
            elif data[0] == 'up':
                position[1] -= data[1]
            else:
                position[0] += data[1]

        return position[0] * position[1]

    def __solve_puzzle_2(self) -> int:
        """Solve the second part of the Puzzle.

        Returns:
            int: The product of the Horizontal Position and Depth

        """

        # Position of the Submarine ( Horizontal Position, Depth and Aim )
        position: List[int] = [0, 0, 0]

        for data in self.__data:
            if data[0] == 'down':
                position[2] += data[1]
            elif data[0] == 'up':
                position[2] -= data[1]
            else:
                position[0] += data[1]
                position[1] += (position[2] * data[1])

        return position[0] * position[1]

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            colored(
                'The product of the Horizontal Position and Depth:',
                'green'
            ),
            self.__solve_puzzle_1()
        )

        print(
            colored(
                'The product of the Horizontal Position and Depth:',
                'green'
            ),
            self.__solve_puzzle_2()
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
