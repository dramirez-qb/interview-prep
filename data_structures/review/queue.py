class Error(Exception):
    pass


class EmptyQueueError(Error):
    pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        try:
            if not self.head:
                raise EmptyQueueError
            return self.head.data
        except EmptyQueueError:
            print('Empty Queue')

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(1)
    print(queue.is_empty())
    print(queue.peek())
    queue.dequeue()
    queue.print_list()
