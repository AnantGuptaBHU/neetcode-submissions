class Solution:
    def backtrack(self, nums, target, i, arr, res):
        if target < 0:
            return
        if target == 0:
                res.append(arr.copy())
                return
        if i == len(nums):     
            return
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        self.backtrack(nums, target, j, arr, res)
        arr.append(nums[i])
        self.backtrack(nums, target-nums[i], i+1, arr, res)
        arr.pop()
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.backtrack(candidates, target, 0, [], res)
        return res