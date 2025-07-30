class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("Prev node is not in linked list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, position):   #delete Node by Position

        if self.head == None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                return

        if temp.next is None:
            return

        nxt = temp.next.next
        temp.next = nxt

    def deleteNodeByData(self, key_data):  # delete Node by data
        if self.head == None:
            return

        temp = self.head

        if temp.data == key_data:
            self.head = temp.next
            temp = None
            return

        while temp.next != None:
            if temp.next.data == key_data:
                prev = temp
                nxt = temp.next.next
                prev.next = nxt
                return
            else:
                temp = temp.next

        if temp.next == None:
            return

    def search(self, data):
        curr = self.head
        while curr != None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def sortLinkedList(self, head):
        curr = head
        index = Node(None)

        if curr is None:
            return
        else:
            while curr is not None:
                index = curr.next
                while index is not None:
                    if curr.data > index.data:
                        curr.data, index.data = index.data, curr.data
                    index = index.next
                curr = curr.next



linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)

linked_list.head.next = second
second.next = third

linked_list.insertAtBegin(4)
linked_list.insertAtEnd(10)
linked_list.insertAfter(third, 5)

temp = linked_list.head

while temp != None:
    print(temp.data)
    temp = temp.next
result = linked_list.search(10)
if result:
    print("Element Found")
else:
    print("Element not found")

# linked_list.deleteNode(1)
# linked_list.deleteNodeByData(5)
temp = linked_list.head
print("\nAfter Deleting Node:")
while temp != None:
    print(temp.data)
    temp = temp.next

linked_list.sortLinkedList(linked_list.head)
temp = linked_list.head
print("\nAfter Sorting:")
while temp != None:
    print(temp.data)
    temp = temp.next


