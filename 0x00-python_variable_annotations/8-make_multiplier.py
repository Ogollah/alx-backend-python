#!/usr/bin/env python3
"""
Type-annotated function for creating a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a multiplier (float) and returns a callable function
    that multiplies its input by the specified multiplier.

    Parameters:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A callable function that multiplies its input by the multiplier.
    """
    return lambda x: x * multiplier
