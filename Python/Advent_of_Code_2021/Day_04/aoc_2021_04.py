import numpy
from aocd import submit
from termcolor import colored
from aocd.models import Puzzle
from collections import Counter
from typing import List, Union, Dict, Tuple


class AOC2021D04:

    def __init__(self) -> None:
        """Initialize the AOC2021D04 Class."""

        self.__year: int = 2021
        self.__day: int = 4
        self.__puzzle: Puzzle = Puzzle(year=self.__year, day=self.__day)
        self.__data: Dict[str, Union[List[int], List[List[List[int]]]]] = \
            self.__process_puzzle_input()

    def __process_puzzle_input(self) -> \
            Dict[str, Union[List[int], List[List[List[int]]]]]:
        """Process Puzzle Input.

        Returns:
            Dict[str, Union[List[int], List[List[List[int]]]]]: Processed Puzzle
                Input

        """

        # Get all the numbers
        numbers: List[int] = list(
            map(int, self.__puzzle.input_data.split('\n')[0].split(','))
        )

        # Select Boards
        boards = [x.split('\n') for x in
                  self.__puzzle.input_data.split('\n\n')[1:]]

        # Convert Boards to 2D integer Lists
        for index, element in enumerate(boards):
            boards[index] = [
                list(map(int, i)) for i in list(
                    map(
                        lambda x: x.split(' '),
                        list(
                            map(
                                lambda x: ' '.join(x.split()),
                                element
                            )
                        )
                    )
                )
            ]

        return {'numbers': numbers, 'boards': boards}

    @staticmethod
    def __contains(container: Counter, contained: Counter) -> bool:
        """Check if Small Counter Object (contained) is in Bigger Counter Object
            (container).

        Args:
            container (Counter): Bigger Counter Object
            contained (Counter): Smaller Counter Object

        Returns:
            bool: Bigger Counter Object contains Smaller Counter Object

        """

        return all(container[x] >= contained[x] for x in contained)

    def __search_for_win(
            self,
            selected_numbers: List[int],
            board: List[List[int]]
    ) -> Tuple[bool, int]:
        """Check for winning condition on board based on selected numbers.

        Args:
            selected_numbers (List[int]): Selected Numbers
            board (List[List[int]]): Bingo Board

        Returns:
            Tuple[bool, int]: Winning condition satisfied and sum of unchecked
                numbers

        """

        # Iterate through every row of board
        for index, row in enumerate(board):

            # Grab the column based on index
            column: List[int] = [x[index] for x in board]

            # Count elements in Selected Numbers
            selected_numbers_counter: Counter = Counter(selected_numbers)

            # Count elements in Row
            row_counter: Counter = Counter(row)

            # Count elements in Column
            column_counter: Counter = Counter(column)

            # If the Smaller Counter Object (row_counter/column_counter) is part
            # of the Bigger Counter Object (selected_numbers_counter) that means
            # that the given row or column is checked, so that is a winning
            # board
            if self.__contains(
                    container=selected_numbers_counter,
                    contained=row_counter
            ) or self.__contains(
                container=selected_numbers_counter,
                contained=column_counter
            ):
                return True, sum(
                    [x for x in list(numpy.concatenate(board).flat) if
                     x not in selected_numbers]
                )

        return False, 0

    def __solve_puzzle(self, last_win: bool) -> int:
        """Solve the first part of the Puzzle.

        Args:
            last_win (bool): Result selection

        Returns:
            int: The Final Score of the First or Last Winning Board based on
                argument

        """

        # Create a copy of all boards - not to modify the original List while
        # removing elements
        boards_copy = self.__data['boards'].copy()

        # List to save scores
        win_results: List[int] = []

        # Go through all the numbers, starting with first 5
        for position in range(5, len(self.__data['numbers'].copy())):

            selected_numbers: List[int] = self.__data['numbers'][:position]

            # Check selected numbers for all boards
            for index, board in enumerate(boards_copy):

                # Check winning condition
                result: Tuple[bool, int] = self.__search_for_win(
                    selected_numbers=selected_numbers,
                    board=board
                )

                # Save the scores and remove the winning table
                if result[0]:
                    win_results.append(result[1] * selected_numbers[-1])
                    boards_copy.pop(index)

                    # If we are looking for the first win we can exit the
                    # function earlier
                    if not last_win:
                        return win_results[last_win * -1]

        # Return value based on first (last_win=False) or last (last_win=True)
        # win
        return win_results[last_win * -1]

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""

        print(
            colored(
                'The Final Score of the First Winning Board: ',
                'green'
            ),
            self.__solve_puzzle(last_win=False)
        )

        print(
            colored(
                'The Final Score of the Last Winning Board: ',
                'green'
            ),
            self.__solve_puzzle(last_win=True)
        )

    def solve_and_submit_puzzles(self) -> None:
        """Solve both Puzzles and Submit the Solution to the Advent of Code
            Website.

        """

        submit(
            year=self.__year,
            day=self.__day,
            part="a",
            answer=self.__solve_puzzle(last_win=False)
        )
        submit(
            year=self.__year,
            day=self.__day,
            part="b",
            answer=self.__solve_puzzle(last_win=True)
        )
