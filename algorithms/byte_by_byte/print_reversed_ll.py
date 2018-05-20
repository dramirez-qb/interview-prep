import sys

sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/data_structures/linkedlist')
from linkedlist import LinkedList

def reverse_ll(head):
    '''
    Given a linked list, print the nodes of the list in reverse order.
    '''

    if head is None:
        return None

    reverse_ll(head.next)
    print(head.data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(3)
    ll.append(3)
    ll.append(0)
    ll.append(5)
    ll.append(8)
    ll.append(2)

    reverse_ll(ll.head)
