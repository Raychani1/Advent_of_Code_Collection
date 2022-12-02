from typing import Any, Dict, List, Tuple, Union

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D02:

    def __init__(self) -> None:
        """Initialize the AOC2022D02 Class."""
        self.year: int = 2022
        self.day: int = 2
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: List[List[str]] = self.__process_puzzle_input()

        # Helping Variables
        self.__win_draw_lose_mapping: Dict[str, Dict[str, Union[str, int]]] = {
            'win': {
                'A': 'Y',
                'B': 'Z',
                'C': 'X',
                'point': 6
            },
            'draw': {
                'A': 'X',
                'B': 'Y',
                'C': 'Z',
                'point': 3
            },
            'lose': {
                'A': 'Z',
                'B': 'X',
                'C': 'Y',
                'point': 0
            },
        }

    def __process_puzzle_input(self) -> List[List[str]]:
        """Process Puzzle Input.

        Returns:
            List[List[str]]: Processed Puzzle Input.
        """
        return list(map(str.split, self.__puzzle.input_data.split('\n')))

    def __update_values(self, scenario: str, opponent: str) -> Tuple[Any, Any]:
        """Update variable values.

        Returns:
            Tuple[Any, Any]: New variable values.
        """
        return (
            self.__win_draw_lose_mapping[scenario]['point'], 
            self.__win_draw_lose_mapping[scenario][opponent]
        )

    def __play_rock_paper_scissors(
        self,
        round: List[str],
        win_condition: bool = False
    ) -> int:
        """Calculate results of Rock Paper Scissors round.

        Args:
            round (List[str]): Rock Paper Scissors round.
            win_condition (bool, optional): Use Elf's instructions. Defaults to
            False.

        Returns:
            int: Results of Rock Paper Scissors round
        """
        win_draw_lose_points = 0
        my_choice_points = 0

        opponent, me = tuple(round)

        if win_condition:
            match(me):
                case 'X':
                    win_draw_lose_points, me = self.__update_values(
                        scenario='lose', 
                        opponent=opponent
                    )
                case 'Y':
                    win_draw_lose_points, me = self.__update_values(
                        scenario='draw', 
                        opponent=opponent
                    )
                case 'Z':
                    win_draw_lose_points, me = self.__update_values(
                        scenario='win', 
                        opponent=opponent
                    )
        else:
            if (opponent, me) in list(
                self.__win_draw_lose_mapping['win'].items()
            ):
                win_draw_lose_points = (
                    self.__win_draw_lose_mapping['win']['point']
                )
            elif (opponent, me) in list(
                self.__win_draw_lose_mapping['draw'].items()
            ):
                win_draw_lose_points = (
                    self.__win_draw_lose_mapping['draw']['point']
                )

        match(me):
            case 'X': my_choice_points = 1
            case 'Y': my_choice_points = 2
            case 'Z': my_choice_points = 3

        return (int(win_draw_lose_points) + my_choice_points)

    def solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
            int: My total score based on strategy guide.
        """
        return sum(list(map(self.__play_rock_paper_scissors, self.__data)))

    def solve_puzzle_2(self) -> int:
        """Solve the second part of the Puzzle.

        Returns:
            int: My total score based on Elf's instructions and strategy guide.
        """
        return sum(
            [
                self.__play_rock_paper_scissors(
                    round=r,
                    win_condition=True
                ) for r in self.__data
            ]
        )

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""
        print(
            colored(
                'My total score based on strategy guide:',
                'green'
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                "My total score based on Elf's instructions and strategy guide:",
                'green'
            ),
            self.solve_puzzle_2(),
        )
