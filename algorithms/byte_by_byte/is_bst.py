import sys

sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/data_structures/trees')
from binary_tree import Node

def is_bst(node):
    return is_bst_helper(node, -sys.maxsize + 1, sys.maxsize)

def is_bst_helper(node, min, max):
    if not node:
        return True
    elif node.data < min or node.data > max:
        return False
    else:
        return is_bst_helper(node.left, min, node.data) and is_bst_helper(node.right, node.data + 1, max)

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(8)

    print(is_bst(root))
