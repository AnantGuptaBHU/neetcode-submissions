class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        for item in d:
            freq[d[item]].append(item)
        r = []
        for i in range(n,-1, -1):
            for c in freq[i]:
                k-=1
                r.append(c)
                if k == 0:
                    return r