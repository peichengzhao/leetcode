from typing import List


# 空间复杂度是o m  m是元素个数

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        help_list = triangle.copy()
        hang = len(triangle)
        # 从倒数第二行开始
        for j in range(hang-2, -1, -1):
            cur_count = len(triangle[j])
            for i in range(cur_count):
                help_list[j][i] = help_list[j][i] + min(help_list[j+1][i], help_list[j+1][i+1])
        return help_list[0][0]