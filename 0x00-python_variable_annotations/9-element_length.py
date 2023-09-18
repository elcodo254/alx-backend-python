#!/usr/bin/env python3
"""
Annotate function’s parameters and return values with appropriate types
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return list of tuples, one for each element, of which
    consists of the element itself and its length.
    Args: lst: Iterable[Sequence]
    """
    return [(i, len(i)) for i in lst]
