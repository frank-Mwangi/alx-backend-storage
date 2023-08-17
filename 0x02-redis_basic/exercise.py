#!/usr/bin/env python3
"""
The Cache class
"""

import redis
import uuid
from typing import Union


class Cache:
    """Class to store data attached to random keys in Redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
