class Solution:
    def countBits(self, n: int) -> List[int]:
        r = [0] * (n + 1)
        for i in range(1, n+1):
            r[i] = r[(i & (i-1))] + 1
        return r
        