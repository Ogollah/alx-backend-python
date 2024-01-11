#!/usr/bin/env python3
"""
Type-annotated function for safely retrieving a value
from a dictionary using a given key.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Function that takes a dictionary, a key, and an
    optional default value, and returns the value
    associated with the key in the dictionary.
    If the key is not present, it returns the default value.

    Parameters:
    dct (Mapping): The input dictionary.
    key (Any): The key to retrieve from the dictionary.
    default (Def, optional): The default value to return
    if the key is not present. Defaults to None.

    Returns:
    Res: The value associated with the key or the default value
    if the key is not present.
    """
    return dct.get(key, default)
