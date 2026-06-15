from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return 
        rows = len(matrix)
        cols = len(matrix[0])
        new_matrix = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for m in range(rows):
                        new_matrix[m][j] = True
                    for n in range(cols):
                        new_matrix[i][n] = True
        for i in range(rows):
            for j in range(cols):
                if new_matrix[i][j]:
                    matrix[i][j] = 0
        return 











class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = {}
        col = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0