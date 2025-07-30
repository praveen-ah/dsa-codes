def binarysearch(arr, x, first, last):
    if last >= first:
        mid = first + (last - first) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binarysearch(arr, x, mid + 1, last)
        else:
            return binarysearch(arr, x, first, mid - 1)
    else:
        return -1


arr = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarysearch(arr, x, 0, len(arr)-1)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)
