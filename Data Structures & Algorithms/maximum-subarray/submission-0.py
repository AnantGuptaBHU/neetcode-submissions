class Solution:
    def maxSubArray(self, nums):
        maxi = -1
        l = len(nums)
        su = 0
        for i in range(l):
            su += nums[i]
            maxi = max(maxi, su)
            if su <=0:
                su = 0
        return maxi