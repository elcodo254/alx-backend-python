#!/usr/bin/env python3
"""
type-annoted function that returns floor of float
"""


def floor(n: float) -> int:
    """
    Returns larn=gest int value less or equal to n
    args: n - float
    """
    return int(n) if n >= 0 else int(n) - 1
