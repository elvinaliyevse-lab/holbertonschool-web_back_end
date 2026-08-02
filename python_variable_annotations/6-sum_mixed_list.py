#!/usr/bin/env python3
"""Module providing a type-annotated mixed list sum function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats as a float"""
    return sum(mxd_lst)
