import re
from typing import Dict, List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2023D02:
    def __init__(self) -> None:
        """Initializes the AOC2023D02 Class."""
        self.year: int = 2023
        self.day: int = 2
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Dict[int, List[Tuple[int, int, int]]]:
        """Processes Puzzle Input.

        Returns:
            Dict[int, List[Tuple[int, int, int]]]: Processed Puzzle Input.
        """
        game_data: Dict[int, List[Tuple[int, int, int]]] = {}

        for game in self.__puzzle.input_data.split('\n'):
            split_data = game.split(':')
            game_id = int(split_data[0].split()[-1])
            game_data[game_id] = []

            grabs = split_data[-1].split(';')

            for grab in grabs:
                red_regex = re.findall(r'(\d+) red', grab)
                green_regex = re.findall(r'(\d+) green', grab)
                blue_regex = re.findall(r'(\d+) blue', grab)

                red = int(red_regex[0]) if red_regex else 0
                green = int(green_regex[0]) if green_regex else 0
                blue = int(blue_regex[0]) if blue_regex else 0

                game_data[game_id].append((red, green, blue))

        return game_data

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Sum of valid game IDs.
        """
        valid = []
        available_pieces = (12, 13, 14)

        for game_id, grabs in self.__data.items():
            grab_validity = []

            for grab in grabs:
                current_grab = [i <= j for i, j in zip(grab, available_pieces)]
                grab_validity.extend(current_grab)

                # Break the loop if there are any invalid grabs
                if not all(grab_validity):
                    break

            if all(grab_validity):
                valid.append(game_id)

        return sum(valid)

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Sum of cube set powers.
        """
        # Select the larges grab for each color and calculate the power for
        # each game then sum it
        return sum(
            [
                max(list(zip(*grabs))[0])
                * max(list(zip(*grabs))[1])
                * max(list(zip(*grabs))[2])
                for grabs in self.__data.values()
            ]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            self.solve_puzzle_1(),
            colored('is the sum of the IDs of those games.', 'green'),
        )

        print(
            self.solve_puzzle_2(),
            colored('is the sum of the power of these sets.', 'green'),
        )
