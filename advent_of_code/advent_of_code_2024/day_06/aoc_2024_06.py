import copy
import itertools
from typing import Any, List, Tuple

from aocd.models import Puzzle
from termcolor import colored

from advent_of_code.advent_of_code_2024.day_06.structures.guard import Guard


class AOC2024D06:
    def __init__(self) -> None:
        """Initializes the AOC2024D06 Class."""
        self.year: int = 2024
        self.day: int = 6
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__layout, self.__guard = self.__process_puzzle_input()

    def __process_puzzle_input(
        self,
    ) -> Tuple[List[List[Any]], Guard]:
        """Processes Puzzle Input.

        Returns:
            Tuple[List[List[Any]], Guard]: Processed Puzzle Input.
        """
        layout = list(
            map(list, self.__puzzle.examples[0].input_data.split('\n'))
        )

        guard: Guard = {
            'direction': 'N',
            'current_coordinate': (-1, -1),
            'visited_coordinates': set(),
        }

        for i, j in itertools.product(
            range(len(layout)), range(len(layout[0]))
        ):
            if layout[i][j] == '^':
                guard['current_coordinate'] = (i, j)
                guard['visited_coordinates'] = {(i, j)}

        return layout, guard

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: TODO
        """
        guard: Guard = copy.deepcopy(self.__guard)

        next_position: Tuple[int, int] = guard['current_coordinate']

        while (0 <= next_position[0] < len(self.__layout)) and (
            0 <= next_position[1] < len(self.__layout[0])
        ):
            if self.__layout[next_position[0]][next_position[1]] == '#':
                match guard['direction']:
                    case 'N':
                        guard['direction'] = 'E'
                    case 'E':
                        guard['direction'] = 'S'
                    case 'S':
                        guard['direction'] = 'W'
                    case 'W':
                        guard['direction'] = 'N'
            else:
                guard['current_coordinate'] = next_position
                guard['visited_coordinates'].add(next_position)

            match guard['direction']:
                case 'N':
                    next_position = (
                        guard['current_coordinate'][0] - 1,
                        guard['current_coordinate'][1],
                    )
                case 'E':
                    next_position = (
                        guard['current_coordinate'][0],
                        guard['current_coordinate'][1] + 1,
                    )
                case 'S':
                    next_position = (
                        guard['current_coordinate'][0] + 1,
                        guard['current_coordinate'][1],
                    )
                case 'W':
                    next_position = (
                        guard['current_coordinate'][0],
                        guard['current_coordinate'][1] - 1,
                    )

        return len(guard['visited_coordinates'])

    def solve_puzzle_2(self) -> Any:
        """Solves the second part of the Puzzle.

        Returns:
            Any: TODO
        """
        pass

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            colored('TODO', 'green'),
            self.solve_puzzle_1(),
        )

        print(
            colored('TODO', 'green'),
            self.solve_puzzle_2(),
        )
