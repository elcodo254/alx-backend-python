#!/usr/bin/env python3
"""
type annotated function that makes multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return function that multiplies float by `multiplier`.
    Args: multiplier: float
    """
    return lambda x: x * multiplier
