class Solution:
    def searching(self, arr, i, j):
        if arr[i] <= arr[j]:
            return i
        mid = (j-i)//2 + i
        if j<=i:
            return i
        if arr[mid] > arr[i] and arr[mid] < arr[j]:
            return i
        if arr[mid] > arr[j]:
            return self.searching(arr, mid+1, j)
        if arr[mid] < arr[i]:
            return self.searching(arr, i, mid)
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
        l = len(nums)
        rp = self.searching(nums, 0, l-1)
        a = self.sea(nums, target, 0, rp-1)
        if a == -1:
            b = self.sea(nums, target, rp, l-1)
            return b
        return a