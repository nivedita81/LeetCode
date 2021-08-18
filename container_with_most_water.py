from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # another method
        # area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = max(area, min(height[i], height[j])*(j-i))
        # return area

        area = 0
        first, last = 0, len(height) - 1
        while first < last:
            area = max(area, min(height[first], height[last]) * (last - first))

            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return area


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = Solution().maxArea(arr)
    print(ans)
