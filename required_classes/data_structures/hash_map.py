#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hash_map.py
-------------

Description: Contains the HashMap class for Milestone 3

Author: Lorenzo .S
Date Created: 04-22-2026
Status: Development (alpha)

"""

# ===== Imports =====

# Standard library

# Third-party


# Local application


class HashMap:
    """
    Docstring for HashMap class
        - Description: The HashMap class using separate chaining and rehashing for the Milestone Three project
        - Author: Lorenzo .S
    """

    def __init__(self, size=5) -> None:
        """
        Docstring for HashMap.__init__()
         - Description: Initializes the HashMap with a given size and empty buckets
         - Author: Lorenzo .S
        """
        self._size = size
        self._buckets = [[] for _ in range(self._size)]
        self._count = 0

    def _hash(self, key):
        """
        Docstring for HashMap._hash()
            - Description: Computes the hash index for a given key
            - Author: Lorenzo .S
        """
        return hash(key) % self._size

    def _load_factor(self):
        """
        Docstring for HashMap._load_factor()
            - Description: Calculates the current load factor of the HashMap
            - Author: Lorenzo .S
        """
        return self._count / self._size

    def put(self, key, value):
        """
        Docstring for HashMap.put()
            - Description: Inserts or updates a key-value pair in the HashMap
            - Author: Lorenzo .S
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._count += 1

        if self._load_factor() >= 0.8:
            self._rehash()
        return

    def get(self, key):
        """
        Docstring for HashMap.get()
            - Description: Retrieves the value associated with a given key
            - Author: Lorenzo .S
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key {key} not found")

    def _rehash(self) -> None:
        """
        Docstring for HashMap._rehash()
            - Description: Doubles the bucket size and reinserts all key-value pairs
            - Author: Lorenzo .S
        """
        old_buckets = self._buckets
        self._size *= 2
        self._buckets = [[] for _ in range(self._size)]
        self._count = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def keys(self):
        """
        Docstring for HashMap.keys()
            - Description Return all keys stored in the hash map.
            - Author: Jerod Abraham    
        """
        keys = []
        for bucket in self._buckets:
            for entry in bucket:
                keys.append(entry[0])
        return keys

    def __len__(self):
        """
        Docstring for HashMap.__len__()
         - Description: Returns the number of key-value pairs stored in the HashMap.
         - Author: Lorenzo .S
        """
        return self._count

    def capacity(self):
        """
        Docstring for HashMap.capacity()
         - Description: Returns the current number of buckets in the HashMap.
         - Author: Lorenzo .S
        """
        return self._size