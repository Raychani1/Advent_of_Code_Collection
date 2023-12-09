import re
from typing import Dict, Set, Union

from aocd.models import Puzzle
from termcolor import colored


class AOC2023D04:
    def __init__(self) -> None:
        """Initializes the AOC2023D04 Class."""
        self.year: int = 2023
        self.day: int = 4
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(
        self,
    ) -> Dict[int, Dict[str, Union[int, Set[int]]]]:
        """Processes Puzzle Input.

        Returns:
            Dict[int, Dict[str, Union[int, Set[int]]]]: Processed Puzzle Input.
        """
        data = {}

        for card, numbers in [
            data.split(':') for data in self.__puzzle.input_data.split('\n')
        ]:

            winning_numbers, card_numbers = numbers.split('|')
            winning_numbers = set(map(int, winning_numbers.split()))
            card_numbers = set(map(int, card_numbers.split()))
            matches = len(winning_numbers.intersection(card_numbers))
            points = 2 ** (matches - 1) if matches != 0 else 0

            data[int(re.findall(r'Card\ +(\d+)', card)[0])] = {
                'winning_numbers': winning_numbers,
                'card_numbers': card_numbers,
                'matches': matches,
                'number_of_cards': 1,
                'points': points,
            }

        for card_id in sorted(data.keys()):
            for i in range(1, data[card_id]['matches'] + 1):
                data[card_id + i]['number_of_cards'] += (
                    data[card_id]['number_of_cards'] * 1
                )

        return data

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Cards worth in points.
        """
        return sum([card['points'] for card in self.__data.values()])

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of total scratchcards.
        """
        return sum([card['number_of_cards'] for card in self.__data.values()])

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('The cards are worth', 'green'),
            self.solve_puzzle_1(),
            colored('points in total.', 'green'),
        )

        print(
            colored('We end up with a total of', 'green'),
            self.solve_puzzle_2(),
            colored('scratchcards.', 'green'),
        )
