from aocd import submit
from termcolor import colored
from aocd.models import Puzzle
from typing import List, Tuple, Dict


class AOC2021D05:

    def __init__(self) -> None:
        """Initialize the AOC2021D05 Class."""

        self.__year: int = 2021
        self.__day: int = 5
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: List[List[Tuple[int, ...]]] = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[Tuple[int, ...]]]:
        """Process Puzzle Input.

        Returns:
            List[List[Tuple[int, ...]]]: Processed Puzzle Input

        """

        data: List[List[Tuple[int, ...]]] = list()

        for element in list(
                map(
                    lambda x: x.split(' -> '),
                    self.__puzzle.input_data.split('\n')
                )
        ):
            data.append(
                [
                    tuple(map(int, element[0].split(','))),
                    tuple(map(int, element[1].split(',')))
                ]
            )

        return data

    @staticmethod
    def __modify_dictionary(dictionary: Dict[str, int], key: str) -> None:
        """Modify the content of the Counter Dictionary.

        Args:
            dictionary (Dict[str, int]): Ventilation Mapping Dictionary
            key (str): Ventilation Mapping Dictionary Key (Coordinates)

        """

        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1

    def __process_horizontal_lines(
            self,
            vent: List[Tuple[int, ...]],
            dictionary: Dict[str, int]
    ) -> None:
        """Process horizontal ventilation line coordinates.

        Args:
            vent (List[Tuple[int, ...]]): Ventilation Coordinates
            dictionary (Dict[str, int]): Ventilation Mapping Dictionary

        """

        for y_position in range(
                min(vent[0][1], vent[1][1]),
                max(vent[0][1], vent[1][1]) + 1
        ):
            self.__modify_dictionary(
                dictionary=dictionary,
                key=str(
                    tuple([vent[0][0], y_position])
                )
            )

    def __process_vertical_lines(
            self,
            vent: List[Tuple[int, ...]],
            dictionary: Dict[str, int]
    ) -> None:
        """Process vertical ventilation line coordinates.

        Args:
            vent (List[Tuple[int, ...]]): Ventilation Coordinates
            dictionary (Dict[str, int]): Ventilation Mapping Dictionary

        """

        for x_position in range(
                min(vent[0][0], vent[1][0]),
                max(vent[0][0], vent[1][0]) + 1
        ):
            self.__modify_dictionary(
                dictionary=dictionary,
                key=str(
                    tuple([x_position, vent[0][1]])
                )
            )

    def __process_diagonal_lines(
            self,
            vent: List[Tuple[int, ...]],
            dictionary: Dict[str, int]
    ) -> None:
        """Process diagonal ventilation line coordinates.

        Args:
            vent (List[Tuple[int, ...]]): Ventilation Coordinates
            dictionary (Dict[str, int]): Ventilation Mapping Dictionary

        """

        x_position = vent[0][0]
        y_position = vent[0][1]

        self.__modify_dictionary(
            dictionary=dictionary,
            key=str(
                tuple([x_position, y_position])
            )
        )

        while tuple([x_position, y_position]) != vent[1]:
            x_position += 1 if vent[0][0] < vent[1][0] else -1
            y_position += 1 if vent[0][1] < vent[1][1] else -1

            self.__modify_dictionary(
                dictionary=dictionary,
                key=str(
                    tuple([x_position, y_position])
                )
            )

    def __solve_puzzle(self, check_diagonals: bool) -> int:
        """Solve both parts of the Puzzle.

        Args:
            check_diagonals (bool): Count diagonal values based on Puzzle Part

        Returns:
            int: Number of points where two lines overlap

        """

        # Dictionary to save position occurrences
        vents_mapping = dict()

        # For each Ventilation data
        for vent in self.__data:

            # We check if the vent is horizontal
            if vent[0][0] == vent[1][0]:
                self.__process_horizontal_lines(
                    vent=vent,
                    dictionary=vents_mapping
                )

            # Or vertical
            elif vent[0][1] == vent[1][1]:
                self.__process_vertical_lines(
                    vent=vent,
                    dictionary=vents_mapping
                )

            # Or in case of Part 2 diagonal
            else:
                if check_diagonals:
                    self.__process_diagonal_lines(
                        vent=vent,
                        dictionary=vents_mapping
                    )

        return len(list(filter(lambda elem: elem >= 2, vents_mapping.values())))

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            colored('At', 'green'),
            self.__solve_puzzle(check_diagonals=False),
            colored(
                'points at least two (non diagonal) lines overlap.',
                'green'
            )
        )

        print(
            colored('At', 'green'),
            self.__solve_puzzle(check_diagonals=True),
            colored('points at least two lines overlap.', 'green')
        )

    def solve_and_submit_puzzles(self) -> None:
        """Solve both Puzzles and Submit the Solution to the Advent of Code
            Website.

        """

        submit(
            year=self.__year,
            day=self.__day,
            part="a",
            answer=self.__solve_puzzle(check_diagonals=False)
        )
        submit(
            year=self.__year,
            day=self.__day,
            part="b",
            answer=self.__solve_puzzle(check_diagonals=True)
        )
