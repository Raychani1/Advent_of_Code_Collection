from aocd.models import Puzzle
from termcolor import colored


class AOC2022D06:

    def __init__(self) -> None:
        """Initialize the AOC2022D06 Class."""
        self.year: int = 2022
        self.day: int = 6
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: str = self.__puzzle.input_data

    def __check_for_unique_signals(self, number_of_unique_signals: int) -> int:
        """Check for first occurrence of unique signals following each other.

        Args:
            number_of_unique_signals (int): Minimum length of consecutive 
            signals.

        Returns:
            int: Index of last unique signal, the start-of-* marker.
        """
        for i in range(len(self.__data)):
            if (
                len(
                    set(self.__data[i:i+number_of_unique_signals])
                ) == number_of_unique_signals
            ):
                return (i+number_of_unique_signals)

    def solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: Number of characters need to be processed before the first 
            start-of-packet marker is detected.
        """
        return self.__check_for_unique_signals(number_of_unique_signals=4)

    def solve_puzzle_2(self) -> str:
        """Solve the second part of the Puzzle.

        Returns:
            int: Number of characters need to be processed before the first 
            start-of-message marker is detected.
        """
        return self.__check_for_unique_signals(number_of_unique_signals=14)

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""
        print(
            self.solve_puzzle_1(),
            colored(
                (
                    'characters need to be processed before the first' 
                    'start-of-packet marker is detected.'
                ),
                'green'
            ),
        )
        
        print(
            self.solve_puzzle_2(),
             colored(
                (
                    'characters need to be processed before the first' 
                    'start-of-message marker is detected.'
                ),
                'green'
            ),
        )
