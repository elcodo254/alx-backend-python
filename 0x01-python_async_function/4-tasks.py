#!/usr/bin/env python3
"""
Asynchronous coroutine that takes integer args
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in args, waits for random delay then returns it
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = [await task for task in asyncio.as_completed(tasks)]
    return delay
