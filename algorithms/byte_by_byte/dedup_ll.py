import sys

sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/data_structures/linkedlist')
from linkedlist import LinkedList

def delete_dups(head):
    '''
    Remove all duplicates from a linked list.
    '''

    if not head:
        return None

    dups = set()
    curr = head
    while curr:
        if curr.data in dups:
            prev.next = curr.next
        else:
            dups.add(curr.data)
            prev = curr
        curr = curr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(-2)
    ll.append(3)
    ll.append(1)
    ll.append(2)

    delete_dups(ll.head)

    ll.print_list()
