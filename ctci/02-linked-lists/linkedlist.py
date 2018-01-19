class Node:
    """Node in linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    """Singly linked list"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Add node to end of linked list
        Runtime: O(n)
        """

        if self.head is None:
            self.head = Node(data)
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
        return self.head

    def prepend(self, data):
        """
        Add node to beginning of list
        Runtime: O(1)
        """

        if self.head is None:
            self.head = Node(data)
            return self.head

        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        return self.head

    def delete_with_value(self, data):
        """
        Delete given node
        Runtime: O(n)
        """

        if(self.head is None):
            return self.head

        if(self.head.data == data):
            self.head = self.head.next
            return self.head

        current = self.head
        while current.next is not None:
            if(current.next.data == data):
                current.next = current.next.next
                return self.head
            current = current.next

    def print_list(self):
        """
        Print linked list
        Runtime: O(n)
        """

        current = self.head
        while current:
            print(current, end=' ')
            current = current.next
