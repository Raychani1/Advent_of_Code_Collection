from typing import List, Optional


class MathExpressionTreeNode:

    """Represents a combination of math expressions. Each node is the result of
    different operations:

    - The left child is the result of the sum operation.
    - The middle child is the result of the concatenation operation.
    - The right child is the result of the multiplication operation.
    """

    def __init__(self, value: int) -> None:
        """Initializes a MathExpressionTreeNode object.

        Args:
            value (int): Value to assigned to the node.
        """
        self.value: int = value
        self.left: Optional[MathExpressionTreeNode] = None
        self.middle: Optional[MathExpressionTreeNode] = None
        self.right: Optional[MathExpressionTreeNode] = None


def build_tree(numbers: List[int]) -> MathExpressionTreeNode:
    """Builds a tree of Math expressions, containing Math Expression Tree Nodes.

    Args:
        numbers (List[int]): List of values used for calculations.

    Returns:
        MathExpressionTreeNode: Root object of the Math Expression Tree.
    """
    if len(numbers) == 1:
        # Base case: only one number, return it as a leaf node
        return MathExpressionTreeNode(numbers[0])

    # Take two numbers from the list
    left_value = numbers[0] + numbers[1]  # Sum
    middle_value = int(str(numbers[0]) + str(numbers[1]))  # Concatenation
    right_value = numbers[0] * numbers[1]  # Multiplication

    # Create the current node with left, middle and right children, build them
    # recursively
    node = MathExpressionTreeNode(numbers[0])
    node.left = build_tree([left_value] + numbers[2:])
    node.middle = build_tree([middle_value] + numbers[2:])
    node.right = build_tree([right_value] + numbers[2:])

    return node


def print_tree(node: Optional[MathExpressionTreeNode], depth: int = 0) -> None:
    """Prints Math Expression Tree recursively starting from `node`. Depth
    considers `node` the root of the given tree.

    Args:
        node (Optional[MathExpressionTreeNode]): Node in the Math Expression
            Tree.
        depth (int, optional): Depth of current node. Defaults to 0.
    """
    if node is None:
        return
    print(' ' * depth * 2 + f"Node: {node.value}")
    print_tree(node.left, depth + 1)
    print_tree(node.middle, depth + 1)
    print_tree(node.right, depth + 1)


def get_tree_values(
    node: Optional[MathExpressionTreeNode], fetch_middle: bool = False
) -> List[int]:
    """Returns all the values from given Math Expression Tree.

    Args:
        node (Optional[MathExpressionTreeNode]): Node to fetch values from.
        fetch_middle (bool, optional): Flag wether the concatenated values
            should be extracted. Defaults to False.

    Returns:
        List[int]: _description_
    """
    if node is None:
        return []

    # If it's a leaf node (no left and no right children)
    if node.left is None and node.right is None:
        return [node.value]

    # Recursively collect leaf values from both left and right subtrees
    leaf_values: List[int] = []

    leaf_values.extend(
        get_tree_values(node=node.left, fetch_middle=fetch_middle)
    )

    if fetch_middle:
        leaf_values.extend(
            get_tree_values(node=node.middle, fetch_middle=fetch_middle)
        )

    leaf_values.extend(
        get_tree_values(node=node.right, fetch_middle=fetch_middle)
    )

    return leaf_values
