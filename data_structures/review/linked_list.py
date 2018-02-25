class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return self.head
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return self.head

    def delete_with_value(self, data):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
                return self.head

            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return self.head
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(2)
    ll.append(15)
    ll.append(20)
    ll.prepend(1)
    ll.delete_with_value()
    ll.print_list()
