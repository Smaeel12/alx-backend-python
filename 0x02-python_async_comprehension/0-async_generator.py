#!/usr/bin/env python3
""" 0. Async Generator
"""
import asyncio
from random import uniform
from typing import AsyncGenerator



async def async_generator() -> AsyncGenerator[float]:
    """ An asynchronous generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
