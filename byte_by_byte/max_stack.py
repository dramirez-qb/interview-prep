print('importing max stack module')

class MaxStack:
    def __init__(self):
        self.top = None
        self.max = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.old_max = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is not None:
            return self.top.data

    def push(self, data):
        new_node = self.Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        if self.max is None or new_node.data > self.max.data:
            new_node.old_max = self.max
            self.max = new_node

    def pop(self):
        try:
            if self.top is None:
                raise IndexError
            remove_node = self.top
            self.top = remove_node.next
            if remove_node.old_max is not None:
                self.max = remove_node.old_max
            return remove_node.data
        except IndexError:
            print('Empty Stack')

    def get_max(self):
        try:
            if self.top is None:
                raise IndexError
            return self.max.data
        except IndexError:
            print('Empty Stack')

    def print_stack(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    stack = MaxStack()
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.push(5)
    stack.pop()
    stack.print_stack()
    print(stack.get_max())
