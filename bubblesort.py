class BSort:
    def bubbleSort(self, arr):
        for i in range(0, len(arr)):
            for k in range(len(arr)-1, i, -1):
                if arr[k] < arr[k-1]:
                    arr[k], arr[k-1] = arr[k-1], arr[k]
            # for k in range(0, len(arr)):
            #     if (k < len(arr) - 1) and (arr[k] > arr[k+1]):
            #         arr[k], arr[k+1] = arr[k+1], arr[k]
        return arr


if __name__ == '__main__':
    sort = BSort()
    result = []
    array = [53, 24, 93, 12, 27, 32, 45, 56, 22]
    result = sort.bubbleSort(array)
    print(result)
