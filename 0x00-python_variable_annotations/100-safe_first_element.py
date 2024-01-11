#!/usr/bin/env python3
"""
Type-annotated function for retrieving the first
element of a sequence if it exists.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that takes a sequence and returns the first element
    if it exists, or None otherwise.

    Parameters:
    lst (Sequence[Any]): The input sequence.

    Returns:
    Union[Any, None]: The first element of the sequence or None
    if the sequence is empty.
    """
    return lst[0] if lst else None
