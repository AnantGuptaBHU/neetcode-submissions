class Solution:
    def search(self, arr, i, j):
        if arr[i] <= arr[j]:
            return arr[i]
        mid = (j-i)//2 + i
        if j<=i:
            return arr[i]
        if arr[mid] > arr[i] and arr[mid] < arr[j]:
            return arr[i]
        if arr[mid] > arr[j]:
            return self.search(arr, mid+1, j)
        if arr[mid] < arr[i]:
            return self.search(arr, i, mid)
        
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        return self.search(nums, 0, l-1)