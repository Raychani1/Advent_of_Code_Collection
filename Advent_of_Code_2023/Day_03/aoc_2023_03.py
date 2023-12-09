import re
from typing import Dict, List, Tuple, Union

import numpy as np
from aocd.models import Puzzle
from termcolor import colored


class AOC2023D03:
    def __init__(self) -> None:
        """Initializes the AOC2023D03 Class."""
        self.year: int = 2023
        self.day: int = 3
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__split_data = self.__puzzle.input_data.split('\n')
        self.__data = self.__process_puzzle_input()

    def __extract_special_characters(
        self, special_characters_pattern: str
    ) -> Tuple[
        Dict[str, Dict[str, Dict[str, Union[int, List[int]]]]],
        List[Tuple[str, int, int]],
    ]:
        """Extracts special characters with coordinates.

        Args:
            special_characters_pattern (str): RegEx patter for matching special
            characters.

        Returns:
            Tuple[
                Dict[str, Dict[str, Dict[str, Union[int, List[int]]]]],
                List[Tuple[str, int, int]]
            ]: Extracted special characters and their coordinates.
        """
        processed_data = {}
        special_characters = []

        for row_index, row in enumerate(self.__split_data):
            for column_index, symbol in [
                (m.start(0), m.group())
                for m in re.finditer(
                    pattern=special_characters_pattern, string=row
                )
            ]:
                special_characters.append((symbol, column_index, row_index))
                coordinates = f'({column_index}, {row_index})'
                coordinate_info = {'part_numbers': [], 'sum': 0, 'product': 0}

                if symbol not in processed_data.keys():
                    processed_data[symbol] = {coordinates: coordinate_info}
                else:
                    processed_data[symbol][coordinates] = coordinate_info

        return processed_data, special_characters

    def __extract_numbers_around_special_character(
        self, num_of_digits: int, scc_x: int, scc_y: int, line_length: int
    ) -> List[int]:
        """Extracts numbers around special characters.

        Args:
            num_of_digits (int): Length of numbers to look for.
            scc_x (int): Special character column (x) coordinate.
            scc_y (int): Special character row (y) coordinate.
            line_length (int): Line length for size checks.

        Returns:
            List[int]: Extracted numbers around the given special character.
        """
        part_numbers = []
        offset = num_of_digits + 1
        start_position = scc_x - offset if scc_x - offset >= 0 else 0
        end_position = (
            (scc_x + offset + 1)
            if (scc_x + offset + 1) <= line_length
            else line_length
        )

        beginning_of_row = '*' if scc_x <= 4 and num_of_digits == 3 else ''
        end_of_row = (
            '*' if (line_length - scc_x) <= 4 and num_of_digits == 3 else ''
        )

        up_down_regex = fr'(?=\.{beginning_of_row}(\d{{num_of_digits}})\.{end_of_row})'.replace(
            'num_of_digits', str(num_of_digits)
        )
        left_regex = fr'\.{beginning_of_row}(\d{{num_of_digits}})'.replace(
            'num_of_digits', str(num_of_digits)
        )
        right_regex = r'(\d{num_of_digits})\.'.replace(
            'num_of_digits', str(num_of_digits)
        )

        part_numbers.extend(
            list(
                map(
                    int,
                    set(
                        [
                            m
                            for m in re.findall(
                                up_down_regex,
                                self.__split_data[scc_y - 1][
                                    start_position:end_position
                                ],
                            )
                        ]
                    ),
                )
            )
        )
        part_numbers.extend(
            list(
                map(
                    int,
                    set(
                        [
                            m
                            for m in re.findall(
                                up_down_regex,
                                self.__split_data[scc_y + 1][
                                    start_position:end_position
                                ],
                            )
                        ]
                    ),
                )
            )
        )

        part_numbers.extend(
            list(
                map(
                    int,
                    set(
                        [
                            m
                            for m in re.findall(
                                left_regex,
                                self.__split_data[scc_y][start_position:scc_x],
                            )
                        ]
                    ),
                )
            )
        )

        part_numbers.extend(
            list(
                map(
                    int,
                    set(
                        [
                            m
                            for m in re.findall(
                                right_regex,
                                self.__split_data[scc_y][scc_x:end_position],
                            )
                        ]
                    ),
                )
            )
        )

        return part_numbers

    def __process_puzzle_input(
        self,
    ) -> Dict[str, Dict[str, Dict[str, Union[int, List[int]]]]]:
        """Processes Puzzle Input.

        Returns:
            Dict[str, Dict[str, Dict[str, Union[int, List[int]]]]]: Processed
            Puzzle Input.
        """
        special_characters_pattern = (
            r'''([!@#$%^&*\(\)_+\-=\[\]{};':"\\|,<>\/?])'''
        )
        line_length = len(self.__split_data[0])

        processed_data, special_characters = self.__extract_special_characters(
            special_characters_pattern=special_characters_pattern
        )

        for special_character in special_characters:
            symbol, scc_x, scc_y = special_character
            part_numbers = []

            for num_of_digits in range(1, 4):
                part_numbers.extend(
                    self.__extract_numbers_around_special_character(
                        num_of_digits=num_of_digits,
                        scc_x=scc_x,
                        scc_y=scc_y,
                        line_length=line_length,
                    )
                )

            coordinate_key = f'({scc_x}, {scc_y})'
            processed_data[symbol][coordinate_key][
                'part_numbers'
            ] = part_numbers
            processed_data[symbol][coordinate_key]['sum'] = sum(part_numbers)
            processed_data[symbol][coordinate_key]['product'] = (
                np.prod(part_numbers) if len(part_numbers) >= 2 else 0
            )

        return processed_data

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Sum of all of the part numbers in the engine schematic.
        """
        return sum(
            [
                coordinate['sum']
                for symbol_dict in self.__data.values()
                for coordinate in symbol_dict.values()
            ]
        )

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Sum of all of the gear ratios in the engine schematic.
        """
        return sum([gear['product'] for gear in self.__data['*'].values()])

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored(
                'The sum of all part numbers in the engine schematic is:',
                'green',
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'The sum of all gear ratios in the engine schematic is:',
                'green',
            ),
            self.solve_puzzle_2(),
        )
