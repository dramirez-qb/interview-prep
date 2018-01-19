class ResizableArray:
    """
    Resizable array implementation. If array is reaching capacity, double its size.
    """

    def __init__(self):
        self.items = []
        self.size = 0

    def get(self, index):
        """
        Return value at given index.
        Runtime: O(1)
        """

        try:
            return self.items[index]
        except IndexError:
            print('Invalid index:', index)

    def set(self, index, item):
        """
        Set value at given index.
        Runtime: O(1)
        """

        try:
            self.items[index] = item
        except IndexError:
            print('Invalid index:', index)

    def ensure_extra_capacity(self):
        """
        If array has reached capacity, double its size and copy elements over to new array.
        Runtime: O(n)
        """

        if self.size == len(self.items):
            copy = self.items[:]
            self.items = copy

    def append(self, item):
        """
        Add element to end of array.
        Runtime: O(1)
        """

        self.ensure_extra_capacity()
        self.items[self.size] = item
        self.size += 1

    def pop(self):
        """
        Delete last element of array.
        Runtime: O(1)
        """

        try:
            del self.items[-1]
        except IndexError:
            print('Invalid index')
