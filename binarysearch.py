from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:  #static function means all objects points to the same function
        # if len(nums) == 0:
        #     return -1
        low, high = 0, len(nums) - 1
        if low == high and nums[low] == target:
            return low
        else:
            return -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    arr = [5, 7, 9, 10, 23, 56, 78]
    n = 9
    s = Solution()
    index = s.search(arr, n)
    print(index)
