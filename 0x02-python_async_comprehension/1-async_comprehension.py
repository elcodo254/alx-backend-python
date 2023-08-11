#!/usr/bin/env python3
"""
async comprehension coroutine
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    loop 10 times, each time asynchronously wait 1 second, then yield a
    random number between 0 and 10.
    """
    result = [i async for i in async_generator()]
    return result
