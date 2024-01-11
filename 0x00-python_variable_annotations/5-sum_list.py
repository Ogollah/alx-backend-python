#!/usr/bin/env python3
"""
Type-annotated function for summing a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that takes a list of floats and returns their sum as a float.

    Parameters:
    input_list (List[float]): The input list of floats.

    Returns:
    float: The sum of the input list of floats.
    """
    return float(sum(input_list))
