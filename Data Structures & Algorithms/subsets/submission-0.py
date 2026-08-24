class Solution:
    def backtrack(self, nums, i, arr, res):
        if i == len(nums):
            res.append(arr.copy())
            return
        self.backtrack(nums,i + 1, arr, res)
        arr.append(nums[i])
        self.backtrack(nums,i + 1, arr, res)
        arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]
        # for num in nums:
        #     arr = []
        #     for i in range(len(res)):
        #         arr.append(res[i]+[num])
        #     res += arr
        # return res
        res = []
        self.backtrack(nums, 0, [], res)
        return res
