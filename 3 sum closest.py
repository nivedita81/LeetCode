import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_sum = 0
        min_dist = sys.maxsize
        
        if(n<3):
            return 0
        
        for i in range(0,n):
            k = n-1
            for j in range(i+1,k):
                curr_sum = nums[i] + nums[j] + nums[k]
                
                curr_dist = abs(target-curr_sum)
                if(curr_dist < min_dist):
                    min_dist = curr_dist
                    min_sum = curr_sum
                    
                if(curr_sum < target):
                    j +=1
                elif(curr_sum > target):
                    k -=1
                else:
                    j+=1
                    k-=1
        return min_sum
        