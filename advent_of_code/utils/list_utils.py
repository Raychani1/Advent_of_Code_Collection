
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