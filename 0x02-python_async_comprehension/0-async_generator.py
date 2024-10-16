#!/usr/bin/env python3
""" 0. Async Generator
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An asynchronous generator"""
    for _ in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
