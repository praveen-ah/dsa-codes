# Binary Tree in Python

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def traversePreOrder(self):
        print(self.val, end=" ")
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=" ")
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=" ")


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')

print("\nPreOrder Traversal: ")
root.traversePreOrder()

print("\nInOrder Traversal: ")
root.traverseInOrder()

print("\nPostOrder Traversal: ")
root.traversePostOrder()
