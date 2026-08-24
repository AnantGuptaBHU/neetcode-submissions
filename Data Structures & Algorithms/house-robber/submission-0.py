class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i1 = max(nums[0], nums[1])
        i2 = nums[0]
        for i in range(2, len(nums)):
            curr = i2 + nums[i]
            skip = i1
            i1 = max(curr, skip)
            i2 = skip
        return i1
