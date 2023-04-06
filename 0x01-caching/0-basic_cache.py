#!/usr/bin/python3
"""
contains caching class
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    contains caching class
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        # is None is right, not == None
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        # is None is right, not == None
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
