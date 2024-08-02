#!/usr/bin/env python3
"""This module contains a type-annotated function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float argument and returns
    a function that multiplies a float by multiplier
    """

    return (lambda value: value * multiplier)
