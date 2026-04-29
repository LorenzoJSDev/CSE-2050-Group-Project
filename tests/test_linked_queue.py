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

# Local application
from required_classes.data_structures.linked_queue import LinkedQueue


class TestLinkedQueue(unittest.TestCase):
    """
    Docstring for TestLinkedQueue.
        - Description: Contains the test cases for the LinkedQueue class.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestLinkedQueue.setUp()
            - Description: Sets up a fresh LinkedQueue object before each test.
            - Author: Lorenzo .S
        """
        self.queue = LinkedQueue()

    def test_init(self):
        """
        Docstring for TestLinkedQueue.test_init()
            - Description: Tests that the queue initializes correctly.
            - Author: Lorenzo .S
        """
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

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

    def test_dequeue_empty(self):
        """
        Docstring for TestLinkedQueue.test_dequeue_empty()
            - Description: Tests that dequeue raises an error when the queue is empty.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.queue.dequeue()

    def test_dequeue_reduces_size(self):
        """
        Docstring for TestLinkedQueue.test_dequeue_reduces_size()
            - Description: Tests that dequeue properly reduces queue size.
            - Author: Lorenzo .S
        """
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.queue.dequeue()

        self.assertEqual(len(self.queue), 1)

    def test_queue_becomes_empty_after_all_dequeues(self):
        """
        Docstring for TestLinkedQueue.test_queue_becomes_empty_after_all_dequeues()
            - Description: Tests that the queue reports empty after removing all items.
            - Author: Lorenzo .S
        """
        self.queue.enqueue("X")
        self.queue.enqueue("Y")

        self.queue.dequeue()
        self.queue.dequeue()

        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_mixed_enqueue_dequeue(self):
        """
        Docstring for TestLinkedQueue.test_mixed_enqueue_dequeue()
            - Description: Tests queue stability during mixed enqueue and dequeue operations.
            - Author: Lorenzo .S
        """
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.dequeue(), 1)

        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

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