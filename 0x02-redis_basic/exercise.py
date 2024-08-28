#!/usr/bin/env python3
""" Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """The __init__ method store an instance of the Redis client
        is a private"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The Store method takes in data as argument and returns
        a generate key and string."""
        temp = str(uuid4())
        self._redis.set(name=temp, value=data)
        return Temp
