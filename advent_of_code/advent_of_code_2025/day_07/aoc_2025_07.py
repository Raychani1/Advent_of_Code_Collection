import copy
from typing import List

from aocd.models import Puzzle
from termcolor import colored


class AOC2025D07:

    def __init__(self) -> None:
        """Initializes the AOC2025D07 Class."""
        self.year: int = 2025
        self.day: int = 7
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self) -> List[List[str]]:
        """Processes Puzzle Input.

        Returns:
            List[List[str]]: Processed Puzzle Input.
        """
        return [list(row) for row in self.__puzzle.input_data.split('\n')]

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of times the beam will be split.
        """
        current_beam_positions = {self.__data[0].index('S')}
        split_counter = 0

        for index in range(1, len(self.__data) - 1):
            next_stage_beam_positions = set()
            
            current_stage_beam_positions = copy.deepcopy(current_beam_positions)

            for position in current_stage_beam_positions:
                if self.__data[index + 1][position] == '^':
                    split_counter += 1
                    current_beam_positions.remove(position)
                    next_stage_beam_positions.update(
                        {position - 1, position + 1}
                    )
                else:
                    next_stage_beam_positions.add(position)
        
            current_beam_positions = next_stage_beam_positions

        return split_counter

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Number of different timelines a single tachyon particle would 
                end up on.
        """
        timeline_counter = {self.__data[0].index('S'): 1}

        for index in range(1, len(self.__data) - 1):
            timeline_counter_next_stage = {}

            for position, value in timeline_counter.items():
                new_positions = (
                    [position - 1, position + 1]
                    if self.__data[index + 1][position] == '^' else 
                    [position]
                )

                for new_position in new_positions:
                    if new_position not in timeline_counter_next_stage:
                        timeline_counter_next_stage[new_position] = value
                    else:
                        timeline_counter_next_stage[new_position] += value

            timeline_counter = timeline_counter_next_stage

        return sum(timeline_counter.values())

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('The beam will be split', 'green'),
            self.solve_puzzle_1(),
            colored('times.', 'green'),
        )

        print(
            colored('A single tachyon particle would end up on', 'green'),
            self.solve_puzzle_2(),
            colored('different timelines.', 'green'),
        )
