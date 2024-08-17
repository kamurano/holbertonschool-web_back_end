#!/usr/bin/env python3
"""Measure the runtime of wait_n."""
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_runtime(n: int, max_delay: int) -> float:
    """Measures the total runtime and returns it."""
    import time

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n