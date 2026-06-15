
from typing import List
#超时解答
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        min_sum = float("inf")
        return self.process(grid, 0, 0, grid[0][0])

    def process(self, grid: List[List[int]], row: int, col: int, temp_sum: int):
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return temp_sum
        #往右走
        right_sum = self.process(grid, row, col+1, temp_sum + grid[row][col+1] ) if col < len(grid[0]) - 1 else -1
        down_sum = self.process(grid, row+1, col, temp_sum + grid[row+1][col]) if row < len(grid) - 1 else -1
        if right_sum != -1 and down_sum != -1:
            return min(right_sum, down_sum)
        return right_sum if right_sum != -1 else down_sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        temp = 0
        for i in range(len(grid[0])):
            dp[0][i] = temp + grid[0][i]
            temp += grid[0][i]
        temp = 0
        for j in range(len(grid)):
            dp[j][0] = temp + grid[j][0]
            temp += grid[j][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
               dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[len(grid) - 1][len(grid[0]) - 1]