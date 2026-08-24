"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        a = [intervals[0].end]
        for i in range(1,len(intervals)):
            aa = False
            for j in range(len(a)):
                if a[j] <= intervals[i].start:
                    a[j] = intervals[i].end
                    aa = True
                    break
            if aa == False:
                a.append(intervals[i].end)
        return len(a)
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        return len(heap)


        