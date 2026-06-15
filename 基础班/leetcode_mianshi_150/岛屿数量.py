from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0" 
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count







from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))
        count = sum(1 for i in range(m) for j in range(n) if grid[i][j] == "1")#陆地数量
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
                count -= 1

        dirs = [(1,0), (0,1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for dx, dy in dirs:
                        ni, nj = i+dx, j+dy
                        if 0<=ni<m and 0<=nj<n and grid[ni][nj] == "1":
                            union(i*n+j, ni*n+nj)
        return count






