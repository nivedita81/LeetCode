def threeSum(nums):
    nums = sorted(nums)
    ans = []
    temp = []
    duplicate = dict()
    sums, target = 0, 0
    n = len(nums)
    for k in range(n):
        i, j = k + 1, n - 1
        while i < j:
            sums = nums[k] + nums[i] + nums[j]
            if sums < target:
                i += 1
            elif sums > target:
                j -= 1
            else:
                temp = [nums[k], nums[i], nums[j]]
                i += 1
                j -= 1
                ans.append(temp)
    unique_combinations_as_tuples = set(tuple(x) for x in ans)
    unique_combinations_as_list = [list(x) for x in unique_combinations_as_tuples]
    return unique_combinations_as_list


arr = [-1, 0, 1, 2, -1, -4]
print("hello")
final = threeSum(arr)
print("hi")
print(final)
