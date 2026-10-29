class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l = len(piles)
        left = 1
        right = maxPile
        while left < right:
            mid = (right + left) // 2
            count = 0
            for j in range(0,l):
                count += piles[j] // mid
                if piles[j] % mid != 0:
                    count += 1
            if count <= h:
                right = mid
            else:
                left = mid + 1
        return left