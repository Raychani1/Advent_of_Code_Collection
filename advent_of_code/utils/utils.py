from typing import Any, Dict, List


def filter_dictionary(
    dictionary: Dict[Any, Any], callback: Any
) -> Dict[Any, Any]:
    """Filter Dictionary based on callback condition.

    Args:
        dictionary (Dict[Any, Any]): Dictionary to filer.
        callback (Any): Filtering callback.

    Returns:
        Dict[Any, Any]: Filtered dictionary.
    """
    filtered_dict = dict()

    for (key, value) in dictionary.items():

        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            filtered_dict[key] = value

    return filtered_dict


def get_diagonal_starting(
    matrix: List[Any],
    start_row: int,
    start_col: int,
    num_elements: int,
    direction: str = 'main',
) -> List[Any]:
    """Fetches `num_elements` from a `matrix` diagonally starting from
    `start_row` and `start_col`.

    Args:
        matrix (List[Any]): Matrix to select elements from.
        start_row (int): Starting row index.
        start_col (int): Starting column index.
        num_elements (int): Number of elements to select.
        direction (str): Direction of the diagonal. Supported values:
            ['main', 'anti']. Defaults to 'main'.

    Raises:
        ValueError: If an unsupported direction is selected.

    Returns:
        List[Any]: Diagonally selected elements in a single list.
    """
    diagonal = []
    rows, cols = len(matrix), len(matrix[0])

    for _ in range(num_elements):

        # Add elements if within bounds
        if 0 <= start_row < rows and 0 <= start_col < cols:
            diagonal.append(matrix[start_row][start_col])

        # Move diagonally down-right
        if direction == 'main':
            start_row += 1
            start_col += 1

        # Move diagonally down-left
        elif direction == 'anti':
            start_row += 1
            start_col -= 1

        else:
            raise ValueError("Invalid direction. Use 'main' or 'anti'.")

    return diagonal


def get_diagonal_centered(
    matrix: List[Any],
    center_row: int,
    center_col: int,
    num_elements: int,
    direction: str = 'main',
) -> List[Any]:
    """Fetches `num_elements` from a `matrix` diagonally centered around
    `center_row` and `center_col`.

    Args:
        matrix (List[Any]): Matrix to select elements from.
        center_row (int): Center element row index.
        center_col (int): Center element column index.
        num_elements (int): Number of elements to select.
        direction (str): Direction of the diagonal. Supported values:
            ['main', 'anti']. Defaults to 'main'.

    Raises:
        ValueError: If an unsupported direction is selected.

    Returns:
        List[Any]: Diagonally selected elements in a single list.
    """
    diagonal = []
    rows, cols = len(matrix), len(matrix[0])
    half = num_elements // 2  # Half of the desired elements for symmetry

    for step in range(-half, half + 1):

        # Move diagonally up-left (negative step) and down-right (positive step)
        if direction == 'main':
            row, col = center_row + step, center_col + step

        # Move diagonally up-right (negative step) and down-left (positive step)
        elif direction == 'anti':
            row, col = center_row + step, center_col - step

        else:
            raise ValueError("Invalid direction. Use 'main' or 'anti'.")

        # Add elements if within bounds
        if 0 <= row < rows and 0 <= col < cols:
            diagonal.append(matrix[row][col])

    return diagonal
