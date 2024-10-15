#!/usr/bin/env python3
""" module 0. The basics of async
"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """asynchronous coroutine that waits for a random delay between
    0 and max_delay (included and float value) seconds and eventually
    returns it
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
