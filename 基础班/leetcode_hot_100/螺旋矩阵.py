from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:  # 处理空矩阵/空行情况
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, up, down = 0, cols - 1, 0, rows - 1
        results = []
        while left <= right and down >= up:
            #向右
            for i in range(left, right + 1):
                results.append(matrix[up][i])
            up += 1
            #向下
            if up <= down:
                for j in range(up, down + 1):
                    results.append(matrix[j][right])
                right -= 1
            if left <= right and down >= up:
                for i in range(right, left - 1, -1):
                    results.append(matrix[down][i])
                down -= 1
            if up <= down and left <= right:
                for j in range(down, up - 1, -1):
                    results.append(matrix[j][left])
                left += 1
        return results