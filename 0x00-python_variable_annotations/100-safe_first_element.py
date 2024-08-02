#!/usr/bin/env python3
"""
This module is used to practise duck-typing annotations
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function return the first element of a list
    or None if list is empty
    """
    if lst:
        return lst[0]
    else:
        return None
