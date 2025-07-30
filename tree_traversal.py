# Tree traversal in Python

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end="")
        inorder(root.right)


def preorder(root):
    if root:
        print(str(root.val) + "->", end="")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end="")


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')

print("\nPreOrder Traversal: ")
preorder(root)

print("\nInOrder Traversal: ")
inorder(root)

print("\nPostOrder Traversal: ")
postorder(root)
