def linearsearch(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

arr = [2, 4, 0, 1, 9]
element = 1
result = linearsearch(arr, element)
if result == -1:
    print("Element not found")
else:
    print("Elemnt found at index: ", result)