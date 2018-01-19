class Node:
    """Node in binary search tree"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Insert node into binary tree
        Runtime: O(log n)
        """

        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        """
        Binary tree contains value?
        Runtime: O(log n)
        """

        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def in_order(self):
        """
        Prints nodes in binary tree (left children, root, right children)
        Runtime: O(n)
        """

        if self.left is not None:
            self.left.in_order()
        print(self.data)
        if self.right is not None:
            self.right.in_order()

    def pre_order(self):
        """
        Prints nodes in binary tree (root, left children, right children)
        Runtime: O(n)
        """

        print(self.data)
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def post_order(self):
        """
        Prints nodes in binary tree (left children, right children, root)
        Runtime: O(n)
        """
        
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        print(self.data)
