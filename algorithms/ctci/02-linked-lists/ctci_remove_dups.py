import linkedlist as ll


def remove_dups(linked_list, head):
    if head is None:
        return None

    if head.next is None:
        return head

    current = head
    values_set = set()
    while current.next is not None:
        if current.next.data in values_set:
            current.next = current.next.next
        else:
            values_set.add(current.data)
        current = current.next
    return head


def remove_dups_runner(linked_list, head):
    if head is None:
        return None

    if head.next is None:
        return head

    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


if __name__ == "__main__":
    linked_list = ll.LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(3)
    linked_list.append(7)
    linked_list.append(1)
    linked_list.append(2)
    print('before')
    linked_list.print_list()
    remove_dups_runner(linked_list, linked_list.head)
    print('after')
    linked_list.print_list()
