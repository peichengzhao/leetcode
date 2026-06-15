from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #以某一个点为顶点 组成的最大正方形是多大
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        max_length = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    if i ==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_length = max(max_length, dp[i][j])
        return max_length * max_length