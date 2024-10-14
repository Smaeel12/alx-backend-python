#!/usr/bin/python3
""" 2. Measure the runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n
def measure_time(n, max_delay):
    """ function that measures the total execution time
    returns total_time / n
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n