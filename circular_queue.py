class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("Circular queue is full")

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data

        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("Queue is Empty")

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp

        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCqueue(self):
        if self.head == -1:
            print("Queue is Empty")

        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
        # else:
        #     for i in self.queue:
        #         print(i, end=" ")


cqueue = CircularQueue(5)
cqueue.enqueue(1)
cqueue.enqueue(2)
cqueue.enqueue(3)
cqueue.enqueue(4)
cqueue.enqueue(5)
cqueue.enqueue(6)
cqueue.printCqueue()

cqueue.dequeue()
print("\nAfter Dequeue:")
cqueue.printCqueue()

cqueue.dequeue()
print("\nAfter Dequeue:")
cqueue.printCqueue()

cqueue.enqueue(6)
print("\nAfter Enqueue:")
cqueue.printCqueue()

cqueue.enqueue(7)
print("\nAfter Enqueue:")
cqueue.printCqueue()

cqueue.enqueue(8)
