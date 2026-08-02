#!/usr/bin/env python3
"""Module providing a type-annotated key/value tuple function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple holding the string and the square of the number"""
    return (k, v ** 2)
