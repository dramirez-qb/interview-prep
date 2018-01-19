import linkedlist as ll


def delete_middle_node(n):
    """
    Delete a node in the middle (not first or last)
    Runtime
    O(1) O(1)
    """
    if n is None or n.next is None:
        return False
    next = n.next
    n.data = next.data
    n.next = next.next
    return True


if __name__ == "__main__":
    linked_list = ll.LinkedList()
    linked_list.append('a')
    linked_list.append('b')
    linked_list.append('c')
    linked_list.append('d')
    linked_list.append('e')
    linked_list.append('f')
    linked_list.print_list()
    delete_middle_node(linked_list.head.next)
    linked_list.print_list()
