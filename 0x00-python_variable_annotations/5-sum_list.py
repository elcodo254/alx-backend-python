#!/usr/bin/env python3
"""
type-annotated function that takes list of floats and returns sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return sum of all elements in input_list.
    args: input_list - list of floats
    """
    return sum(input_list)
