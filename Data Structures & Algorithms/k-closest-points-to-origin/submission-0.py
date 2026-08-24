import heapq
class Solution:
    def kClosest(self, points, k):
        arr = []
        for point in points:
            d = (point[0]**2) + (point[1]**2)
            heapq.heappush(arr, (d, point[0], point[1]))
        res = []
        while len(res) < k:
            ar = heapq.heappop(arr)
            a = ar[1]
            b = ar[2]
            res.append([a,b])
        return res