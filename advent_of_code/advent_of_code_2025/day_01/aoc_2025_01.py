from typing import List

from aocd.models import Puzzle
from termcolor import colored


class AOC2025D01:
    def __init__(self) -> None:
        """Initializes the AOC2025D01 Class."""
        self.year: int = 2025
        self.day: int = 1
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[int]:
        """Processes Puzzle Input.

        Returns:
            List[int]: Processed Puzzle Input.
        """
        return [
            int(rotation) for rotation in
            self.__puzzle.input_data.translate(
                str.maketrans({'R': '', 'L': '-'})
            ).split('\n')
        ]

    def solve_puzzle_1(
        self,
        dial_size: int = 100,
        starting_position: int = 50,
        check_position: int = 0
    ) -> int:
        """Solves the first part of the Puzzle.

        Args:
            dial_size (int): Size of the dial. Defaults to 100.
            starting_position (int): Safe dial starting position.
                Defaults to 50.
            check_position (int): Number to check the dial for. Defaults to 0.

        Returns:
            int: Safe password - how many times is it pointing to
                `check_position`.
        """
        password = 0
        current_position = starting_position

        for rotation in self.__data:
            current_position = (current_position + rotation) % dial_size

            if current_position == check_position:
                password += 1

        return password

    def solve_puzzle_2(
        self,
        dial_size: int = 100,
        starting_position: int = 50,
        check_position: int = 0
    ) -> int:
        """Solves the second part of the Puzzle.
    
        Args:
            dial_size (int): Size of the dial. Defaults to 100.
            starting_position (int): Safe dial starting position.
                Defaults to 50.
            check_position (int): Number to check the dial for crossing.
                Defaults to 0.

        Returns:
            int: Safe password - how many times was the `check_position`
                crossed.
        """
        password = 0
        current_position = starting_position

        for rotation in self.__data:
            goal_position = current_position + rotation

            rotation_range = (
                range(current_position - 1, goal_position - 1, -1) 
                if goal_position < current_position else 
                range(current_position + 1, goal_position + 1)
            )

            password += sum(
                [i % dial_size == check_position for i in rotation_range]
            )           

            current_position = goal_position % dial_size

        return password

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Number of times the dial pointed to 0:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('Number of times the dial crossed 0:', 'green'),
            self.solve_puzzle_2(),
        )
