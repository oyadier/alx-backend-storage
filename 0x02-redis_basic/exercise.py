#!/usr/bin/env python3
import redis
import uuid
from typing import Union
'''Writing strings to Redis'''


class Cache():
    """
        Cache class.
    """

    def __init__(self):
        '''
            Initialize the cache class
        '''
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, int, float, bytes]) -> str:
        ''' Store data in the cache '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
            Get data from the cache.
        '''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''
            Get a string from the cache.
        '''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''
            Get an int from the cache.
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
