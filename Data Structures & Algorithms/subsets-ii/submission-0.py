class Solution:
    def backtrack(self, nums, i, arr, res):
        if i == len(nums):
            res.append(arr.copy())
            return
        arr.append(nums[i])
        self.backtrack(nums, i + 1, arr, res)
        arr.pop()
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        self.backtrack(nums, j, arr, res)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)
        return res