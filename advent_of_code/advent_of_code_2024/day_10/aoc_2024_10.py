import itertools
from collections import deque
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D10:
    def __init__(self) -> None:
        """Initializes the AOC2024D10 Class."""
        self.year: int = 2024
        self.day: int = 10
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        (
            self.__num_of_rows,
            self.__num_of_col,
            self.__layout,
            self.__starting_positions,
        ) = self.__process_puzzle_input()

    def __process_puzzle_input(
        self,
    ) -> Tuple[int, int, List[List[int]], List[Tuple[int, int]]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[int, int, List[List[int]], List[Tuple[int, int]]]: Processed
                Puzzle Input.
        """
        layout = [
            list(map(int, row))
            for row in list(
                map(lambda x: list(x), self.__puzzle.input_data.split('\n'))
            )
        ]

        num_of_rows = len(layout)
        num_of_cols = len(layout[0])

        starting_positions = []

        for i, j in itertools.product(range(num_of_rows), range(num_of_cols)):
            if layout[i][j] == 0:
                starting_positions.append((i, j))

        return num_of_rows, num_of_cols, layout, starting_positions

    def __in_range(self, point: Tuple[int, int]) -> bool:
        """Checks if point is in valid puzzle range.

        Args:
            point (Tuple[int, int]): Point to validate.

        Returns:
            bool: Point range validity.
        """
        return (
            0 <= point[0] < self.__num_of_rows
            and 0 <= point[1] < self.__num_of_col
        )

    def __process_path(
        self, starting_position: Tuple[int, int], count_distinct: bool
    ) -> int:
        """Processes given path from `starting_position`.

        Args:
            starting_position (Tuple[int, int]): The starting position of given
                path.
            count_distinct (bool): Flag wether to search for distinct paths or
                not.

        Returns:
            int: Number of valid path variations.
        """
        queue = deque([starting_position])
        visited = set()
        score_sum = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            y, x = queue.popleft()
            current_value = self.__layout[y][x]

            if current_value == 9:
                score_sum += 1
                continue

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if (
                    self.__in_range((ny, nx))
                    and self.__layout[ny][nx] - current_value == 1
                    and (ny, nx) not in visited
                ):
                    queue.append((ny, nx))
                    visited.add((ny, nx) if count_distinct else ())

        return score_sum

    def __calculate_path_scores(self, count_distinct: bool) -> int:
        """Calculates path scores for each available path.

        Args:
            count_distinct (bool): Flag wether to search for distinct paths or
                not.

        Returns:
            int: Number of valid path variations.
        """
        score_sum = 0

        for starting_position in self.__starting_positions:
            score_sum += self.__process_path(
                starting_position=starting_position,
                count_distinct=count_distinct,
            )

        return score_sum

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Sum of the scores of all trailheads on topographic map.
        """
        return self.__calculate_path_scores(count_distinct=True)

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Sum of the ratings of all trailheads.
        """
        return self.__calculate_path_scores(count_distinct=False)

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored(
                'Sum of the scores of all trailheads on topographic map:',
                'green',
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored('Sum of the ratings of all trailheads:', 'green'),
            self.solve_puzzle_2(),
        )
