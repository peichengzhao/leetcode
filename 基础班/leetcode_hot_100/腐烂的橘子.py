from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        minutes = 0  # 修正拼写：mintues → minutes
        
        # 核心优化：每次循环先记录「当前分钟需要腐烂的坐标」，避免同分钟互相感染
        while True:
            # 第一步：收集当前所有能让新鲜橘子腐烂的坐标（本次分钟的腐烂源）
            rotten_pos = []
            for i in range(rows):
                for j in range(cols):
                    # 找到腐烂橘子，且四周有新鲜橘子，记录坐标
                    if grid[i][j] == 2:
                        if i > 0 and grid[i-1][j] == 1:
                            rotten_pos.append((i-1, j))
                        if i < rows - 1 and grid[i+1][j] == 1:  # 修复：elif → if
                            rotten_pos.append((i+1, j))
                        if j > 0 and grid[i][j-1] == 1:
                            rotten_pos.append((i, j-1))
                        if j < cols - 1 and grid[i][j+1] == 1:
                            rotten_pos.append((i, j+1))
            
            # 第二步：如果没有要腐烂的橘子，终止循环
            if not rotten_pos:
                break
            
            # 第三步：一次性标记本次分钟腐烂的橘子（避免同分钟互相感染）
            for (x, y) in rotten_pos:
                grid[x][y] = 2
            
            # 第四步：只有实际腐烂了橘子，分钟数才+1（修复：多计数问题）
            minutes += 1
        
        # 最后检查：是否还有新鲜橘子，有则返回-1，无则返回分钟数
        if self.has_fresh_orange(grid):
            return -1
        return minutes
    
    # 修复：重新实现正确的判断函数——检查网格中是否有新鲜橘子（1）
    def has_fresh_orange(self, grid: List[List[int]]) -> bool:
        for row in grid:
            if 1 in row:  # 简化遍历，更高效
                return True
        return False