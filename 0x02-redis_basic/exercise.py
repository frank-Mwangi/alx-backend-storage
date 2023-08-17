#!/usr/bin/env python3
"""
The Cache class
"""

import redis
import uuid
from typing import Union, Callable


class Cache:
    """Class to store data attached to random keys in Redis"""
    def __init__(self):
        """The init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis, returns unique
        random key as a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float, None]:
        """Converts data back to desired format"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """get string format of value pointed to by key"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """get int representation of value paired to key"""
        return self.get(key, fn=int)
