#!/usr/bin/env python3
"""
Type-annotated function for converting a key and value to a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a key (string) and a value (union of int or float)
    and returns a tuple with the key and the square of the value as a float.

    Parameters:
    k (str): The input key as a string.
    v (Union[int, float]): The input value as either an integer or a float.

    Returns:
    Tuple[str, float]: A tuple containing the key and
    the square of the value as a float.
    """
    return (k, float(v**2))
