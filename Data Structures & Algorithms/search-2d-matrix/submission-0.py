class Solution:
    def searchRow(self, nums, target, i, j):
        mid = i +(j-i)//2
        if j<i:
            return -1
        if nums[mid][0] <= target and (mid == len(nums)-1 or target < nums[mid+1][0]):
            return mid
        elif nums[mid][0] > target:
            return self.searchRow(nums, target, i, mid-1)
        else:
            return self.searchRow(nums, target, mid+1, j)
    def searchColumn(self, nums, target, i, j):
        mid = i +(j-i)//2
        if j<i:
            return False
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.searchColumn(nums, target, i, mid-1)
        else:
            return self.searchColumn(nums, target, mid+1, j)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.searchRow(matrix, target, 0, len(matrix)-1)
        print(row)
        return False if row == -1 else self.searchColumn(matrix[row], target, 0, len(matrix[row])-1)
        