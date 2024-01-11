#!/usr/bin/env python3
"""
Type-annotated function for summing a mixed list of integers and floats.
"""
from typing import Union, List


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Function that takes a mixed list of integers and floats
    and returns their sum as a float.

    Parameters:
    mixed_list (List[Union[int, float]]):
    The input mixed list of integers and floats.

    Returns:
    float: The sum of the input mixed list.
    """
    return float(sum(mixed_list))
