#岛屿问题
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        col = len(grid)
        row = len(grid[0])
        number = 0
        for i in range(col):
            for j in range(row):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    number += 1
        return number

    
    def dfs(self, grid: List[List[str]], i: int, j: int):
        if i<0 or i >= len(grid) or j<0 or j >=len(grid[0]):
            return 
        if grid[i][j] == "0":
            return  
        else:
            grid[i][j] = "0"
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
        return 
