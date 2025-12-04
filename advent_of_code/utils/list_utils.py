
from itertools import product
from typing import Any, List, Union


def chunks_of_size(values: Union[str, List[Any]], chunk_size: int) -> List[Any]:
    """Chunks `values` to `chunk_sized` chunks.

    Args:
        values (Union[str, List[Any]]): List of values / string to chunk.
        chunk_size (int): Chunk size.

    Returns:
        List[Any]: Chunked values.
    """
    return [values[i:i+chunk_size] for i in range(0, len(values), chunk_size)]


def get_2d_neighbor_elements(
    data: List[List[Any]], current_row: int, current_col: int
) -> List[Any]:
    """Gets neighbor elements for `current_row`;`current_col` position in a 2D
    List.

    Args:
        data (List[List[Any]]): List to process.
        current_row (int): Current row index.
        current_col (int): Current column index.

    Returns:
        List[Any]: Neighbor elements around `current_row`;`current_col`.
    """
    neighbors = []
    max_rows = len(data)
    deltas = (-1, 0, 1)

    # Generate combination of delta with itself
    for row_delta, col_delta in product(deltas, repeat=2):

        # Skip the middle element
        if row_delta == 0 and col_delta == 0:
            continue

        new_row = current_row + row_delta
        new_col = current_col + col_delta

        # Add only in-bound elements
        if 0 <= new_row < max_rows and 0 <= new_col < len(data[new_row]):
            neighbors.append(data[new_row][new_col])

    return neighbors
