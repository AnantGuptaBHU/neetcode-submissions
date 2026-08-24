class Solution:
    def backtrack(self, i, arr, res):
        if i == len(arr):
            res.append(arr.copy())
            return
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            self.backtrack(i + 1, arr, res)
            arr[i], arr[j] = arr[j], arr[i]
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, nums, res)
        return res