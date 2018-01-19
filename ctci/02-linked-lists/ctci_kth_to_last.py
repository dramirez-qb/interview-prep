import linkedlist as ll


def kth_to_last(ll, head, k):
    if head is None or k < 1:
        return None
    fast = head
    slow = head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow.data

if __name__ == "__main__":
    linked_list = ll.LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(-1)
    linked_list.append(3)
    linked_list.append(7)
    linked_list.append(9)
    linked_list.append(6)
    linked_list.append(5)
    k = 1
    print(kth_to_last(linked_list, linked_list.head, k))
