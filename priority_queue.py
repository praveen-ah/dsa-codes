
def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, i)


def insert(arr, num):
    if len(arr) == 0:
        arr.append(num)
    else:
        arr.append(num)
        for i in range(len(arr)//2, -1, -1):
            heapify(arr, len(arr), i)


def deleteNode(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            break

    arr[i], arr[-1] = arr[-1], arr[i]
    arr.pop()

    for i in range(len(arr)//2, -1, -1):
        heapify(arr, len(arr), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
