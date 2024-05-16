#!/usr/bin/env python3
import redis
import uuid
from typing import Union
'''Writing strings to Redis'''


class Cache():

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, int, float, bytes]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
