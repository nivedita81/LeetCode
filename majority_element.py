from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #
        # count = [0] * len(nums)
        # for i in range(len(nums)):
        #     count[nums[i]] = count[nums[i]] + 1
        #     if count[nums[i]] > len(nums) // 2:
        #         return nums[i]
        #
        # return None
        maj_ele_index = 0
        count = 1
        ele_count = 0

        for i in range(len(nums)):
            if nums[maj_ele_index] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_ele_index = i
                count = 1
        maj_ele = nums[maj_ele_index]

        for i in range(len(nums)):
            if nums[i] == maj_ele:
                ele_count += 1
        if ele_count > len(nums) / 2:
            return maj_ele
        else:
            return None


if __name__ == '__main__':
    s = Solution()
    # input_arr = [3, 2, 3]
    input_arr = [2, 2, 1, 1, 1, 2, 2]
    output = s.majorityElement(input_arr)
    print(output)
