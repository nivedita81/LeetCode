from typing import List


def findinfpoint(nums: List[int]) -> int:
    n = len(nums)
    low, high = 0, n - 1
    while low < high:
        mid = low + (high - low) // 2
        if (nums[mid] > nums[mid + 1]) and mid < n - 1:
            return mid
        if (nums[mid - 1] > nums[mid]) and mid > 0:
            return mid - 1
        if nums[low] >= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


class Solution:
    def findMin(self, nums: List[int]) -> int:

        inf_point = findinfpoint(nums)

        if inf_point == -1:
            return nums[0]
        else:
            return nums[inf_point + 1]


if __name__ == '__main__':
    arr = [1,2,3]
    s = Solution()
    s.findMin(arr)
    print(s.findMin(arr))
