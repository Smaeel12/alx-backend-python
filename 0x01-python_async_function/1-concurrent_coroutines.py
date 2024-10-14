#!/usr/bin/python3
""" 1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """ function that spawn wait_random n times with the specified max_delay
    return the list of all the delays
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    
    return delays