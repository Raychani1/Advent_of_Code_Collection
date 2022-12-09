import operator
from typing import Dict, List, Tuple

from aocd.models import Puzzle
from termcolor import colored

from utils.utility_functions import filter_dictionary


class AOC2022D07:

    def __init__(self) -> None:
        """Initialize the AOC2022D07 Class."""
        self.year: int = 2022
        self.day: int = 7
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: Dict[str, int] = self.__process_puzzle_input()

    @staticmethod
    def __process_cd_command(
        file_system: Dict[str, int],
        current_dir: str,
        split_terminal_line: List[str]
    ) -> Tuple[Dict[str, int], str]:
        """Process Change Directory Command.

        Args:
            file_system (Dict[str, int]): Current File System.
            current_dir (str): Current Directory.
            split_terminal_line (List[str]): Split terminal command.

        Returns:
            Tuple[Dict[str, int], str]: Updated values.
        """
        if 'cd' in split_terminal_line:
            if split_terminal_line[-1] not in ['/', '..']:
                current_dir = (
                    f"{current_dir if current_dir != '/' else ''}/"
                    f"{split_terminal_line[-1]}"
                )
                file_system[current_dir] = 0
            elif split_terminal_line[-1] == '..':
                current_dir = '/'.join(
                    current_dir.split('/')[:-1]
                )

        return file_system, current_dir

    def __process_terminal_commands(self) -> Dict[str, int]:
        """Process Terminal Commands

        Returns:
            Dict[str, int]: Loaded File System.
        """
        file_system = {'/': 0}
        current_dir = '/'

        for terminal_line in self.__puzzle.input_data.split('\n'):
            split_terminal_line = terminal_line.split()

            if terminal_line[0] == '$':
                file_system, current_dir = self.__process_cd_command(
                    file_system=file_system,
                    current_dir=current_dir,
                    split_terminal_line=split_terminal_line
                )

            else:
                if split_terminal_line[0].isdigit():
                    file_system[current_dir] += int(split_terminal_line[0])

        return file_system

    @staticmethod
    def __sum_dir_sizes(file_system: Dict[str, int]) -> Dict[str, int]:
        """Add directory size to parent directory size.

        Args:
            file_system (Dict[str, int]): Current File System.

        Returns:
            Dict[str, int]: Updated File System.
        """
        for key in sorted(file_system, key=len, reverse=True):
            if key != '/':
                parent_dir = '/'.join(key.split('/')[:-1])
                file_system[
                    parent_dir if parent_dir != '' else '/'
                ] += file_system[key]

        return file_system

    def __process_puzzle_input(
        self
    ) -> Dict[str, int]:
        """Process Puzzle Input.

        Returns:
            Dict[str, int]: Processed Puzzle Input.
        """
        return self.__sum_dir_sizes(
            file_system=self.__process_terminal_commands()
        )

    def __find_dir_size(
        self,
        relate: operator,
        size_limit: int
    ) -> List[int]:
        """Find directories which have specific size.

        Args:
            relate (operator): Operator of specification.
            size_limit (int): Size limit.

        Returns:
            List[int]: List of filtered values.
        """
        return list(
            filter_dictionary(
                self.__data,
                lambda elem: relate(elem[1], size_limit)
            ).values()
        )

    def solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: The sum of the total sizes of selected directories.
        """
        return sum(
            self.__find_dir_size(
                relate=operator.lt,
                size_limit=100000
            )
        )

    def solve_puzzle_2(self) -> str:
        """Solve the second part of the Puzzle.

        Returns:
            int: The total sizes of selected directory.
        """

        return sorted(
            self.__find_dir_size(
                relate=operator.gt,
                size_limit=(self.__data['/'] - 40000000)
            )
        )[0]

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""
        print(
            colored(
                'The sum of the total sizes of selected directories is',
                'green'
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'The total sizes of selected directory is',
                'green'
            ),
            self.solve_puzzle_2(),            
        )
