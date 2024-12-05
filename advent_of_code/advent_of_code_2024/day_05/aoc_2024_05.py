import itertools
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D05:
    def __init__(self) -> None:
        """Initializes the AOC2024D04 Class."""
        self.year: int = 2024
        self.day: int = 5
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__ordering_rules, self.__updates = self.__process_puzzle_input()

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
        # ordering_rules: Dict[str, List[str]] = {}

        # for ordering_rules_info in split_data[0].split('\n'):
        #     split_info = ordering_rules_info.split('|')

        #     if split_info[0] not in ordering_rules.keys():
        #         ordering_rules[split_info[0]] = [split_info[1]]
        #     else:
        #         ordering_rules[split_info[0]].append(split_info[1])

        updates = list(map(lambda x: x.split(','), split_data[1].split('\n')))

        return ordering_rules, updates

    def __is_valid(self, values: List[str]) -> bool:
        # TODO - Docstring
        return all(
            list(
                '|'.join(list(combination)) in self.__ordering_rules
                for combination in list(itertools.combinations(values, 2))
            )
        )

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: TODO
        """
        middle_sum: int = 0

        for update in self.__updates:
            if self.__is_valid(values=update):
                middle_sum += int(update[len(update) // 2])

        return middle_sum

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: TODO
        """
        middle_sum = 0

        for update in self.__updates:
            if not self.__is_valid(values=update):
                for permutation in list(itertools.permutations(update)):
                    if self.__is_valid(values=list(permutation)):
                        middle_sum += int(permutation[len(permutation) // 2])

        return middle_sum

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('TODO', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('TODO', 'green'),
            self.solve_puzzle_2(),
        )
