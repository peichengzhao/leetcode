from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        number = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j, {}, rows, cols)
                    number += 1
        return number
    

    def dfs(self, grid: List[List[str]], i: int, j: int, hash_map: dict, rows: int, cols: int):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
            return 
        grid[i][j] = "0"
        self.dfs(grid, i+1, j, hash_map, rows, cols)
        self.dfs(grid, i-1, j, hash_map, rows, cols)
        self.dfs(grid, i, j+1, hash_map, rows, cols)
        self.dfs(grid, i, j-1, hash_map, rows, cols)
        return