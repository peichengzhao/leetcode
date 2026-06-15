from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        result = []
        index = 0
        intervals = sorted(intervals, key = lambda x: x[0])
        while index < len(intervals):
            left = intervals[index][0]
            right = intervals[index][1]
            temp = index+1
            while temp < len(intervals) and right >= intervals[temp][0]:
                right = max(intervals[temp][1], right)
                temp += 1
            result.append([left, right])
            index = temp
        return result