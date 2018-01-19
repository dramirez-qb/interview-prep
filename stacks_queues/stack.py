import empty_stack_exception as es


class Stack:
    """Stack implementation (LIFO)"""

    def __init__(self):
        self.top = None

    class Node:
        """Node in stack"""

        def __init__(self, data):
            self.data = data
            self.next = None

    def is_empty(self):
        """
        Is stack empty?
        Runtime: O(1)
        """

        return self.top is None

    def peak(self):
        """
        Return top element in stack
        Runtime: O(1)
        """

        if self.top is None:
            raise es.EmptyStackError('Empty Stack')
        return self.top.data

    def push(self, data):
        """
        Add element to top of stack
        Runtime: O(1)
        """

        new_node = self.Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Remove element at top of stack
        Runtime: O(1)
        """

        if self.top is None:
            raise es.EmptyStackError('Empty Stack')
        data = self.top.data
        self.top = self.top.next
        return data

    def print_stack(self):
        """
        Print elements in stack
        Runtime: O(n)
        """

        current = self.top
        while current:
            print(current.data)
            current = current.next
