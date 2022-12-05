from operator import methodcaller
from typing import List

from aocd.models import Puzzle
from termcolor import colored


class AOC2022D04:

	def __init__(self) -> None:
		"""Initialize the AOC2022D04 Class."""
		self.year: int = 2022
		self.day: int = 4
		self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
		self.__data: List[List[List[int]]] = self.__process_puzzle_input()

	def __process_puzzle_input(self) -> List[List[List[int]]]:
		"""Process Puzzle Input.

		Returns:
			List[List[List[int]]]: Processed Puzzle Input.
		"""
		return [
			[list(map(int, j)) for j in i] for i in [
				list(
					map(
						methodcaller("split", "-"),
						ranges
					)
				) for ranges in list(
					map(
						methodcaller("split", ","),
						self.__puzzle.input_data.split()
					)
				)
			]
		]

	@staticmethod
	def __range_overlap(
			range_data: List[List[int]],
			full_overlap: bool = True
	) -> bool:
		"""Check for range overlap.

		Args:
			range_data (List[List[int]]): Ranges to check for overlaps.
			full_overlap (bool, optional): Find full overlaps. Defaults to 
			True.

		Returns:
			bool: Overlap found.
		"""
		range1, range2 = tuple([set(range(r[0], r[1]+1)) for r in range_data])

		return (
			len(set.intersection(range1, range2)) in [len(range1), len(range2)]
			if full_overlap else len(set.intersection(range1, range2)) != 0
		)

	def solve_puzzle_1(self) -> int:
		"""Solve the first part of the Puzzle.

		Returns:
			int: Number of full overlaps in assignment pairs.
		"""
		return sum(list(map(self.__range_overlap, self.__data)))

	def solve_puzzle_2(self) -> int:
		"""Solve the second part of the Puzzle.

		Returns:
			int:  Number of partial overlaps in assignment pairs.
		"""
		return sum(
			[
				self.__range_overlap(range_data=r, full_overlap=False)
				for r in self.__data
			]
		)

	def solve_and_display_puzzles(self) -> None:
		"""Solve both Puzzles and Display the Solution."""
		print(
			colored(
				'Found full overlap in',
				'green'
			),
			self.solve_puzzle_1(),
			colored(
				'assignment pairs.',
				'green'
			),
		)

		print(
			colored(
				'Found partial overlap in',
				'green'
			),
			self.solve_puzzle_2(),
						colored(
				'assignment pairs.',
				'green'
			),
		)
