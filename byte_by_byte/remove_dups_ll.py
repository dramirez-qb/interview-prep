import sys
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/linkedlist')
import linkedlist as ll

def remove_dups_ll(head):
    """
    Given the head of an unsorted linked list, write a function to remove all duplicates

    Ex.
    2 -> 1 -> 1 -> 3 -> 5 -> 3 -> 2
                        ^
    seen = {2, 1, 3, 5}
    prev = 5
    2 -> 1 -> 3 -> 5

    Iterate through ll
    Add elements to a set
    Use a previous pointer
    If current.data in seen
    O(n) O(n)
    """

    if head:
        current = head
        prev = None
        seen = set()

        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

        return head


if __name__ == '__main__':
    linked_list = ll.LinkedList()
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(3)
    linked_list.append(2)
    remove_dups_ll(linked_list.head)
    linked_list.print_list()
