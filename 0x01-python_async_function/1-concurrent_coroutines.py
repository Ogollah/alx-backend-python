#!/usr/bin/env python3
"""
Asynchronous Python
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of awaited responses from the previous function
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*tasks)
    return sorted(res)
