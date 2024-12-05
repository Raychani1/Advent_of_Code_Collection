from typing import Any, Dict, List

from advent_of_code.advent_of_code_2024.day_01.aoc_2024_01 import AOC2024D01
from advent_of_code.advent_of_code_2024.day_02.aoc_2024_02 import AOC2024D02
from advent_of_code.advent_of_code_2024.day_03.aoc_2024_03 import AOC2024D03
from advent_of_code.advent_of_code_2024.day_04.aoc_2024_04 import AOC2024D04
from advent_of_code.advent_of_code_2024.day_05.aoc_2024_05 import AOC2024D05

AOC_CONFIG: Dict[str, List[Any]] = {
    '2024': [
        AOC2024D01(),
        AOC2024D02(),
        AOC2024D03(),
        AOC2024D04(),
        AOC2024D05(),
    ]
}
