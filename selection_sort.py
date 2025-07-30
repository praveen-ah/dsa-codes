def selection(arr):
    for step in range(len(arr)):
        min_idx = step
        for i in range(step+1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        # temp = arr[step]
        # arr[step] = arr[min_idx]
        # arr[min_idx] = temp
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])
    print(arr)


arr = [-2, 45, 0, 11, -9]
selection(arr)