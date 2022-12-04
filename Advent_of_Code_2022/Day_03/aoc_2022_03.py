from typing import List

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D03:

	def __init__(self) -> None:
		"""Initialize the AOC2022D03 Class."""
		self.year: int = 2022
		self.day: int = 3
		self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
		self.__data: List[str] = self.__process_puzzle_input()

	def __process_puzzle_input(self) -> List[str]:
		"""Process Puzzle Input.

		Returns:
			List[str]: Processed Puzzle Input.
		"""
		return self.__puzzle.input_data.split()

	@staticmethod
	def __split_in_half(rucksack: str) -> List[str]:
		"""Split string in half.

		Args:
			rucksack (str): Rucksack string.

		Returns:
			List[str]: String split in half.
		"""
		middle_index: int = round(len(rucksack) / 2)

		return [rucksack[:middle_index], rucksack[middle_index:]]

	@staticmethod
	def __calculate_priorities(rucksack: List[str]) -> int:
		"""Calculate common item priorities.

		Args:
			rucksack (List[str]): Rucksack strings.

		Returns:
			int: Rucksack priority.
		"""
		common_item: str = next(
			iter(set.intersection(*list(map(set, rucksack))))
		)

		return (
			((ord(common_item) - ord('a')) + 1) if common_item.islower()
			else ((ord(common_item) - ord('A')) + 27)
		)

	def solve_puzzle_1(self) -> int:
		"""Solve the first part of the Puzzle.

		Returns:
			int: Sum of common item priorities in rucksack compartments.
		"""
		return sum(
			[
				self.__calculate_priorities(rucksack) for rucksack in list(
					map(self.__split_in_half, self.__data)
				)
			]
		)

	def solve_puzzle_2(self) -> int:
		"""Solve the second part of the Puzzle.

		Returns:
			int:  Sum of common item priorities in rucksack groups.
		"""
		return sum(
			[
				self.__calculate_priorities(self.__data[i:i+3])
				for i in range(0, len(self.__data) - 2, 3)
			]
		)

	def solve_and_display_puzzles(self) -> None:
		"""Solve both Puzzles and Display the Solution."""
		print(
			colored(
				'Sum of common item priorities in rucksack compartments:',
				'green'
			),
			self.solve_puzzle_1(),
		)

		print(
			colored(
				'Sum of common item priorities in rucksack groups:',
				'green'
			),
			self.solve_puzzle_2(),
		)
