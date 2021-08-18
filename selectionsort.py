def selectionSort(arr):
    for i in range(0, len(arr)):
        minVal = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minVal]:
                minVal = j
        arr[i], arr[minVal] = arr[minVal], arr[i]
    return arr


print(selectionSort([6, 8, 1, 4, 5, 3, 7, 2]))
