import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for stone in stones:
            heapq.heappush(arr, (-1)*stone)
        while len(arr) > 1:
            a = heapq.heappop(arr)*(-1)
            b = heapq.heappop(arr)*(-1)
            if a == b:
                c = 0
            else:
                c = (-1)*abs(a-b)
                heapq.heappush(arr, c)
        return arr[0]*(-1) if arr else 0
