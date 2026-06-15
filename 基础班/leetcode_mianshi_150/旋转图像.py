from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        up, down = 0, n-1
        while up <= down:
            length = down - up
            #上到左边
            for i in range(length):
                temp = matrix[up+i][up]
                matrix[up+i][up] = matrix[down][up+i]
                matrix[down][up+i] = matrix[down-i][down]
                matrix[down-i][down] = matrix[up][down-i]
                matrix[up][down-i] = temp
            up += 1
            down -= 1
        return 
