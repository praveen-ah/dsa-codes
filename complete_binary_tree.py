# Checking if a binary tree is a complete binary tree in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


def is_complete(root, index, nodesCount):
    if root is None:
        return True

    if index >= nodesCount:
        return False

    return (is_complete(root.left, 2*index+1, nodesCount)) and (is_complete(root.right, 2*index+2, nodesCount))


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)

nodesCount = count_nodes(root)
index = 0

if is_complete(root, index, nodesCount):
    print("Yes!, It is Complete Binary Tree")
else:
    print("No, Not")
