#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_linked_queue.py
-------------

Description: Contains the test cases for the LinkedQueue class.

Author: Lorenzo .S
Contributors:
Date Created: 04-08-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application (your project modules)
from required_classes.data_structures.linked_queue import LinkedQueue


# ==== Classes ==== #
class TestLinkedQueue(unittest.TestCase):
    """
    Docstring for TestLinkedQueue.
        - Description: Contains the test cases for the LinkedQueue class.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestLinkedQueue.setUp()
            - Description: Sets up objects for testing.
            - Author: Lorenzo .S
        """
        self.queue = LinkedQueue()

    # ---- Test LinkedQueue.__init__() ---- #

    def test_init(self):
        """
        Docstring for TestLinkedQueue.test_init()
            - Description: Tests that the queue initializes correctly.
            - Author: Lorenzo .S
        """
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    # ---- Test enqueue() and __len__() ---- #

    def test_enqueue_and_size(self):
        """
        Docstring for TestLinkedQueue.test_enqueue_and_size()
            - Description: Tests enqueue operation and size tracking.
            - Author: Lorenzo .S
        """
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(len(self.queue), 3)
        self.assertFalse(self.queue.is_empty())

    # ---- Test FIFO behavior ---- #

    def test_fifo_order(self):
        """
        Docstring for TestLinkedQueue.test_fifo_order()
            - Description: Tests that items are dequeued in FIFO order.
            - Author: Lorenzo .S
        """
        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.queue.enqueue("C")

        self.assertEqual(self.queue.dequeue(), "A")
        self.assertEqual(self.queue.dequeue(), "B")
        self.assertEqual(self.queue.dequeue(), "C")

    # ---- Test dequeue on empty ---- #

    def test_dequeue_empty(self):
        """
        Docstring for TestLinkedQueue.test_dequeue_empty()
            - Description: Tests that dequeue raises an error when the queue is empty.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.queue.dequeue()

    # ---- Test peek() ---- #

    def test_peek(self):
        """
        Docstring for TestLinkedQueue.test_peek()
            - Description: Tests peek returns the front item without removing it.
            - Author: Lorenzo .S
        """
        self.queue.enqueue(10)
        self.queue.enqueue(20)

        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(len(self.queue), 2)

    def test_peek_empty(self):
        """
        Docstring for TestLinkedQueue.test_peek_empty()
            - Description: Tests that peek raises an error when the queue is empty.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.queue.peek()


if __name__ == "__main__":
    unittest.main()