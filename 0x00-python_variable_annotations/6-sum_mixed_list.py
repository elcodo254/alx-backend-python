#!/usr/bin/env python3
"""
function that takes a list mxd_lst of floats and integers and
returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return sum of elements of mxd_list.
    Arguments: mxd_lst: List[Union[int, float]]
    """
    return sum(mxd_lst)
