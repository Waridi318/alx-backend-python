#!/usr/bin/env python3
"""This module contains a type-annotated function to_kv
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes 2 arguments and returns a tuple
    """

    return (k, v ** 2)
