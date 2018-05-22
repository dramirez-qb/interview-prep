import sys

sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/data_structures/trees')
from binary_tree import Node
from collections import deque

def level_order(root):
    if not root:
        return None
    nodes = deque([])
    nodes.append(root)

    while nodes:
        curr_node = nodes.popleft()
        print(curr_node.data, end=' ')
        if curr_node.left:
            nodes.append(curr_node.left)
        if curr_node.right:
            nodes.append(curr_node.right)


if __name__ == '__main__':
    tree = Node(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)

    level_order(tree)
