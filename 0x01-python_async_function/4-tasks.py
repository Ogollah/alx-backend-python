#!/usr/bin/env python3
"""
Asynchronous Python
"""

from typing import List
import asyncio
time_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of awaited responses from the previous function
    """
    tasks = [time_wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*tasks)
    return sorted(res)
