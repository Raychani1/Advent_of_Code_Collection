import itertools
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D05:
    def __init__(self) -> None:
        """Initializes the AOC2024D05 Class."""
        self.year: int = 2024
        self.day: int = 5
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__ordering_rules, self.__updates = self.__process_puzzle_input()
        self.__valid_sum, self.__invalid_sum = self.__calculate_middle_sums()

    def __process_puzzle_input(
        self,
    ) -> Tuple[List[str], List[List[str]]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[Dict[str, List[str]], List[List[str]]]: Processed Puzzle
                Input.
        """
        split_data: List[str] = self.__puzzle.input_data.split('\n\n')

        ordering_rules = split_data[0].split('\n')

        updates = list(map(lambda x: x.split(','), split_data[1].split('\n')))

        return ordering_rules, updates

    def __is_valid(self, values: List[str]) -> bool:
        """Checks if all elements in `values` follow the ordering rules.

        Args:
            values (List[str]): Values to validate.

        Returns:
            bool: Result of validation.
        """
        return all(
            list(
                '|'.join(list(combination)) in self.__ordering_rules
                for combination in list(itertools.combinations(values, 2))
            )
        )

    def __sort_invalid_updates(self, update: List[str]) -> List[str]:
        """Sorts invalid values based on available ordering rules.

        Args:
            update (List[str]): Invalid update to sort.

        Returns:
            List[str]: Sorted update.
        """
        while not self.__is_valid(values=update):
            for i in range(len(update)):
                for j in range(i + 1, len(update)):
                    if f'{update[i]}|{update[j]}' not in self.__ordering_rules:
                        update[i], update[j] = update[j], update[i]

        return update

    def __calculate_middle_sums(self) -> Tuple[int, int]:
        """Calculates middle sums for valid and invalid updates.

        Returns:
            Tuple[int, int]: Valid and invalid update sums of middle numbers.
        """
        valid_sum: int = 0
        invalid_sum: int = 0

        for update in self.__updates:
            if self.__is_valid(values=update):
                valid_sum += int(update[len(update) // 2])
            else:
                update = self.__sort_invalid_updates(update=update)

                invalid_sum += int(update[len(update) // 2])

        return valid_sum, invalid_sum

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: TODO
        """
        return self.__valid_sum

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: TODO
        """
        return self.__invalid_sum

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored(
                'Sum of middle numbers in correctly ordered updates:', 'green'
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'Sum of middle numbers in initially incorrectly ordered'
                'updates:',
                'green',
            ),
            self.solve_puzzle_2(),
        )
