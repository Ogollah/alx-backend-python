#!/usr/bin/env python3
"""
Type-annotated function for creating multiple
copies of items in a tuple.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Function that takes a tuple and a zoom factor,
    and returns a list with multiple copies
    of each item in the tuple based on the specified factor.

    Parameters:
    lst (Tuple): The input tuple.
    factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
    List: A list with multiple copies of each item in
    the tuple based on the specified factor.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
