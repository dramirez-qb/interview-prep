import linkedlist as ll


def is_palindrome(head):
    """
    Returns if a linked list is a palindrome
    Runtime
    O(n) O(1)
    """
    fast = head
    slow = head

    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next
    return True


if __name__ == "__main__":
    linked_list = ll.LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(1)

    linked_list.print_list()
    print(is_palindrome(linked_list.head))
