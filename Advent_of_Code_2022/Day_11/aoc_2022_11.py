import math
import os
import sys
from pprint import pprint

import numpy as np
from aocd.models import Puzzle
from termcolor import colored

sys.set_int_max_str_digits(1000000)

class AOC2022D11:
    def __init__(self) -> None:
        """Initializes the AOC2022D11 Class."""
        self.year: int = 2022
        self.day: int = 11
        self.__puzzle: Puzzle = Puzzle(year=self.year, day=self.day)
        self.__data = self.__process_puzzle_input()

    def __process_puzzle_input(self):
        """Processes Puzzle Input.

        Returns:
            List[List[int]]: Processed Puzzle Input.
        """
        monkey_data = {}

        # with open(
        #     os.path.join(
        #         os.getcwd(), 'Advent_of_Code_2022', 'Day_11', 'input_data.txt'
        #     )
        # ) as input_file:
        #     data = ''.join(input_file.readlines()).split('\n\n')

        #     for monkey in data:
        #         lines = monkey.split('\n')

        #         monkey_id = int(lines[0].split()[1][:-1])
        #         starting_items = list(
        #             map(int, lines[1].split(':')[-1].strip().split(', '))
        #         )
        #         operation = lines[2].split('=')[-1].strip()
        #         divisible_by = int(lines[3].split(' ')[-1])
        #         true_monkey_id = int(lines[4].split(' ')[-1])
        #         false_monkey_id = int(lines[5].split(' ')[-1])
                
        #         monkey_data[monkey_id] = {
        #             'items': starting_items,
        #             'operation': operation,
        #             'test': divisible_by,
        #             'true_monkey_id': true_monkey_id,
        #             'false_monkey_id': false_monkey_id,
        #             'number_of_inspected_items': 0
        #         }

        # return monkey_data


        data = ''.join(self.__puzzle.input_data).split('\n\n')

        for monkey in data:
            lines = monkey.split('\n')

            monkey_id = int(lines[0].split()[1][:-1])
            starting_items = list(
                map(int, lines[1].split(':')[-1].strip().split(', '))
            )
            operation = lines[2].split('=')[-1].strip()
            divisible_by = int(lines[3].split(' ')[-1])
            true_monkey_id = int(lines[4].split(' ')[-1])
            false_monkey_id = int(lines[5].split(' ')[-1])
            
            monkey_data[monkey_id] = {
                'items': starting_items,
                'operation': operation,
                'test': divisible_by,
                'true_monkey_id': true_monkey_id,
                'false_monkey_id': false_monkey_id,
                'number_of_inspected_items': 0
            }

        return monkey_data

    def solve_puzzle_1(self) -> int:
        """Solves the first part of the Puzzle.

        Returns:
            int: Number of trees visible from outside the grid.
        """
        order_of_monkeys = sorted(list(self.__data.keys()))
        number_of_rounds = 20

        for _ in range(number_of_rounds):
            for monkey_id in order_of_monkeys:
                current_monkey = self.__data[monkey_id]

                for old in current_monkey['items']:
                    new_value = math.floor(eval(current_monkey['operation']) / 3)
                    # .replace('old', str(item))

                    self.__data[
                        current_monkey[
                            'true_monkey_id' if new_value % current_monkey['test'] == 0 else 'false_monkey_id'
                        ]
                    ]['items'].append(new_value)

                    current_monkey['number_of_inspected_items'] += 1
                    
                current_monkey['items'] = []

        most_items_inspected = sorted([v['number_of_inspected_items'] for _, v in self.__data.items()])[-2:]

        return np.prod(most_items_inspected)

    def solve_puzzle_2(self) -> str:
        """Solves the second part of the Puzzle.

        Returns:
            str: Eight capital letters displayed on the CRT display.
        """
        order_of_monkeys = sorted(list(self.__data.keys()))
        number_of_rounds = 10000

        for i in range(number_of_rounds):
            print(f'Round: {i}')
            for monkey_id in order_of_monkeys:
                current_monkey = self.__data[monkey_id]

                for old in current_monkey['items']:
                    new_value = eval(current_monkey['operation'])

                    self.__data[
                        current_monkey[
                            'true_monkey_id' if new_value % current_monkey['test'] == 0 else 'false_monkey_id'
                        ]
                    ]['items'].append(new_value)

                    current_monkey['number_of_inspected_items'] += 1
                    
                current_monkey['items'] = []

        most_items_inspected = sorted([v['number_of_inspected_items'] for _, v in self.__data.items()])[-2:]

        return np.prod(most_items_inspected)

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

