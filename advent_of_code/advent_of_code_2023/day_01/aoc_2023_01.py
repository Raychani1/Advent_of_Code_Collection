import re
from typing import Dict, List

from aocd.models import Puzzle
from termcolor import colored


class AOC2023D01:
    def __init__(self) -> None:
        """Initializes the AOC2023D01 Class."""
        self.year: int = 2023
        self.day: int = 1
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Dict[str, List[List[str]]]:
        """Processes Puzzle Input.

        Returns:
            Dict[List[List[str]]]: Processed Puzzle Input.
        """
        replacements = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
        }

        split_input = self.__puzzle.input_data.split('\n')

        data = {}

        data['puzzle_1_data'] = [
            [letter for letter in row if letter.isdigit()]
            for row in split_input
        ]

        # Using a forward lookup regex we match every literal number
        data['puzzle_2_data'] = [
            [
                replacements.get(item, item)
                for item in re.findall(
                    fr"(?=({'|'.join(replacements.keys())}|\d))", row
                )
            ]
            for row in split_input
        ]

        return data

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Sum of the trebuchet calibration values.
        """
        return sum(
            [
                int(number[0] + number[-1])
                for number in self.__data['puzzle_1_data']
            ]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Sum of the new trebuchet calibration values.
        """
        return sum(
            [
                int(number[0] + number[-1])
                for number in self.__data['puzzle_2_data']
            ]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('The sum of the calibration values is:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('The sum of the calibration values is:', 'green'),
            self.solve_puzzle_2(),
        )
