from typing import List

#超时了
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        prepare_list = []
        cur = 1
        while cur * cur <= n:
            prepare_list.append(cur*cur)
            cur += 1
        return self.process(prepare_list, 0, n)

    def process(self, prepare_list: List[int], index: int, rest: int):
        if rest == 0:
            return 0
        if index == len(prepare_list):
            return float('inf')
        number = prepare_list[index]
        #不选当前数字
        p1 = self.process(prepare_list, index + 1, rest)
        #选择当前数字
        p2 = float('inf')
        p2_next = self.process(prepare_list, index, rest - number)
        if p2_next != float('inf'):
            p2 = p2_next + 1
        return min(p1, p2)

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        prepare_list = []
        cur = 1
        while cur * cur <= n:
            prepare_list.append(cur*cur)
            cur += 1
        length = len(prepare_list)
        help_list = [[0] * (n+1) for _ in range(length + 1)]
        for i in range(length):
            help_list[i][0] = 0
        for j in range(n+1):
            number = prepare_list[i]
            help_list[length][j] = float('inf')
        for i in range(length-1, -1 ,-1):
            for j in range(1, n+1):
                p1 = help_list[i+1][j]
                p2 = float('inf')
                pw_next = help_list[i][j-number]
                if pw_next != float('inf'):
                    p2 = pw_next + 1
                help_list[i][j] = min(p1, p2)
        return help_list[0][n]









#dp[i] = 凑成数字 i 所需的最少完全平方数数量

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            k=1
            while k * k <= i:
                dp[i] = min(dp[i], dp[i - k*k] + 1)
                k += 1
        return dp[n]


















class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] =1 
        for i in range(1, n):
            for j in range(1, amount+1):
                temp = coins[i]
                #如果不使用使用当前temp
                dp[i][j] = dp[i-1][j]
                if j >= temp:
                    dp[i][j] += dp[i][j-temp]
        return dp[-1][-1]















