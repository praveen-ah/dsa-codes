class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


deque = Deque()
deque.addFront(5)
deque.addFront(10)
print(deque.items)

deque.addRear(15)
deque.addRear(20)
print(deque.items)

deque.removeFront()
deque.removeRear()
print(deque.items)

print(deque.isEmpty())
print(deque.size())
