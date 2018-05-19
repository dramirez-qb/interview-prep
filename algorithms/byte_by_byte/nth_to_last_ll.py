import sys

sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/data_structures/linkedlist')
from linkedlist import LinkedList

def nth_to_last(head, n):
    if head is None or n < 0:
        return None

    fast = head
    slow = head

    for i in range(n):
        fast = fast.next
        if fast is None:
            return None


    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    return slow.data


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(5)
    ll.append(5)
    ll.append(8)
    ll.append(11)

    n = int(input())

    print(nth_to_last(ll.head, n))
