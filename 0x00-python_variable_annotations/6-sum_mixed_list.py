#!/usr/bin/env python3
"""This module contains a type-annotated function
sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list mxd_lst of integers
    and floats and returns their sum as a float.
    """
    return sum(x for x in mxd_lst)
