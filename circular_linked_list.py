class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):
        if self.last != None:
            return self.last

        newNode = Node(data)
        self.last = newNode
        self.last.next = self.last

        return self.last

    def addEnd(self, data):
        if self.last == None:
            return self.addToEmpty(data)

        newNode = Node(data)
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

        return self.last

    def addFront(self, data):
        if self.last == None:
            return self.addToEmpty(data)

        newNode = Node(data)
        newNode.next = self.last.next
        self.last.next = newNode

        return self.last

    def addAfter(self, data, item):
        if self.last == None:
            return self.last

        newNode = Node(data)
        temp = self.last.next

        while temp:
            if temp.data == item:
                newNode.next = temp.next
                temp.next = newNode

                if temp == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            temp = temp.next
            if temp == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def traverse(self):
        if self.last == None:
            print("Linked list is empty")
            return

        temp = self.last.next
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.last.next:
                break

    def deleteNode(self, last, item):
        if last == None:
            return

        if last.data == item and last.next == last:
            last = None
            return last

        n = None
        temp = last

        if last.data == item:
            while temp.next != last:
                temp = temp.next
            temp.next = last.next
            last = temp

        while temp.next != last and temp.next.data != item:
            temp = temp.next
        if temp.next.data == item:
            temp.next = temp.next.next
        return last






cll = CircularLinkedList()
last = cll.addToEmpty(10)
last = cll.addEnd(15)
last = cll.addEnd(25)
last = cll.addFront(5)

cll.traverse()

last = cll.addAfter(20,15)
print("\n")
cll.traverse()

last = cll.deleteNode(last, 20)
print("\n")
print(last.data)
print("\n")
cll.traverse()