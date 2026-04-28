#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_milestone3.py
-------------

Description: Contains unit tests for the HashMap class for Milestone 3

Author: Lorenzo .S
Date Created: 04-22-2026
Status: Development (alpha)

"""

# ===== Imports =====

# Standard library
import unittest

# Third-party

# Local application
from required_classes.data_structures.hash_map import HashMap


class BadHash:
    """
    Docstring for BadHash class
        - Description: Helper class used to force hash collisions for testing
        - Author: Lorenzo .S
    """

    def __init__(self, value):
        """
        Docstring for BadHash.__init__()
         - Description: Initializes the BadHash object with a value
         - Author: Lorenzo .S
        """
        self.value = value
        return

    def __hash__(self):
        """
        Docstring for BadHash.__hash__()
            - Description: Forces all instances to have the same hash value
            - Author: Lorenzo .S
        """
        return 1

    def __eq__(self, other):
        """
        Docstring for BadHash.__eq__()
            - Description: Compares two BadHash objects for equality
            - Author: Lorenzo .S
        """
        return isinstance(other, BadHash) and self.value == other.value

    def __repr__(self):
        """
        Docstring for BadHash.__repr__()
            - Description: Returns string representation of BadHash object
            - Author: Lorenzo .S
        """
        return f"BadHash({self.value})"


class TestHashMap(unittest.TestCase):
    """
    Docstring for TestHashMap class
        - Description: Contains unit tests for HashMap functionality including collisions and rehashing
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestHashMap.setUp()
            - Description: Initializes a new HashMap before each test
            - Author: Lorenzo .S
        """
        self.map = HashMap()
        return

    def test_put_and_get_single_item(self):
        """
        Docstring for TestHashMap.test_put_and_get_single_item()
            - Description: Tests inserting and retrieving a single key-value pair
            - Author: Lorenzo .S
        """
        self.map.put("CSE2050", "Data Structures")
        self.assertEqual(self.map.get("CSE2050"), "Data Structures")

    def test_put_updates_existing_key(self):
        """
        Docstring for TestHashMap.test_put_updates_existing_key()
            - Description: Tests updating the value of an existing key
            - Author: Lorenzo .S
        """
        self.map.put("CSE2050", "Old Value")
        self.map.put("CSE2050", "New Value")
        self.assertEqual(self.map.get("CSE2050"), "New Value")

    def test_get_missing_key_raises_keyerror(self):
        """
        Docstring for TestHashMap.test_get_missing_key_raises_keyerror()
            - Description: Tests that accessing a missing key raises KeyError
            - Author: Lorenzo .S
        """
        with self.assertRaises(KeyError):
            self.map.get("DOES_NOT_EXIST")

    def test_collision_handling(self):
        """
        Docstring for TestHashMap.test_collision_handling()
            - Description: Tests that multiple keys with same hash are handled correctly
            - Author: Lorenzo .S
        """
        key1 = BadHash("A")
        key2 = BadHash("B")
        key3 = BadHash("C")

        self.map.put(key1, 100)
        self.map.put(key2, 200)
        self.map.put(key3, 300)

        self.assertEqual(self.map.get(key1), 100)
        self.assertEqual(self.map.get(key2), 200)
        self.assertEqual(self.map.get(key3), 300)

    def test_rehash_triggers_at_point_eight_load_factor(self):
        """
        Docstring for TestHashMap.test_rehash_triggers_at_point_eight_load_factor()
            - Description: Tests that rehash occurs when load factor reaches 0.8
            - Author: Lorenzo .S
        """
        hmap = HashMap(5)

        original_size = hmap._size

        hmap.put("a", 1)
        hmap.put("b", 2)
        hmap.put("c", 3)
        hmap.put("d", 4)

        self.assertEqual(hmap._size, original_size * 2)

    def test_all_items_preserved_after_rehash(self):
        """
        Docstring for TestHashMap.test_all_items_preserved_after_rehash()
            - Description: Tests that all key-value pairs remain after rehashing
            - Author: Lorenzo .S
        """
        hmap = HashMap(5)

        items = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6
        }

        for key, value in items.items():
            hmap.put(key, value)

        for key, value in items.items():
            self.assertEqual(hmap.get(key), value)

    def test_collision_items_preserved_after_rehash(self):
        """
        Docstring for TestHashMap.test_collision_items_preserved_after_rehash()
            - Description: Tests that collision-based entries persist after rehashing
            - Author: Lorenzo .S
        """
        hmap = HashMap(5)

        key1 = BadHash("A")
        key2 = BadHash("B")
        key3 = BadHash("C")
        key4 = BadHash("D")

        hmap.put(key1, 10)
        hmap.put(key2, 20)
        hmap.put(key3, 30)
        hmap.put(key4, 40)

        self.assertEqual(hmap.get(key1), 10)
        self.assertEqual(hmap.get(key2), 20)
        self.assertEqual(hmap.get(key3), 30)
        self.assertEqual(hmap.get(key4), 40)


if __name__ == "__main__":
    unittest.main()