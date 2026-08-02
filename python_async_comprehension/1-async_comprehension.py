#!/usr/bin/env python3
"""Module collecting random numbers with an async comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the ten random numbers yielded by async_generator"""
    return [number async for number in async_generator()]
