class Solution:
    def jump(self, nums):
        max_reach = 0
        l = len(nums)
        count = 0
        curr = 0 
        for i in range(l-1):
            max_reach = max(max_reach, i + nums[i])
            if i == curr:
                count+=1
                curr = max_reach
        return count