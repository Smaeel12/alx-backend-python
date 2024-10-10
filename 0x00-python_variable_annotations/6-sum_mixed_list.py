#!/usr/bin/env python3
"""type-annotated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function sum_mixed_list which takes a list mxd_lst of integers and
    floats and returns their sum as a float
    """
    acc: int = 0
    for n in mxd_lst:
        acc += n
    return acc
