from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return []

        n1_ptr, n2_ptr = 0, 0

        while n1_ptr < len(nums1) and n2_ptr < len(nums2) and n1_ptr != m:
            if nums1[n1_ptr] <= nums2[n2_ptr]:
                n1_ptr = n1_ptr + 1
            else:
                nums1[n1_ptr], nums2[n2_ptr] = nums2[n2_ptr], nums1[n1_ptr]
                n1_ptr = n1_ptr + 1
                n2_ptr = n2_ptr + 1

        if n1_ptr == m:
            for i in range(len(nums2)):
                nums1[m] = nums2[i]
                m = m + 1

        print(nums1)


if __name__ == '__main__':
    sol = Solution()
    # arr1 = [4, 0, 0, 0, 0, 0]
    # a1_m = 1
    # arr2 = [1, 2, 3, 5, 6]
    # a2_n = 5
    arr1 = [4, 5, 6, 0, 0, 0]
    a1_m = 3
    arr2 = [1, 2, 3]
    a2_n = 3
    sol.merge(arr1, a1_m, arr2, a2_n)
