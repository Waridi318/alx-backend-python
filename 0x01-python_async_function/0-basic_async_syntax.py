#!/usr/bin/env python3

"""This module defines an asynchronous coroutine
"""


import random
import asyncio


async def wait_random(max_delay=10):
    """a coroutine that takes in an integer argument,
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
