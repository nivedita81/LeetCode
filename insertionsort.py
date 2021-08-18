def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        while arr[i-1] > temp and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1
    return arr


print(insertionSort([6, 8, 1, 4, 5, 3, 7, 2]))
