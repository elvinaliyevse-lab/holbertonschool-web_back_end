#!/usr/bin/env python3
"""Module spawning several wait_random coroutines concurrently"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in ascending order"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for coroutine in asyncio.as_completed(coroutines):
        delays.append(await coroutine)
    return delays
