import sys
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/linkedlist')
import linkedlist as ll


def ll_is_palindrome(head):
    """
    Given a linked list, write a function to detaermine whether the list is a palindrome.

    Ex.
    2 -> 1 -> 2 -> 1 -> 2 True
    O(n) O(1)
    """

    if head:
        fast = head
        slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.data)
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if slow.data != top:
                return False
            slow = slow.next

        return True


if __name__ == '__main__':
    linked_list = ll.LinkedList()
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(2)
    print(ll_is_palindrome(linked_list.head))
