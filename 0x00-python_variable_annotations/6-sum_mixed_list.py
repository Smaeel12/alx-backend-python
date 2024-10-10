#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    acc: int = 0
    for n in mxd_lst:
        acc += n
    return acc
