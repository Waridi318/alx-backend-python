#!/usr/bin/env python3
"""
This module shows the use of TypeVar
"""


from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None]
) -> Union[Any, T]:

    """This function returns the keys found in a
    dictionary argument provided
    """
    if key in dct:
        return dct[key]
    else:
        return default
