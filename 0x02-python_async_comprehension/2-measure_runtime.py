#!/usr/bin/env python3
"""
async gather in coroutine
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension 4 times in parallel using asyncio.gather
    measure the total runtime and return it.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
