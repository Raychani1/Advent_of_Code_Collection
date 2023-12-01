from typing import Any, Dict, List

from Advent_of_Code_2022.Day_01.aoc_2022_01 import AOC2022D01
from Advent_of_Code_2022.Day_02.aoc_2022_02 import AOC2022D02
from Advent_of_Code_2022.Day_03.aoc_2022_03 import AOC2022D03
from Advent_of_Code_2022.Day_04.aoc_2022_04 import AOC2022D04
from Advent_of_Code_2022.Day_05.aoc_2022_05 import AOC2022D05
from Advent_of_Code_2022.Day_06.aoc_2022_06 import AOC2022D06
from Advent_of_Code_2022.Day_07.aoc_2022_07 import AOC2022D07
from Advent_of_Code_2022.Day_08.aoc_2022_08 import AOC2022D08
from Advent_of_Code_2022.Day_09.aoc_2022_09 import AOC2022D09
from Advent_of_Code_2022.Day_10.aoc_2022_10 import AOC2022D10
from Advent_of_Code_2023.Day_01.aoc_2023_01 import AOC2023D01

AOC_CONFIG: Dict[str, List[Any]] = {
    '2022': [
        AOC2022D01(),
        AOC2022D02(),
        AOC2022D03(),
        AOC2022D04(),
        AOC2022D05(),
        AOC2022D06(),
        AOC2022D07(),
        AOC2022D08(),
        AOC2022D09(),
        AOC2022D10(),
    ],
    '2023': [
        AOC2023D01(),
    ]
}
