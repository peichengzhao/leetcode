
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rows, cols = len(matrix), len(matrix[0])
        right = rows * cols - 1
        while left <= right:
            middle = (left + right) // 2
            row = middle // cols
            col = middle % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # find行
        row = 0
        if matrix[len(matrix)-1][len(matrix[0])-1] < target or matrix[0][0] > target:
            return False

        for i in range(len(matrix)):
            if matrix[i][len(matrix[0])-1] >= target:
                row = i
                break
        for j in range(len(matrix[0])):
            if matrix[row][j] == target:
                return True
        return False

