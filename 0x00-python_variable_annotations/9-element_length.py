#!/usr/bin/env python3
"""
This module was aimed at duck typing an iterable object
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function takes an iterable as an argument
    and returns a list"""
    return [(i, len(i)) for i in lst]
