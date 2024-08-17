#!/usr/bin/env python3
"""safe_first_element function with type annotations."""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): The list to be evaluated.

    Returns:
        Union[Any, None]: The first element of the list if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
    