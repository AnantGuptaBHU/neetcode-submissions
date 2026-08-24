class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            last_bit = n & 1
            r = r << 1
            r = r | last_bit
            n = n >> 1
        return r