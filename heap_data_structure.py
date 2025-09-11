def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(arr, num):
    arr.append(num)
    current = len(arr) - 1
    while current > 0:
        parent = (current-1) // 2
        if arr[current] > arr[parent]:
            arr[current], arr[parent] = arr[parent], arr[current]
            current = parent
        else:
            break


def deleteNode(arr, num):
    i = 0
    for i in range(len(arr)):
        if arr[i] == num:
            break

    arr[i], arr[-1] = arr[-1], arr[i]
    arr.pop()

    if i < len(arr):
        heapify(arr, len(arr), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)
print("Max-Heap array:", arr)

deleteNode(arr, 4)
print("After deleting an element:", arr)

insert(arr, 4)
print("Max-Heap array:", arr)

deleteNode(arr, 9)
print("After deleting an element:", arr)
