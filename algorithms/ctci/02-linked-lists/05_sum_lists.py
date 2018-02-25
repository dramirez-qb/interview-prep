import linkedlist as ll


def add_lists(l1, l2, carry = 0):
    """
    Adds the elements of two linked lists
    """
    if l1 is None and l2 is None and not carry:
        return None

    result = ll.Node(None)
    value = carry
    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data
    result.data = value % 10

    if l1 is not None or l2 is not None:
        more = add_lists(None if l1 is None else l1.next,
                         None if l2 is None else l2.next,
                         1 if value >= 10 else 0)
        result.next = more
    return result


if __name__ == "__main__":
    l1 = ll.LinkedList()
    l2 = ll.LinkedList()
    l1.append(7)
    l1.append(1)
    l1.append(6)

    l2.append(5)
    l2.append(9)
    l2.append(2)

    add_lists(l1.head, l2.head)
