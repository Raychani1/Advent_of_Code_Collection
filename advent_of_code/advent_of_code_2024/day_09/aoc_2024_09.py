import copy
from collections import Counter
from typing import Any, List, Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D09:
    def __init__(self) -> None:
        """Initializes the AOC2024D09 Class."""
        self.year: int = 2024
        self.day: int = 9
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__free_space: str = '.'
        self.__data: List[str] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[str]:
        """Processes Puzzle Input.

        Returns:
            List[str]: Processed Puzzle Input.
        """
        data = []

        for index, value in enumerate(
            list(map(int, list(self.__puzzle.input_data)))
        ):
            if index % 2:
                data.extend([self.__free_space] * value)
            else:
                data.extend([str(index // 2)] * value)

        return data

    @staticmethod
    def __swap_first_dot_with_last_non_dot(
        elements: List[Any], value: Any
    ) -> List[Any]:
        """Swaps the first `value` with the last non `value` element in the
        list.

        Args:
            elements (List[Any]): List of elements to process.
            value (Any): Value which needs to be swapped.

        Returns:
            List[Any]: Elements with the first `value` and the last non `value`
                swapped.
        """
        # Find the first occurrence of `value`
        first_dot_index = elements.index(value)

        # Find the last occurrence of a non `value` element
        last_non_dot_index = (
            len(elements)
            - 1
            - elements[::-1].index(
                next(x for x in reversed(elements) if x != value)
            )
        )

        # Swap the elements
        elements[first_dot_index], elements[last_non_dot_index] = (
            elements[last_non_dot_index],
            elements[first_dot_index],
        )

        return elements

    @staticmethod
    def __find_value_blocks(
        elements: List[Any], value: Any
    ) -> List[Tuple[int, int]]:
        """Find starting index and length of each consecutive `value` block in
        the `elements` list.

        Args:
            elements (List[Any]): The input list of elements.
            value (Any): Value to

        Returns:
            List[Tuple[int, int]]: Each tuple contains (start_index, length) of
                `value` blocks.
        """
        dot_blocks = []
        n = len(elements)
        i = 0

        while i < n:
            if elements[i] == value:
                start = i
                length = 0
                while i < n and elements[i] == value:
                    length += 1
                    i += 1
                dot_blocks.append((start, length))
            else:
                i += 1

        return dot_blocks

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Filesystem checksum.
        """
        data = copy.deepcopy(self.__data)

        number_of_free_spaces = Counter(data)[self.__free_space]

        for _ in range(len(data) - number_of_free_spaces + 1):
            self.__swap_first_dot_with_last_non_dot(
                elements=data, value=self.__free_space
            )

        return sum(
            [
                index * int(value)
                for index, value in enumerate(
                    list(filter(lambda x: x != self.__free_space, data))
                )
            ]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Updated filesystem checksum.
        """
        data = copy.deepcopy(self.__data)

        number_of_files = Counter(data)
        largest_file_id = int(max(number_of_files.keys()))

        # For each File ID
        for file_id in range(largest_file_id, 0, -1):
            file = str(file_id)
            file_starting_index = data.index(file)
            number_of_file = number_of_files[file]

            # Identify relevant blocks of free space where files might fit
            dot_blocks = list(
                filter(
                    lambda x: x[1] >= number_of_files[file],
                    self.__find_value_blocks(
                        elements=data, value=self.__free_space
                    ),
                )
            )

            # If a free space block exists before the file move it
            if dot_blocks and dot_blocks[0][0] < file_starting_index:
                (
                    data[dot_blocks[0][0] : dot_blocks[0][0] + number_of_file],
                    data[
                        file_starting_index : file_starting_index
                        + number_of_file
                    ],
                ) = (
                    data[
                        file_starting_index : file_starting_index
                        + number_of_file
                    ],
                    data[dot_blocks[0][0] : dot_blocks[0][0] + number_of_file],
                )

        return sum(
            [
                index * int(value)
                for index, value in enumerate(data)
                if value != self.__free_space
            ]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Filesystem checksum:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('Updated filesystem checksum:', 'green'),
            self.solve_puzzle_2(),
        )
