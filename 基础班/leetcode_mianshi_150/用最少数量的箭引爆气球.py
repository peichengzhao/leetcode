from typing import List
"""
射气球 = 找最少的点覆盖所有区间
排序：按区间右端点升序
规则：
第一箭射第一个区间右端
后面气球起点超出箭位 → 换新箭，射当前右端"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        last_arrow = points[0][1]
        res = 1
        for i in range(1, len(points)):
            begin, end = points[i][0], points[i][1]
            if begin > last_arrow:
                res += 1
                last_arrow = end
        return res