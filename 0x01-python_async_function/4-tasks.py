#!/usr/bin/python3
""" 4. Tasks
"""
import asyncio
from random import uniform

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    """function that spawn task_wait_random n times with the specified
    max_delay return the list of all the delays
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
