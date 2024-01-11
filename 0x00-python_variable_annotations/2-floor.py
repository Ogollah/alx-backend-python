#!/usr/bin/env python3
"""
Type-annotated function for flooring a float and returning an integer.
"""
import math


def floor(n: float) -> int:
    """
    Function that floors a float and returns the result as an integer.

    Parameters:
    n (float): The input float.

    Returns:
    int: The result of flooring the input float.
    """
    return math.floor(n)
