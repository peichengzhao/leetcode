from typing import List, Optional


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[float("inf") for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]





class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if i==0 and j == 0:
                    continue
                elif i==0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j==0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]