#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    acc: int = 0
    for n in input_list:
        acc += n
    return acc
