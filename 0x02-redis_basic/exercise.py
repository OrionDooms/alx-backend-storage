#!/usr/bin/env python3
""" Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """The __init__ method store an instance of the Redis client
        is a private"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The Store method takes in data as argument and returns
        a generate key and string."""
        temp = str(uuid.uuid4())
        self._redis.set(name=temp, value=data)
        return temp

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """The get method take a key string argument and an
        optional Callable argument named fn"""
        return fn(value) if fn and value is not None else value

    def get_str(self, key: str) -> str:
        """Get_str will automatically parametrize Cache.get with the
        correct conversion function."""
        return self.get(key, bytes.decode)

    def get_int(self, key: str) -> int:
        """Get_int will automatically parametrize Cache.get with the
        correct conversion function."""
        return self.get(key, lambda x: int(x.decode('utf-8')))
