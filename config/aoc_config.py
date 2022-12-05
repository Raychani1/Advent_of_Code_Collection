from typing import Any, Dict, List

from Advent_of_Code_2022.Day_01.aoc_2022_01 import AOC2022D01
from Advent_of_Code_2022.Day_02.aoc_2022_02 import AOC2022D02
from Advent_of_Code_2022.Day_03.aoc_2022_03 import AOC2022D03
from Advent_of_Code_2022.Day_04.aoc_2022_04 import AOC2022D04
from Advent_of_Code_2022.Day_05.aoc_2022_05 import AOC2022D05


AOC_CONFIG: Dict[str, List[Any]] = {
    '2022': [
        AOC2022D01(),
        AOC2022D02(),
        AOC2022D03(),
        AOC2022D04(),
        AOC2022D05(),
    ]
}