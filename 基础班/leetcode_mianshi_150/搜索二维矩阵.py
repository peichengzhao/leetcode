from typing import List, Optional

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        # find_hang
        hang = row
        for i in range(row):
            if matrix[i][col-1] >= target:
                hang = i
                break
        if hang == row: return False
        for j in range(col):
            if matrix[hang][j] == target:
                return True
        return False