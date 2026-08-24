class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # su = 0
        # for num in nums:
        #     su += num
        # l = len(nums)
        # return (l*(l+1))//2 - su
        r = 0
        l = len(nums)
        for i in range(l):
            r = r ^ i ^ nums[i]
        r = r ^ l
        return r