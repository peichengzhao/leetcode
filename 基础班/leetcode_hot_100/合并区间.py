from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        begin = 0
        end = 0
        while begin < len(sorted_intervals):
            begin_value = sorted_intervals[begin][0]
            end_value = sorted_intervals[end][1]
            while end < len(sorted_intervals) - 1 and end_value >= sorted_intervals[end+1][0]:
                end_value = max(end_value, sorted_intervals[end+1][1])
                end += 1
            begin = end + 1
            end += 1
            result.append([begin_value, end_value])
        return result
        

