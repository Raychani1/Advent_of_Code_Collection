from typing import List, Optional

from aocd.models import Puzzle
from termcolor import colored


class AOC2025D03:

    def __init__(self) -> None:
        """Initializes the AOC2025D03 Class."""
        self.year: int = 2025
        self.day: int = 3
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[int]]:
        """Processes Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input.
        """
        return [
            [
                int(battery) for battery in list(battery_bank)
            ] for battery_bank in self.__puzzle.input_data.split('\n')
        ]

    @staticmethod
    def __largest_number_from_digits(
        digits: List[int], goal_number_length: int
    ) -> Optional[int]:
        """Returns the largest number of length `goal_number_length` formed from
        `digits`preserving their original order. None if `goal_number_length` is
        negative or 0.

        **Disclaimer: GPT Inspired.**

        Args:
            digits (List[int]): Digit at disposal for picking.
            goal_number_length (int): Desired number length.

        Returns:
            Optional[int]: None or largest number based on arguments.
        """
        available_number_length = len(digits)

        if goal_number_length <= 0:
            return None
    
        if goal_number_length >= available_number_length:
            return int(''.join(str(d) for d in digits))

        stack = []
        for digit_index, digit in enumerate(digits):
            remaining_length = available_number_length - digit_index
            
            # If we find a bigger number and still have enough numbers to meet
            # the goal we may replace the last number from the stack.
            while (
                stack and
                stack[-1] < digit and
                (
                    (len(stack) + remaining_length - 1) >= goal_number_length
                )
            ):
                stack.pop()

            if len(stack) < goal_number_length:
                stack.append(digit)

        return int(''.join(str(digit) for digit in stack))

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Total output joltage for 2 batteries per bank.
        """
        return sum(
            [
                self.__largest_number_from_digits(battery_bank, 2) for battery_bank in self.__data
            ]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Total output joltage for 12 batteries per bank.
        """
        return sum(
            [
                self.__largest_number_from_digits(battery_bank, 12) for battery_bank in self.__data
            ]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Total output joltage for 2 batteries per bank:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('Total output joltage for 12 batteries per bank:', 'green'),
            self.solve_puzzle_2(),
        )
