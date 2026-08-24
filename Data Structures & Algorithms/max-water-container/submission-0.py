class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxi = 0
        i = 0
        j = len(h)-1
        while i<j:
            maxi = max(maxi, (j-i)*min(h[i], h[j]))
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return maxi
        