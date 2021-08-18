from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                prod = (nums[i]-1) * (nums[j]-1)
                if prod > max_prod:
                    max_prod = prod

        return max_prod


if __name__ == '__main__':
    inp = [3, 4, 5, 2]
    s = Solution()
    output = s.maxProduct(inp)
    print(output)
