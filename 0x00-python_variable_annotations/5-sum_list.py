#!/usr/bin/env python3
"""type-annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function sum_list which takes a list input_list of floats as argument
    and returns their sum as a float
    """
    acc: int = 0
    for n in input_list:
        acc += n
    return acc
