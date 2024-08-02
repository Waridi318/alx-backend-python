#!/usr/bin/env python3
"""This module contains a type-annotated function sum_list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function takes a list of floats as argument
    and returns their sum as a float
    """


    return sum(x for x in input_list)
