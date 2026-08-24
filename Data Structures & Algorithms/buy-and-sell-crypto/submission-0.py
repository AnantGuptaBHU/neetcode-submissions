class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        a = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > a:
                maxi = max(maxi, prices[i] - a)
            else:
                a = prices[i]
        return maxi