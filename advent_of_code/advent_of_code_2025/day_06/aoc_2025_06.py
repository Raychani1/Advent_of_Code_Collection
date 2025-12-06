from math import prod
from typing import Dict, List, Union

from aocd.models import Puzzle
from termcolor import colored


class AOC2025D06:

    def __init__(self) -> None:
        """Initializes the AOC2025D06 Class."""
        self.year: int = 2025
        self.day: int = 6
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> Dict[str, List[Union[str, int]]]:
        """Processes Puzzle Input.

        Returns:
            Dict[str, List[Union[str, int]]]: Processed Puzzle Input.
        """
        row_split_data = self.__puzzle.input_data.split('\n')
        number_split_data = [row.split() for row in row_split_data]
        column_split_data = [list(row) for row in row_split_data[:-1]]

        return {
            'operations': number_split_data[-1],
            'part_1_numbers': [
                [int(num)for num in row] for row in number_split_data[:-1]
            ],
            'part_2_numbers': self.__process_part_2_input(
                data=column_split_data
            )
        }
    
    def __process_part_2_input(self, data: List[List[str]]) -> List[List[int]]:
        """Processes input data for Part 2.

        Args:
            data (List[List[str]]): Data to process for Part 2.

        Returns:
            List[List[int]]: Processed input for Part 2.
        """
        part_2_numbers = []
        current_number_group = []
        for col_index in range(len(data[0])):
            number = []
            for row in data:
                number.append(row[col_index])
            joint_number = ''.join(number).replace(' ', '')
            
            if joint_number:
                current_number_group.append(int(joint_number))
            else:
                part_2_numbers.append(current_number_group)
                current_number_group = []
        part_2_numbers.append(current_number_group) 

        return part_2_numbers 

    def __solve_puzzle(self, part: int) -> int:
        """Solves puzzle with input based on `part`.

        Args:
            part (int): Indicator which part of the puzzle is being solved.

        Returns:
            int: Puzzle result.
        """
        result = 0

        for index, operation in enumerate(self.__data['operations']):
            numbers_to_process = (
                [
                    number[index] for number in self.__data['part_1_numbers']
                ] if part == 1 else self.__data['part_2_numbers'][index]
            )
            if operation == '+':
                result += sum(numbers_to_process)
            elif operation == '*':
                result += prod(numbers_to_process)

        return result

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Grand total of operation results for vertical groups.
        """
        return self.__solve_puzzle(part=1)

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Grand total of operation results for vertical numbers.
        """
        return self.__solve_puzzle(part=2)

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Grand total of operation results for vertical groups:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('Grand total of operation results for vertical numbers:', 'green'),
            self.solve_puzzle_2(),
        )