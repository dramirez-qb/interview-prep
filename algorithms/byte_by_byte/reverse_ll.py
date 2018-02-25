import sys
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/linkedlist')
import linkedlist as ll


def reverse_ll(head):
    if head:
        reverse_ll(head.next)
        print(head.data, end=' ')


if __name__ == '__main__':
    linked_list = ll.LinkedList()
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)
    reverse_ll(linked_list.head)
