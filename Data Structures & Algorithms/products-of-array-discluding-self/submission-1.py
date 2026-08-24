class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        pre = [1]*l
        for i in range(1,l):
            pre[i] = pre[i-1] * nums[i-1]
        suf = nums[-1]
        for i in range(l-2, -1, -1):
            pre[i] = pre[i] * suf
            suf = suf*nums[i]
        return pre