#!/usr/bin/env python3
"""Module providing an asynchronous generator of random numbers"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random numbers between 0 and 10, waiting a second each"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
