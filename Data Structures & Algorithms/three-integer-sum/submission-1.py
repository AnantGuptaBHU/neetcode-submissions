class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        r=[]
        k=0
        while k < (l-2):
            j = l-1
            i = k+1
            target = -nums[k]
            while i<j:
                a = nums[i]+nums[j]
                if a < target:
                    i+=1
                elif a> target:
                    j-=1
                else:
                    r.append([nums[i], nums[j], nums[k]])
                    while i < l-1 and nums[i] == nums[i+1]:
                        i+=1
                    while j>1 and nums[j] == nums[j-1]:
                        j-=1
                    i+=1
                    j-=1
            while k<l-1 and nums[k] == nums[k+1]:
                k+=1
            k+=1
        return r