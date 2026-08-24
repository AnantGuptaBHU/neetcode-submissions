class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while i<j:
            a = nums[i]+nums[j]
            if a < target:
                i+=1
            elif a> target:
                j-=1
            else:
                return [i+1,j+1]
        