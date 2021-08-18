from typing import List


def findfirstpos(nums: List[int], n: int, target: int) -> int:
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            if mid==0 or nums[mid - 1] < nums[mid]:
                return mid
            else:
                high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def findlastpos(nums: List[int], n: int, target: int) -> int:
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            if mid ==n-1 or nums[mid + 1] > nums[mid]:
                return mid
            else:
                low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans = []
        n = len(nums)
        if n == 0:
            ans = [-1, -1]
            return ans
        if n == 1 and nums[0] == target:
            ans = [0, 0]
            return ans
        elif n == 1 and nums[0] != target:
            ans = [-1, -1]
            return ans

        first_pos = findfirstpos(nums, n, target)
        last_pos = findlastpos(nums, n, target)

        ans = [first_pos, last_pos]
        return ans


if __name__ == '__main__':
    arr = [2, 2]
    target = 2
    s = Solution()
    print(s.searchRange(arr, target))
