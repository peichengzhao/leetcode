class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.process(n)
    def process(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n == 0:
            return 0
        #走一步
        choose_1 = self.process(n-1)
        choose_2 = self.process(n-2)
        return choose_1 + choose_2


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
















class Solution:
    def climbStairs(self, n: int) -> int:
        return self.process(n)
    
    def process(self,n: int):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        #选择走1
        foot_1 = self.process(n-1)
        #选择走2
        foot_2 = self.process(n-2)
        return foot_1 + foot_2

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1], dp[2], dp[3]
        for i in range(len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
