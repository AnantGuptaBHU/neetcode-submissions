class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        keys = set(nums)
        maxi = 0
        for num in keys:
            if num - 1 not in keys:
                r = 1
                while num + r in keys:
                    r += 1
                maxi = max(maxi, r)
        return maxi