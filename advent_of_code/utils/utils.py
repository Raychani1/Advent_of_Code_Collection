from typing import Any, Dict


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
