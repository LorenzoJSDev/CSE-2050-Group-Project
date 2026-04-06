class Node:
    """
    Description: Represents a single element in the linked queue.
    Author: Jerod Abraham
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """
    Description: a queue using a linked list.
    Author: Jerod Abraham
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        removed_node = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return removed_node.data

    def __len__(self):
        return self.size

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        return self.front.data