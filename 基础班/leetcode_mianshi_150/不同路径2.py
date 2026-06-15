from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        res = 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == n and m == 1 and obstacleGrid[-1][-1] == 0:
            return 1
        if obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1] == 0:
                dp[i][n-1] = 1
            else:
                break
        for j in range(n-2, -1, -1):
            if obstacleGrid[m-1][j] == 0:
                dp[m-1][j] = 1
            else:
                break
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


# 节省空间的写法
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])  # 1. 取网格的【列数】
        f = [0] * (n + 1)         # 2. 开一个一维数组，长度=列数+1（关键巧思！）
        f[1] = 1                  # 3. 起点初始化：最开始只有1条路径（站在起点）
        
        # 4. 逐行遍历整个网格（从上到下一行一行走）
        for row in obstacleGrid:
            # 5. 逐列遍历当前行（从左到右一列一列走）
            for j, x in enumerate(row):
                if x == 0:        # 6. 当前格子无障碍：路径数 = 上边 + 左边
                    f[j + 1] += f[j]
                else:             # 7. 当前格子有障碍：路径数直接归零
                    f[j + 1] = 0
        return f[n]               # 8. 最后一个位置就是答案