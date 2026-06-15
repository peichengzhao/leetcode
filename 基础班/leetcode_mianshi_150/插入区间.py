from typing import List

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval
        
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        res.append([new_start, new_end])
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res