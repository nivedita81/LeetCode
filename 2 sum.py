def twoSum(nums, target):
    result = []

    input = dict()

    for index, val in enumerate(nums):
        input[val] = index

    for index, val in enumerate(nums):
        comp = input.get(target - val)
        if comp is not None and comp != index:
            if index < comp:
                temp = [index, comp]
            else:
                temp = [comp, index]
        result.extend(temp)
        break

        input[val] = index

    return result


arr = [2, 7, 11, 15]
ans = twoSum(arr, 9)
print(ans)
