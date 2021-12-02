from aocd import submit
from termcolor import colored
from aocd.models import Puzzle


class AOC2021D02:

    def __init__(self) -> None:
        """Initialize the AOC2021D02 Class."""

        self.__year = 2021
        self.__day = 2
        self.__puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data = self.__read_puzzle_input(
            puzzle_input=self.__puzzle.input_data
        )

    @staticmethod
    def __read_puzzle_input(puzzle_input: str) -> list:
        """Process puzzle input.

        Args:
            puzzle_input (str): Puzzle input string

        Returns:
            list: Processed puzzle input

        """

        input_list = [x.split() for x in puzzle_input.split('\n')]

        for element in input_list:
            element[1] = int(element[1])

        return input_list

    def __solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: The product of the Horizontal Position and Depth

        """

        # Position of the Submarine ( Horizontal Position and Depth )
        position = [0, 0]

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
        position = [0, 0, 0]

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
