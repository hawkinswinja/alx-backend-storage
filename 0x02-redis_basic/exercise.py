#!/usr/bin/env python3
"""exercise"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """wraps the function and increments its count"""
    key = method.__qualname__
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increments the key of the method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """wraps method to add data to redis list"""
    @wraps(method)
    def wrapper2(self, *args, **kwargs):
        """add inputs and outputs to list"""
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return output
    return wrapper2


class Cache():
    """class description of a Cache"""
    def __init__(self):
        """initialize instance of class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """returns the value of key"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        else:
            return val

    def get_str(self, key: str) -> str:
        """returns the str version of get"""
        return str(self.get(key).decode('utf-8'))

    def get_int(self, key: str) -> int:
        """returns the str version of get"""
        return int(self.get(key).decode('utf-8'))
