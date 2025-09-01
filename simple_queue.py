class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def enqueue(self, data):
        if self.tail == self.size - 1:
            print("Queue is Full")

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data

        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("Queue is empty")

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp

        else:
            temp = self.queue[self.head]
            self.head = self.head + 1
            return temp

    def printqueue(self):
        if self.head == -1:
            print("Queue is empty")
        else:
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

q.printqueue()
q.dequeue()

print("\nAfter Dequeue: ")
q.printqueue()
