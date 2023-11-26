import math
from typing import Tuple

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D09:
    def __init__(self) -> None:
        """Initializes the AOC2022D09 Class."""
        self.year: int = 2022
        self.day: int = 9
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self):
        """Processes Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input.
        """
        return [
            tuple([x[0], int(x[1])])
            for x in list(map(str.split, self.__puzzle.input_data.split('\n')))
        ]

    def __setup_simulation(self, number_of_knots: int) -> None:
        """Sets up simulation variables.

        Args:
            number_of_knots (int): Number of knots in the rope.
        """
        starting_position = (11, 15)
        self.__knots = {}
        for i in range(number_of_knots):
            self.__knots[i] = {
                'current_position': starting_position,
                'visited_positions': [starting_position],
            }

    @staticmethod
    def __calculate_distance(
        head_position: Tuple[int, int], tail_position: Tuple[int, int]
    ) -> float:
        """Calculates the Euclidean distance between two coordinates.

        Args:
            head_position (Tuple[int, int]): Position of the head of the rope
                in the coordinate system.
            tail_position (Tuple[int, int]): Position of the tail of the rope
                in the coordinate system.

        Returns:
            float: Euclidean distance between two coordinates
        """
        return math.sqrt(
            pow(head_position[0] - tail_position[0], 2)
            + pow(head_position[1] - tail_position[1], 2)
        )

    @staticmethod
    def __move_diagonally(
        previous_x: int,
        previous_y: int,
        current_x: int,
        current_y: int,
    ) -> Tuple[int, int]:
        """Calculates new coordinates in a diagonal movement

        Args:
            previous_x (int): Previous knot's column position (x) in the
                coordinate system.
            previous_y (int): Previous knot's row position (y) in the
                coordinate system.
            current_x (int): Current knot's column position (x) in the
                coordinate system.
            current_y (int): Current knot's row position (y) in the coordinate
                system.

        Returns:
            Tuple[int, int]: New coordinates for the current knot.
        """
        # Diagonal movement to the right
        if previous_x > current_x:
            direction_vector_x, direction_vector_y = (
                1,
                1 if previous_y > current_y else -1,
            )

        # Diagonal movement to the left
        else:
            direction_vector_x, direction_vector_y = (
                -1,
                1 if previous_y > current_y else -1,
            )

        return (current_x + direction_vector_x, current_y + direction_vector_y)

    @staticmethod
    def __move_horizontally_or_vertically(
        previous_x: int,
        previous_y: int,
        current_x: int,
        current_y: int,
    ) -> Tuple[int, int]:
        """Calculates new coordinates in a horizontal or vertical movement

        Args:
            previous_x (int): Previous knot's column position (x) in the
                coordinate system.
            previous_y (int): Previous knot's row position (y) in the
                coordinate system.
            current_x (int): Current knot's column position (x) in the
                coordinate system.
            current_y (int): Current knot's row position (y) in the coordinate
                system.

        Returns:
            Tuple[int, int]: New coordinates for the current knot.
        """
        # Horizontal movement
        if previous_y == current_y:
            direction_vector_x, direction_vector_y = (
                1 if previous_x > current_x else -1,
                0,
            )

        # Vertical movement
        elif previous_x == current_x:
            direction_vector_x, direction_vector_y = (
                0,
                1 if previous_y > current_y else -1,
            )

        return (current_x + direction_vector_x, current_y + direction_vector_y)

    def __move_head(self, direction: str) -> None:
        """Moves the head of the rope based on `direction`.

        Args:
            direction (str): Direction of rope head movement.
        """
        x_head, y_head = self.__knots[0]['current_position']

        match direction:
            case 'U':
                new_position = (x_head, y_head - 1)
            case 'D':
                new_position = (x_head, y_head + 1)
            case 'R':
                new_position = (x_head + 1, y_head)
            case 'L':
                new_position = (x_head - 1, y_head)

        self.__knots[0]['current_position'] = new_position

    def __move_subsequent_knots(self, number_of_knots: int) -> None:
        """Moves every knot in the rope after the head based on given rules.

        Args:
            number_of_knots (int): Number of subsequent knots in the rope.
        """
        for i in range(1, number_of_knots):
            previous_knot_position = self.__knots[i - 1]['current_position']
            current_knot_position = self.__knots[i]['current_position']

            previous_x, previous_y = previous_knot_position
            current_x, current_y = current_knot_position

            # Covered or in
            if self.__calculate_distance(
                previous_knot_position, current_knot_position
            ) not in [0.0, 1.0, math.sqrt(2)]:

                # Check if they are in different column
                if (previous_x != current_x) and (previous_y != current_y):
                    new_position = self.__move_diagonally(
                        previous_x=previous_x,
                        previous_y=previous_y,
                        current_x=current_x,
                        current_y=current_y,
                    )

                else:
                    new_position = self.__move_horizontally_or_vertically(
                        previous_x=previous_x,
                        previous_y=previous_y,
                        current_x=current_x,
                        current_y=current_y,
                    )

                self.__knots[i]['current_position'] = new_position
                self.__knots[i]['visited_positions'].append(
                    self.__knots[i]['current_position']
                )

            else:
                return

    def __simulate_rope_movement(self, number_of_knots: int) -> int:
        """Simulates rope movement which has given `number_of_knots` in it.

        At the end of the simulation a number of coordinates which were visited
            by the tail of the rope is calculated.

        Args:
            number_of_knots (int): Number of knots in the rope.

        Returns:
            int: Number of coordinates visited by the tail of the rope.
        """
        self.__setup_simulation(number_of_knots=number_of_knots)

        for direction, length in self.__data:

            for _ in range(length):
                self.__move_head(direction=direction)
                self.__move_subsequent_knots(number_of_knots=number_of_knots)

        return len(set(self.__knots[number_of_knots - 1]['visited_positions']))

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of trees visible from outside the grid.
        """
        return self.__simulate_rope_movement(number_of_knots=2)

    def solve_puzzle_2(self) -> int:
        """Solves the second part of the Puzzle.

        Returns:
            int: Highest scenic score possible for any tree.
        """
        return self.__simulate_rope_movement(number_of_knots=10)

    def solve_and_display_puzzles(self) -> None:
        """Solves both Puzzles and Display the Solution."""
        print(
            self.solve_puzzle_1(),
            colored('trees are visible from outside the grid.', 'green'),
        )

        print(
            colored('Highest scenic score possible for any tree:', 'green'),
            self.solve_puzzle_2(),
        )
