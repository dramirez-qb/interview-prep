import linkedlist as ll


def partition(head, x):
    """
    Partition a linked list around a value x.
    All nodes less than x come before all nodes greater than or equal to x.
    Runtime
    O(n) O(n)
    """
    
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    current = head
    while current is not None:
        next = current.next
        current.next = None
        if current.data < x:
            if before_start is None:
                before_start = current
                before_end = before_start
            else:
                before_end.next = current
                before_end = current
        else:
            if after_start is None:
                after_start = current
                after_end = after_start
            else:
                after_end.next = current
                after_end = current
        current = current.next

    if before_start is None:
        return after_start
    before_end.next = after_start
    return before_start


if __name__ == "__main__":
    linked_list = ll.LinkedList()
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(8)
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(2)
    linked_list.append(1)
    x = 5
    linked_list.print_list()
    partition_list = partition(linked_list.head, x)
    partition_list.print_list()
