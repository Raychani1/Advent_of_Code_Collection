from typing import Dict

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D10:
    def __init__(self) -> None:
        """Initializes the AOC2022D10 Class."""
        self.year: int = 2022
        self.day: int = 10
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()
        self.__register_history = self.__monitor_cpu()

    def __process_puzzle_input(self):
        """Processes Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input.
        """
        return [
            tuple([x[0], int(x[1]), 2]) if len(x) == 2 else tuple([x, 1])
            for x in list(map(str.split, self.__puzzle.input_data.split('\n')))
        ]

    def __monitor_cpu(self) -> Dict[int, int]:
        """Monitors 240 cycles (the amount of cycles needed for a 6x40 CRT
        display visualization) and saves register value to history.

        Returns:
            Dict[int, int]: Register history for 240 cycles.
        """
        x = 1
        current_cycle = 1
        register_history = {x: current_cycle}

        # Calculate register changes
        while current_cycle < 240:
            operation = self.__data.pop(0)

            if len(operation) == 2:
                current_cycle += operation[1]
            else:
                # The 'addx' operation needs 2 cycles to execute, so we drag
                # the current value to the following cycle, and update the
                # register after it.
                register_history[current_cycle + 1] = x
                current_cycle += operation[2]
                x += operation[1]

            register_history[current_cycle] = x

        return register_history

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of trees visible from outside the grid.
        """
        check_cycles = [20, 60, 100, 140, 180, 220]

        signal_strengths = sum(
            [cycle * self.__register_history[cycle] for cycle in check_cycles]
        )

        return signal_strengths

    def solve_puzzle_2(self) -> str:
        """Solves the second part of the Puzzle.

        Returns:
            str: Eight capital letters displayed on the CRT display.
        """
        current_cycle = 1

        for _ in range(6):
            for col in range(40):
                x = self.__register_history[current_cycle]
                active_range = range(x - 1, x + 2)
                current_cycle += 1

                if col in active_range:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

        return input(
            colored(
                'The eight capital letters that appear on your CRT are: ',
                'green',
            )
        )

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            self.solve_puzzle_1(),
            colored('is the sum of these six signal strengths.', 'green'),
        )

        self.solve_puzzle_2()
