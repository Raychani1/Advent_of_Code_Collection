import itertools
from typing import Dict, List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D08:
    def __init__(self) -> None:
        """Initializes the AOC2024D08 Class."""
        self.year: int = 2024
        self.day: int = 8
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        (
            self.__num_of_rows,
            self.__num_of_col,
            self.__data,
        ) = self.__process_puzzle_input()

    def __process_puzzle_input(
        self,
    ) -> Tuple[int, int, Dict[str, List[Tuple[int, int]]]]:
        """Processes Puzzle Input.

        Returns:
            Tuple[int, int, Dict[str, List[Tuple[int, int]]]]: Processed Puzzle
                Input. Number of rows, number of columns, and antenna
                coordinates.
        """
        split_data = list(map(list, self.__puzzle.input_data.split('\n')))
        num_of_rows = len(split_data)
        num_of_cols = len(split_data[0])

        antenna_coordinates: Dict[str, List[Tuple[int, int]]] = {}

        for i, j in itertools.product(range(num_of_rows), range(num_of_cols)):
            if split_data[i][j] != '.':
                if split_data[i][j] not in antenna_coordinates.keys():
                    antenna_coordinates[str(split_data[i][j])] = [(i, j)]
                else:
                    antenna_coordinates[str(split_data[i][j])].append((i, j))

        return num_of_rows, num_of_cols, antenna_coordinates

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

    @staticmethod
    def mirror_point(
        original_point: Tuple[int, int], mirror_point: Tuple[int, int]
    ) -> Tuple[int, int]:
        """Calculates the mirrored point of `original_point` relative to
        `mirror_point`.

        Args:
            original_point (Tuple[int, int]): The original point (x, y).
            mirror_point (Tuple[int, int]): The point to mirror around (a, b).

        Returns:
            Tuple[int, int]: The mirrored point (x', y').
        """
        x, y = original_point
        a, b = mirror_point
        mirrored_x = 2 * a - x
        mirrored_y = 2 * b - y

        return (mirrored_x, mirrored_y)

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of unique antinode locations.
        """
        mirrored_points = set()

        for _, coordinates in self.__data.items():
            for original, mirror in list(
                itertools.combinations(coordinates, 2)
            ):
                simple_mirrored = self.mirror_point(original, mirror)
                reverse_mirrored = self.mirror_point(mirror, original)

                if self.__in_range(point=simple_mirrored):
                    mirrored_points.add(simple_mirrored)

                if self.__in_range(point=reverse_mirrored):
                    mirrored_points.add(reverse_mirrored)

        return len(mirrored_points)

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of unique antinode locations with the updated model.
        """
        mirrored_points = set()

        for _, coordinates in self.__data.items():

            for original, mirror in list(
                itertools.combinations(coordinates, 2)
            ):
                # Forward mirror
                simple_original = original
                simple_mirror = mirror

                simple_mirrored = self.mirror_point(
                    original_point=simple_original, mirror_point=simple_mirror
                )

                while self.__in_range(point=simple_mirrored):
                    mirrored_points.add(simple_mirrored)

                    simple_original = simple_mirror
                    simple_mirror = simple_mirrored
                    simple_mirrored = self.mirror_point(
                        original_point=simple_original,
                        mirror_point=simple_mirror,
                    )

                # Reverse mirror
                reverse_original = mirror
                reverse_mirror = original

                reverse_mirrored = self.mirror_point(
                    original_point=reverse_original, mirror_point=reverse_mirror
                )

                while self.__in_range(point=reverse_mirrored):
                    mirrored_points.add(reverse_mirrored)

                    reverse_original = reverse_mirror
                    reverse_mirror = reverse_mirrored
                    reverse_mirrored = self.mirror_point(
                        original_point=reverse_original,
                        mirror_point=reverse_mirror,
                    )

            # Add antinodes that appear on every antenna
            mirrored_points.update(coordinates)

        return len(mirrored_points)

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Number of unique antinode locations:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'Number of unique antinode locations with the updated model:',
                'green',
            ),
            self.solve_puzzle_2(),
        )
