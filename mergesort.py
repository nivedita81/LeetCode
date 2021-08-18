def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)             # recursively splitting the left half until size is 1
        mergeSort(right)            # recursively splitting the right half until size is 1

        i = j = k = 0
        while i < len(left) and j < len(right):     # comparing each value from each small array and placing in arr
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):            # checking if any ele has been left out in the left array
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):           # checking if any ele has been left out in the right array
            arr[k] = right[j]
            j = j + 1
            k = k + 1

    return arr


print(mergeSort([38, 27, 43, 3, 9, 82, 10]))
