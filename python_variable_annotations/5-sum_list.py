#!/usr/bin/env python3
"""Module providing a type-annotated list sum function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats"""
    return sum(input_list)
