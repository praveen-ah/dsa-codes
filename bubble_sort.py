def bubble(arr):
    for i in range(len(arr)):
        isSorted = False
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                isSorted = True
        if not isSorted:
            break
    print(arr)

arr = [-2, 45, 0, 11, -9]
bubble(arr)