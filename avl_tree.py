import sys


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def insert_node(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor:
            if balanceFactor > 1:
                if key < root.left.key:
                    return self.rightRotate(root)
                else:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)
            if balanceFactor < -1:
                if key > root.right.key:
                    return self.leftRotate(root)
                else:
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)
        return root

    def delete_Node(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_Node(root.left, key)
        elif key > root.key:
            root.right = self.delete_Node(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValNode(root.right)
            root.key = temp.key
            root.right = self.delete_Node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def getMinValNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValNode(root.left)

    def leftRotate(self, z):
        y = z.right
        t3 = y.left
        y.left = z
        z.right = t3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        t3 = y.right
        y.left = z
        z.left = t3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printHelper(self, root, indent, last):
        if root != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(root.key)
            self.printHelper(root.left, indent, False)
            self.printHelper(root.right, indent, True)


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_Node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)
