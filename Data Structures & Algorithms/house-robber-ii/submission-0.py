class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[-1], nums[0])
        i1 = max(nums[0], nums[1])
        i2 = nums[0]
        for i in range(2, len(nums)):
            curr = i2 + nums[i]
            skip = i1
            i1 = max(curr, skip)
            i2 = skip
        a = i2
        i1 = max(nums[2], nums[1])
        i2 = nums[1]
        for i in range(3, len(nums)):
            curr = i2 + nums[i]
            skip = i1
            i1 = max(curr, skip)
            i2 = skip
        b = i1
        return max(a, b)
