import heap_exception as he


class MinHeap:
    """
    Min Heap implementation (complete binary tree). Each node is smaller than its children.
    """

    def __init__(self):
        self.items = []
        self.size = 0

    def get_left_child_index(self, parent_index):
        """
        Get left child of a given parent node.
        Runtime: O(1)
        """

        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        """
        Get right child of a given parent node.
        Runtime: O(1)
        """

        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        """
        Get parent index of given child node.
        Runtime: O(1)
        """

        return (child_index - 1) // 2

    def has_left_child(self, index):
        """
        Node has left child?
        Runtime: O(1)
        """

        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        """
        Node has right child?
        Runtime: O(1)
        """

        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        """
        Node has parent?
        Runtime: O(1)
        """

        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        """
        Return node left child
        Runtime: O(1)
        """

        return self.items[(self.get_left_child_index(index))]

    def right_child(self, index):
        """
        Return node right child
        Runtime: O(1)
        """

        return self.items[(self.get_right_child_index(index))]

    def parent(self, index):
        """
        Return node parent
        Runtime: O(1)
        """

        return self.items[(self.get_parent_index(index))]

    def swap(self, index_one, index_two):
        """
        Swap elements
        Runtime: O(1)
        """

        temp = self.items[index_one]
        self.items[index_one] = self.items[index_two]
        self.items[index_two] = temp

    def peek(self):
        """
        Return first item in heap
        Runtime: O(1)
        """

        if self.size == 0:
            raise he.EmptyHeapError('Empty Heap')
        return self.items[0]

    def pull(self):
        """
        Remove min item in heap (top). Swap it with bottom right element, then find correct spot for element.
        Runtime: O(log n)
        """

        if self.size == 0:
            raise he.EmptyHeapError('Empty Heap')
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.items.pop()
        self.heapify_down()
        return item

    def add(self, item):
        """
        Add item to heap. Insert at bottom right spot, then move element to correct spot.
        Runtime: O(log n)
        """

        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        """
        Bubble element up to correct spot.
        Runtime: O(log n)
        """

        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        """
        Bubble element down to correct spot.
        Runtime: O(log n)
        """

        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index

    def print_heap(self):
        """
        Print items in heap
        Runtime: O(n)
        """

        for item in self.items:
            print(item)
