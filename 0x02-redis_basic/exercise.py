#!/usr/bin/env python3
"""
write to redis
"""
import redis
from uuid import uuid4
from typing import Any


class Cache():
    """
    write to redis
    """
    def __init__(self):
        """initialize redis in class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """get uuid key and save data"""
        keystore = str(uuid4())
        self._redis.set(keystore, data)
        return keystore
