from typing import Callable, List, Tuple

import numpy as np
from aocd.models import Puzzle
from termcolor import colored

from advent_of_code.utils.list_utils import chunks_of_size


class AOC2025D02:
    def __init__(self) -> None:
        """Initializes the AOC2025D02 Class."""
        self.year: int = 2025
        self.day: int = 2
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[Tuple[int, int]]:
        """Processes Puzzle Input.

        Returns:
            List[Tuple[int, int]]: Processed Puzzle Input.
        """
        return [
            tuple(
                [int(val) for val in ranges.split('-')]
            ) for ranges in self.__puzzle.input_data.split(',')
        ]
    
    @staticmethod
    def __is_invalid_product_part_1(product_id: int) -> bool:
        """Checks wether product IDs is invalid in terms of Part 1.

        Product ID is invalid, if the number is repeated twice.

        Args:
            product_id (int): Product ID to validate.

        Returns:
            bool: Product ID validation result.
        """
        product_id_str = str(product_id)
        
        if len(product_id_str) % 2 == 1:
            return False
        else:
            half = round(len(product_id_str) / 2)
            return product_id_str[:half] == product_id_str[half:]
    
    @staticmethod
    def __is_invalid_product_part_2(product_id: int) -> bool:
        """Checks wether product IDs is invalid in terms of Part 2.

        Product ID is invalid, if the number is repeated at least twice.

        Args:
            product_id (int): Product ID to validate.

        Returns:
            bool: Product ID validation result.
        """
        product_id_str = str(product_id)

        half = round(len(product_id_str) / 2)

        for window_size in range(half, 0, -1):
            if len(
                set(
                    chunks_of_size(
                        values=product_id_str, chunk_size=window_size
                    )
                )
            ) == 1:
                return True

        return False
    
    def __solve_puzzle(self, func: Callable) -> int:
        """Solves puzzle with the associated validation `func`.

        Args:
            func (Callable): Product ID validation function.

        Returns:
            int: Sum of invalid products based on `func`.
        """
        result = 0

        for range_start, range_end in self.__data:
            products = np.array(range(range_start, range_end + 1))
            is_invalid_v = np.vectorize(func, otypes=[bool])
            mask = is_invalid_v(products)
            result += sum(products[mask])

        return result

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Sum of invalid products.
        """
        return self.__solve_puzzle(func=self.__is_invalid_product_part_1)
        

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Sum of invalid products.
        """
        return self.__solve_puzzle(func=self.__is_invalid_product_part_2)

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Sum of invalid products (IDs repeating twice):', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'Sum of invalid products (IDs repeating at least twice):',
                'green'
            ),
            self.solve_puzzle_2(),
        )
