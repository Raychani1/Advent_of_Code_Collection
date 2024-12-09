from typing import Set, Tuple, TypedDict


class Guard(TypedDict):
    direction: str
    current_coordinate: Tuple[int, int]
    visited_coordinates: Set[Tuple[int, int]]
