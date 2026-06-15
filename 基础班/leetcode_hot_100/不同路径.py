class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        return self.walk_ways(1, 1, m, n)

    
    def walk_ways(self, hang: int, lie: int, m: int, n: int) -> int:
        if hang == m-1 and lie == n:
            return 1
        if hang == m and lie == n-1:
            return 1
        # 选择向右走
        right_ways = self.walk_ways(hang, lie+1, m, n)
        # 选择向下走
        down_ways = self.walk_ways(hang+1, lie, m, n)
        return right_ways + down_ways



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n ==0:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1 ,-1):
                dp[j][i] = dp[j+1][i] + dp[j][i+1]
        return dp[0][0]
