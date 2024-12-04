import itertools
import re
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored

from advent_of_code.utils.utils import (
    get_diagonal_centered,
    get_diagonal_starting,
)


class AOC2024D04:
    def __init__(self) -> None:
        """Initializes the AOC2024D04 Class."""
        self.year: int = 2024
        self.day: int = 4
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__horizontal, self.__vertical = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Tuple[List[str], List[str]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[List[str], List[str]]: Processed Puzzle Input. Rows and
                columns of the input data.
        """
        horizontal = self.__puzzle.input_data.split('\n')
        vertical = list(
            map(lambda x: ''.join(x), list(zip(*list(map(list, horizontal)))))
        )

        return horizontal, vertical

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of times 'XMAS' appeared.
        """
        part_1_regex: str = r'(?=(XMAS|SAMX))'
        results: List[str] = []

        # Check horizontally
        for horizontal in self.__horizontal:
            results.extend(re.findall(part_1_regex, horizontal))

        # Check vertically
        for vertical in self.__vertical:
            results.extend(re.findall(part_1_regex, vertical))

        # Check diagonally
        for row, col, direction in list(
            itertools.product(
                range(len(self.__horizontal)),
                range(len(self.__horizontal[0])),
                ['main', 'anti'],
            )
        ):
            results.extend(
                re.findall(
                    part_1_regex,
                    ''.join(
                        get_diagonal_starting(
                            matrix=self.__horizontal,
                            start_row=row,
                            start_col=col,
                            num_elements=4,
                            direction=direction,
                        )
                    ),
                )
            )

        return len(results)

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of times 'X-MAS' appeared.
        """
        part_2_regex: str = r'(MAS|SAM)'
        results: List[bool] = []

        # Check X shape for each element
        for row, col in list(
            itertools.product(
                range(len(self.__horizontal)), range(len(self.__horizontal[0]))
            )
        ):
            current = []
            for direction in ['main', 'anti']:
                current.append(
                    ''.join(
                        get_diagonal_centered(
                            matrix=self.__horizontal,
                            center_row=row,
                            center_col=col,
                            num_elements=3,
                            direction=direction,
                        )
                    )
                )

            # Check if 'MAS' is in the X shape
            results.append(
                all([bool(re.search(part_2_regex, value)) for value in current])
            )

        return sum(results)

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored("'XMAS' appeared", 'green'),
            self.solve_puzzle_1(),
            colored('times.', 'green'),
        )

        print(
            colored("'X-MAS' appeared", 'green'),
            self.solve_puzzle_2(),
            colored('times.', 'green'),
        )
