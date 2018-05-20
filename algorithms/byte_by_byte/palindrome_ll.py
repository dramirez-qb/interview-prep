import sys

sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/data_structures/linkedlist')
from linkedlist import LinkedList

def is_palidrome(head):
    '''
    Determine whether a linked list is a palidrome.
    '''

    if head is None:
        return False

    fast = head
    slow = head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        fast = fast.next.next
        slow = slow.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.data != stack.pop():
            return False

        slow = slow.next

    return True

if __name__ == '__main__':
    ll_1 = LinkedList()
    ll_1.append(1)
    ll_1.append(2)
    ll_1.append(2)
    ll_1.append(1)

    print(is_palidrome(ll_1.head))

    ll_2 = LinkedList()
    ll_2.append(2)
    ll_2.append(3)

    print(is_palidrome(ll_2.head))

    ll_3 = LinkedList()
    ll_3.append(1)
    ll_3.append(2)
    ll_3.append(1)

    print(is_palidrome(ll_3.head))
