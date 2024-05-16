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
