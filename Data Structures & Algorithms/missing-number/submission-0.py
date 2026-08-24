class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        su = 0
        for num in nums:
            su += num
        l = len(nums)
        return (l*(l+1))//2 - su