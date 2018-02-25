import empty_queue_exception as eq


class Queue:
    """Queue implementation (FIFO)"""

    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        """Node in Queue"""

        def __init__(self, data):
            self.data = data
            self.next = None

    def is_empty(self):
        """
        Is queue empty?
        Runtime: O(1)
        """

        return self.head is None

    def peak(self):
        """
        Return top element in queue.
        Runtime: O(1)
        """

        if self.head is None:
            raise eq.EmptyQueueError
        return self.head.data

    def add(self, data):
        """
        Add element to end of queue.
        Runtime: O(1)
        """

        new_node = self.Node(data)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def remove(self):
        """
        Remove first element of queue.
        Runtime: O(1)
        """

        if self.head is None:
            raise eq.EmptyQueueError

        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return self.head.data

    def print_queue(self):
        """
        Print elements in queue
        Runtime: O(n)
        """

        current = self.head
        while current:
            print(current.data)
            current = current.next
