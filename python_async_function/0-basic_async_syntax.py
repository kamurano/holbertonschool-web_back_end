#!/usr/bin/env python3
"""Basic async syntax."""
import asyncio
import random


async def wait_random(max_delay = 10):
    """Wait for a random amount of seconds."""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
    