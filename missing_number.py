from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if not nums:
            return None
        else:
            xor_val = 0
            xor_ind = 0
            for j in range(len(nums) + 1):
                xor_ind = xor_ind ^ j

            for i in range(len(nums)):
                xor_val = xor_val ^ nums[i]

        return xor_val ^ xor_ind


if __name__ == '__main__':
    s = Solution()
    arr = [3, 0, 1]
    ans = s.missingNumber(arr)
    print(ans)
