from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def process(up: int, down: int):
            if up >= down:
                return
            length = down - up
            for i in range(length):
                #暂时存放上 数据
                temp = matrix[up][up+i]
                #左边到上边
                matrix[up][up+i] = matrix[down-i][up]
                #下边到左边
                matrix[down-i][up] = matrix[down][down-i]
                #右边到下边
                matrix[down][down-i] = matrix[up+i][down]
                #上边到右边
                matrix[up+i][down] = temp
            process(up+1, down-1)
        process(0, n-1)