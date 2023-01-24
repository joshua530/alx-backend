#!/usr/bin/env python3
"""
contains implementation of LIFO cache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO cache implementation
    """
    def __init__(self):
        """init method"""
        self.__cache_keys = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.__cache_keys) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                to_remove = self.__cache_keys[len(self.__cache_keys) - 1]
                print("DISCARD: {}".format(to_remove))
                self.cache_data.pop(to_remove)
                self.__cache_keys = self.__cache_keys[0: len(self.__cache_keys) - 1]
        self.cache_data[key] = item
        self.__cache_keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
