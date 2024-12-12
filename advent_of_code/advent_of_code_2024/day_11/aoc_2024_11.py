from typing import Dict, List

from aocd.models import Puzzle
from termcolor import colored


class AOC2024D11:

    # HEAVILY INSPIRED BY:
    # https://github.com/matheusstutzel/adventOfCode/blob/main/2024/11/p2.py

    def __init__(self) -> None:
        """Initializes the AOC2024D11 Class."""
        self.year: int = 2024
        self.day: int = 11
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: List[int] = self.__process_puzzle_input()
        self.__number_of_rocks = self.__process_rocks_iteratively(iterations=76)

    def __process_puzzle_input(self) -> List[int]:
        """Processes Puzzle Input.

        Returns:
            List[int]: Processed Puzzle Input.
        """
        return list(map(int, self.__puzzle.input_data.split(' ')))

    def __process_rock(
        self, history: List[Dict[int, int]], rock: int, iteration: int
    ) -> int:
        """Processes rock recursively based on historical data.

        Args:
            history (List[Dict[int, int]]): History of each rock in previous
                iterations.
            rock (int): Currently processed rock.
            iteration (int): Current iteration.

        Returns:
            int: Number of rock generated based on history.
        """
        # If it is the first occurrence of given rock it generates one rock
        if iteration == 0:
            return 1

        # If historical record was found return it
        if rock in history[iteration]:
            return history[iteration][rock]

        # If historical record is not found check how many rocks were generated
        # by the 'modified' rock in the previous iteration(s)
        if rock == 0:
            history[iteration][rock] = self.__process_rock(
                history=history, rock=1, iteration=(iteration - 1)
            )

        elif not len(str(rock)) % 2:
            rock_str = str(rock)
            middle = len(rock_str) // 2

            history[iteration][rock] = self.__process_rock(
                history=history,
                rock=int(rock_str[:middle]),
                iteration=(iteration - 1),
            ) + self.__process_rock(
                history=history,
                rock=int(rock_str[middle:]),
                iteration=(iteration - 1),
            )

        else:
            history[iteration][rock] = self.__process_rock(
                history=history, rock=(rock * 2024), iteration=(iteration - 1)
            )

        return history[iteration][rock]

    def __process_rocks_iteratively(self, iterations: int) -> List[int]:
        """Generates number of rocks for each iteration.

        Args:
            iterations (int): Number of iterations to run (not inclusive).

        Returns:
            List[int]: Number of rocks for each iteration.
        """
        history: List[Dict[int, int]] = [{} for _ in range(iterations)]
        number_of_rocks = []

        for iteration in range(iterations):
            number_of_rocks.append(
                sum(
                    [
                        self.__process_rock(
                            history=history, rock=rock, iteration=iteration
                        )
                        for rock in self.__data
                    ]
                )
            )

        return number_of_rocks

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of rocks after 25 iterations.
        """
        return self.__number_of_rocks[25]

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of rocks after 75 iterations.
        """
        return self.__number_of_rocks[75]

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('Number of rocks after 25 iterations:', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('Number of rocks after 75 iterations:', 'green'),
            self.solve_puzzle_2(),
        )
