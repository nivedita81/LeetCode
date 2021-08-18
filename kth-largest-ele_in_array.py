import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for ele in nums:
            if len(heap) > k:
                heapq.heappop(heap)
            heapq.heappush(heap, ele)
        if len(heap) > k:
            heapq.heappop(heap)
        return heap[0]


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 6, 4]
    ans = Solution().findKthLargest(arr, 2)
    print(ans)
