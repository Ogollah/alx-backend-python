#!/usr/bin/env python3
"""
Type-annotated function for computing the length of
each element in a list of sequences.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list of sequences and returns a list of tuples,
    where each tuple contains a sequence and its corresponding length.

    Parameters:
    lst (Iterable[Sequence]): The input list of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples containing
    each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
