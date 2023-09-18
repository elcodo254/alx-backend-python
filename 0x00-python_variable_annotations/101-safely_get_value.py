#!/usr/bin/env python3
"""
adding type notations to functions
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return dct[key] if it exists, otherwise return `default`.
    Args: T - a TypeVar with value '~T'
    """
    if key in dct:
        return dct[key]
    else:
        return default
