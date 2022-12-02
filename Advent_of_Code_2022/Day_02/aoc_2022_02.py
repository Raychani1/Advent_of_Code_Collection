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
		self.__win_draw_lose_mapping: Dict[str, Dict[str, str]] = {
			'win': {
				'A': 'Y',
				'B': 'Z',
				'C': 'X',
			},
			'draw': {
				'A': 'X',
				'B': 'Y',
				'C': 'Z',
			},
			'lose': {
				'A': 'Z',
				'B': 'X',
				'C': 'Y',
			},

		}
		self.__points_mapping: Dict[str, int] = {
			'win': 6,
			'draw': 3,
			'lose': 0,
		}

	def __process_puzzle_input(self) -> List[List[str]]:
		"""Process Puzzle Input.

		Returns:
			List[List[str]]: Processed Puzzle Input.
		"""
		return list(map(str.split, self.__puzzle.input_data.split('\n')))

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
		points: int = 0

		opponent, me = tuple(round)

		if win_condition:
			match(me):
				case 'X':
					me = self.__win_draw_lose_mapping['lose'][opponent]
				case 'Y':
					me = self.__win_draw_lose_mapping['draw'][opponent]
				case 'Z':
					me = self.__win_draw_lose_mapping['win'][opponent]

		choice_points: int = ((ord(me) - ord('X')) + 1)

		if (opponent, me) in list(
			self.__win_draw_lose_mapping['win'].items()
		):
			points = self.__points_mapping['win'] + choice_points

		elif (opponent, me) in list(
			self.__win_draw_lose_mapping['draw'].items()
		):
			points = self.__points_mapping['draw'] + choice_points

		else:
			points = self.__points_mapping['lose'] + choice_points

		return points

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
