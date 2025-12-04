from collections import Counter
from typing import List, Tuple

from aocd.models import Puzzle
from termcolor import colored

from advent_of_code.utils.list_utils import get_2d_neighbor_elements


class AOC2025D04:

    def __init__(self) -> None:
        """Initializes the AOC2025D04 Class."""
        self.year: int = 2025
        self.day: int = 4
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[str]]:
        """Processes Puzzle Input.

        Returns:
            List[List[str]]: Processed Puzzle Input.
        """
        return [list(row) for row in self.__puzzle.input_data.split('\n')]

    def __check_for_neighbor_paper(
        self, current_row: int, current_col: int
    ) -> bool:
        """Checks wether a given paper roll at `current_row`;`current_col` is
        accessible (less than 4 paper rolls around it).

        Args:
            current_row (int): Current row index.
            current_col (int): Current column index.

        Returns:
            bool: `True` if < 4 are around the given paper else `False`. 
        """
        return Counter(
            get_2d_neighbor_elements(
                data=self.__data,
                current_row=current_row,
                current_col=current_col
            )
        )['@'] < 4

    def __get_coordinates_of_accessible_papers(
        self, data: List[List[str]]
    ) -> List[Tuple[int, int]]:
        """Gets coordinates of accessible / removable papers.

        Args:
            data (List[List[str]]): Data to process.

        Returns:
            List[Tuple[int, int]]: List of accessible / removable paper
                coordinates.
        """
        coordinates = []
        for row_id, row in enumerate(data):
            for col_id, col in enumerate(row):
                if col == '@' and self.__check_for_neighbor_paper(
                        current_row=row_id,
                        current_col=col_id
                    ):
                        coordinates.append((row_id, col_id))

        return coordinates

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of accessible papers.
        """
        return len(
            self.__get_coordinates_of_accessible_papers(data=self.__data)
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of removed papers.
        """
        coordinates_to_remove = [(0,0)]
        data = self.__data
        removed_paper = 0

        # Iterate until we have no more paper to remove
        while len(coordinates_to_remove) != 0:

            # Get the position and number of removable paper
            coordinates_to_remove = self.__get_coordinates_of_accessible_papers(
                data=data
            )
            removed_paper += len(coordinates_to_remove)

            # Remove what we can
            for row, col in coordinates_to_remove:
                data[row][col] = '.'
            
        return removed_paper

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Number of accessible papers:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('Number of removable papers:', 'green'),
            self.solve_puzzle_2(),
        )
