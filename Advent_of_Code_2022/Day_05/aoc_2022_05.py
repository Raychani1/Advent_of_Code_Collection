import re
from itertools import chain
from operator import methodcaller
from typing import Dict, List, Union

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D05:

    def __init__(self) -> None:
        """Initialize the AOC2022D05 Class."""
        self.year: int = 2022
        self.day: int = 5
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data: Dict[str, Union[Dict[str, List[str]], List[List[str]]]] = (
            self.__process_puzzle_input()
        )

    def __process_cargo(self) -> Dict[str, List[str]]:
        """Process Cargo Crates.

        Returns:
			Dict[str, List[str]]: Processed Cargo Crates.
        """
        cargo_warehouse: Dict[str, List[str]] = {}

        for line in self.__puzzle.input_data.split('\n\n')[0].split('\n')[:-1]:
            # Replace Cargo Crates with quotation marks and find their content
            for i, cargo in enumerate(
				re.findall(
					r'"(.*?)"',
					''.join(
						[
							'"' if i in range(0, len(line), 2)
							else line[i] for i in range(len(line))
						]
					)
				)
            ):
                stack: str = str(i+1)

                if stack not in cargo_warehouse.keys():
                    cargo_warehouse[stack] = []

                if cargo != ' ':
                    cargo_warehouse[stack].append(cargo)

        return cargo_warehouse

    def __process_movements(self) -> List[List[str]]:
        """Process Movement Data.

        Returns:
			List[List[str]]: Processed Movement Data.
        """
        movements: List[List[str]] = []

        for line in list(
			chain.from_iterable(
				list(
					map(
						methodcaller("split", "\n"),
						self.__puzzle.input_data.split('\n\n')[1:]
					)
				)
			)
        ):
            movements.append(re.findall(r'\d+', line))

        return movements

    def __process_puzzle_input(
		self
    ) -> Dict[str, Union[Dict[str, List[str]], List[List[str]]]]:
        """Process Puzzle Input.

        Returns:
			Dict[str, Union[Dict[str, List[str]], List[List[str]]]]: Processed 
			Puzzle Input.
        """
        return {
            'cargo': self.__process_cargo(),
            'movements': self.__process_movements()
        }

    def __move_crates(self, reverse: bool) -> str:
        """Move creates in cargo.

        Args:
			reverse (bool): Reverse moved crates.

        Returns:
			str: Top crates.
        """
        cargo = self.__data['cargo'].copy()

        for movement in self.__data['movements']:
            amount, from_stack, to_stack = tuple(movement)

            # Select Elements from stack
            elements = cargo[from_stack][:int(amount)]

            # Reverse if not using CrateMover 9001 (Part Two)
            if reverse:
                elements = elements[::-1]

            # Remove elements from stack
            cargo[from_stack] = cargo[from_stack][int(amount):]

            # Add crates to destination
            cargo[to_stack] = list(
                chain.from_iterable([elements, cargo[to_stack]])
            )

        # Get top crate names
        return ''.join([cargo[stack][0] for stack in sorted(cargo.keys())])

    def solve_puzzle_1(self) -> int:
        """Solve the first part of the Puzzle.

        Returns:
			str: Top Crates while moving crates one by one.
        """
        return self.__move_crates(reverse=True)

    def solve_puzzle_2(self) -> str:
        """Solve the second part of the Puzzle.

        Returns:
			str: Top Crates while moving many crates at once.
        """
        return self.__move_crates(reverse=False)

    def solve_and_display_puzzles(self) -> None:
        """Solve both Puzzles and Display the Solution."""
        print(
            colored(
                'Top Crates while moving crates one by one:',
                'green'
            ),
            self.solve_puzzle_1(),
        )

        print(
            colored(
                'Top Crates while moving many crates at once:',
                'green'
            ),
            self.solve_puzzle_2(),
        )
