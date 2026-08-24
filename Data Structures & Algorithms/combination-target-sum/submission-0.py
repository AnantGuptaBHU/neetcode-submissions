class Solution:
    def backtrack(self, nums, target, i, arr, res):
        if target < 0:
            return
        if target == 0:
                res.append(arr.copy())
                return
        if i == len(nums):     
            return
        self.backtrack(nums, target, i + 1, arr, res)
        arr.append(nums[i])
        self.backtrack(nums, target-nums[i], i, arr, res)
        arr.pop()
    def combinationSum(self, nums, target) -> List[List[int]]:
        res = []
        self.backtrack(nums, target, 0, [], res)
        return res