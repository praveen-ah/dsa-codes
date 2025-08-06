class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def calculateDepth(root):
    if root is None:
        return 0

    leftDepth = calculateDepth(root.left)
    rightDepth = calculateDepth(root.right)

    return max(leftDepth, rightDepth) + 1


def isPerfectBinaryTree(root, depth, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return depth == level + 1

    if root.left is None or root.right is None:
        return False

    return isPerfectBinaryTree(root.left, depth, level+1) and isPerfectBinaryTree(root.right, depth, level+1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

if isPerfectBinaryTree(root, calculateDepth(root)):
    print("Yes, Perfect Binary Tree!!")
else:
    print("No, Not!!")
