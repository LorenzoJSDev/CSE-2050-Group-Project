class Node:
    """
    Docstring for Node class
        - Description: Represents a single element in the linked queue.
        - Author: Jerod Abraham
    """

    def __init__(self, data):
        """
        Docstring for Node.__init__()
            - Description: Initializes a Node with data and a reference to the next node.
            - Author: Jerod Abraham
        """
        self.data = data
        self.next = None


class LinkedQueue:
    """
    Docstring for LinkedQueue class
        - Description: Implements a queue using a linked list.
        - Author: Jerod Abraham
    """

    def __init__(self):
        """
        Docstring for LinkedQueue.__init__()
            - Description: Initializes an empty queue with front and rear pointers.
            - Author: Jerod Abraham
        """
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """
        Docstring for LinkedQueue.is_empty()
            - Description: Returns True if the queue is empty, otherwise False.
            - Author: Jerod Abraham
        """
        return self.size == 0

    def enqueue(self, item):
        """
        Docstring for LinkedQueue.enqueue()
            - Description: Adds an item to the rear of the queue.
            - Author: Jerod Abraham
        """
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        """
        Docstring for LinkedQueue.dequeue()
            - Description: Removes and returns the item at the front of the queue. Raises a ValueError if the queue is empty.
            - Author: Jerod Abraham
        """
        if self.is_empty():
            raise ValueError("Queue is empty")

        removed_node = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return removed_node.data

    def __len__(self):
        """
        Docstring for LinkedQueue.__len__()
            - Description: Returns the number of items currently in the queue.
            - Author: Jerod Abraham
        """
        return self.size

    def peek(self):
        """
        Docstring for LinkedQueue.peek()
            - Description: Returns the item at the front of the queue without removing it. Raises a ValueError if the queue is empty.
            - Author: Jerod Abraham
        """
        if self.is_empty():
            raise ValueError("Queue is empty")

        return self.front.data