#!/usr/bin/env python3
"""Module measuring the runtime of four parallel async comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the total runtime of four parallel async_comprehension calls"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
