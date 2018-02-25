class Error(Exception):
    pass


class EmptyStackError(Error):
    pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        try:
            if not self.top:
                raise EmptyStackError
            return self.top.data
        except EmptyStackError:
            print('Empty Stack')

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        try:
            if not self.top:
                raise EmptyStackError
            data = self.top.data
            self.top = self.top.next
            return data
        except EmptyStackError:
            print('Empty Stack')

    def print_list(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(-3)
    stack.push(5)
    stack.push(8)
    stack.push(9)
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    stack.print_list()
