def binarysearch(arr, x):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1

    print(arr)

arr = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarysearch(arr, x)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)

