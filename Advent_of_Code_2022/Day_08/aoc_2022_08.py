from typing import List

import numpy as np
from aocd.models import Puzzle
from termcolor import colored


class AOC2022D08:

    def __init__(self) -> None:
        """Initialize the AOC2022D08 Class."""
        self.year: int = 2022
        self.day: int = 8
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: List[List[int]] = self.__process_puzzle_input()
        self.__data_transposed: List[List[int]] = [
            list(i) for i in zip(*self.__data)
        ]

    def __process_puzzle_input(self) -> List[List[int]]:
        """Process Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input.
        """
        return [
            list(map(int, x))
            for x in list(map(list, self.__puzzle.input_data.split('\n')))
        ]

    def solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: Number of trees visible from outside the grid.
        """

        visibility = np.ones((len(self.__data), len(self.__data[0])))

        for i in range(1, len(self.__data) - 1):
            for j in range(1, len(self.__data[0]) - 1):
                if (
                    self.__data[i][j] <= max(self.__data[i][:j]) and
                    self.__data[i][j] <= max(self.__data[i][j + 1:]) and
                    self.__data[i][j] <= max(self.__data_transposed[j][:i]) and
                    self.__data[i][j] <= max(self.__data_transposed[j][i+1:])
                ):
                    visibility[i][j] = 0

        return int(sum(sum(visibility)))

    @staticmethod
    def __find_first_greater_or_equal_tree(
        trees: List[int],
        current_tree: int
    ) -> int:
        """Find the index of first greater or equal tree in list.

        Args:
            trees (List[int]): Tree heights in given direction.
            current_tree (int): Current trees height. 

        Returns:
            int: Index of first greater or equal tree in list.
        """
        return trees.index(
            list(filter(lambda k: k >= current_tree, trees))[0]
        )

    def solve_puzzle_2(self) -> int:
        """Solve the second part of the Puzzle.

        Returns:
            int: Highest scenic score possible for any tree.
        """
        scenic_scores = np.zeros((len(self.__data), len(self.__data[0])))

        for i in range(1, len(self.__data) - 1):
            for j in range(1, len(self.__data[0]) - 1):
                directions = []

                current = self.__data[i][j]

                mappings = {
                    'Left': {
                        'trees': self.__data[i][:j][::-1],
                        'current': j,
                        'offset': -1
                    },
                    'Right': {
                        'trees': self.__data[i][j+1:],
                        'current': abs(len(self.__data[0]) - (j+1)),
                        'offset': 1
                    },
                    'Up': {
                        'trees': self.__data_transposed[j][:i][::-1],
                        'current': i,
                        'offset': 1
                    },
                    'Down': {
                        'trees': self.__data_transposed[j][i+1:],
                        'current': abs(len(self.__data) - (i+1)),
                        'offset': 1
                    }
                }

                # Calculate Scenic Score for each direction
                for _, direction in mappings.items():
                    directions.append(
                        direction['current']
                        if current > max(direction['trees']) else
                        self.__find_first_greater_or_equal_tree(
                            trees=direction['trees'],
                            current_tree=current
                        ) + direction['offset']
                    )

                scenic_scores[i][j] = np.prod(directions)

        return int(np.max(scenic_scores))

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""
        print(
            self.solve_puzzle_1(),
            colored(
                'trees are visible from outside the grid.',
                'green'
            ),
        )

        print(
            colored(
                'Highest scenic score possible for any tree:',
                'green'
            ),
            self.solve_puzzle_2(),
        )
