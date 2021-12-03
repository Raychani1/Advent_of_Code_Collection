import re
from aocd import submit
from termcolor import colored
from aocd.models import Puzzle
from typing import List
from collections import Counter


class AOC2021D03:

    def __init__(self) -> None:
        """Initialize the AOC2021D03 Class."""

        self.__year: int = 2021
        self.__day: int = 3
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: List[List[str]] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[str]]:
        """Process Puzzle Input.

        Returns:
            List[List[str]]: Processed Puzzle Input

        """

        columns: int = len(self.__puzzle.input_data.split('\n')[0])

        column_data: List[List[str]] = []

        for column in range(columns):
            current_column: List[str] = []

            for row in self.__puzzle.input_data.split('\n'):
                current_column.append(row[column])

            column_data.append(current_column)

        return column_data

    def __solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: Power Consumption of the Submarine

        """

        gamma: str = ''

        for column in self.__data:
            gamma += str(Counter(column).most_common(1)[0][0])

        epsilon: str = ''.join('1' if x == '0' else '0' for x in gamma)

        return int(gamma, 2) * int(epsilon, 2)

    def __get_rating(
            self,
            data: List[str],
            bit: int = 0,
            format_string: str = '',
            rating_type: str = ''
    ) -> str:
        """Get Rating for a specific Type.

        Args:
            data (List[str]): Data to work with
            bit (int): Current examined bit
            format_string (str): Historical Format String to match in Regex
            rating_type (str): Type of Rating [ 'o2' | 'co2' ]

        Returns:
            str: Found Rating

        """

        if len(data) == 1:
            return data[0]

        counter: Counter = Counter(x[bit] for x in data)

        if counter.most_common()[0][1] == counter.most_common()[1][1]:
            format_bit: str = sorted(counter.items())[rating_type == 'o2'][0]
        else:
            format_bit: str = str(counter.most_common()[rating_type != 'o2'][0])

        format_string += format_bit

        r: re.Pattern = re.compile(
            f"^{format_string}.*$"
        )

        return self.__get_rating(
            bit=bit + 1,
            rating_type=rating_type,
            format_string=format_string,
            data=list(filter(r.match, data))
        )

    def __solve_puzzle_2(self) -> int:
        """Solve the second part of the Puzzle.

        Returns:
            int: Life Support Rating of the Submarine

        """

        split_data: List[str] = self.__puzzle.input_data.split('\n')

        return int(
            self.__get_rating(
                data=split_data,
                rating_type='o2'
            ), 2
        ) * int(
            self.__get_rating(
                data=split_data,
                rating_type='co2'
            ), 2
        )

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            colored(
                'The Power Consumption of the Submarine:',
                'green'
            ),
            self.__solve_puzzle_1()
        )

        print(
            colored(
                'The Life Support Rating of the Submarine:',
                'green'
            ),
            self.__solve_puzzle_2()
        )

    def solve_and_submit_puzzles(self) -> None:
        """Solve both Puzzles and Submit the Solution to the Advent of Code
            Website.

        """

        submit(
            year=self.__year,
            day=self.__day,
            part="a",
            answer=self.__solve_puzzle_1()
        )
        submit(
            year=self.__year,
            day=self.__day,
            part="b",
            answer=self.__solve_puzzle_2()
        )
