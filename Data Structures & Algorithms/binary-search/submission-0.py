class Solution:
    def sea(self, nums, target, i, j):
        mid = i +(j-i)//2
        if j<i:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.sea(nums, target, i, mid-1)
        else:
            return self.sea(nums, target, mid+1, j)
    def search(self, nums: List[int], target: int) -> int:
        return self.sea(nums, target, 0, len(nums)-1)