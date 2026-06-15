from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or min(coins) > amount:
            return -1
        if amount == 0:
            return 0
        min_count = [10000]
        path = []
        rest = amount
        self.process(coins, rest, 0, 0, min_count)
        return min_count[0] if min_count[0] != 10000 else -1
    

    def process(self, coins: List[int], rest: int, index: int, current_count: int, min_count: List[int]):
        if rest == 0:
            if current_count < min_count[0]:
                min_count[0] = current_count
            return 
        if rest < 0 or index == len(coins):
            return
        temp = coins[index]
        count = rest // temp
        for i in range(count + 1):
            self.process(coins, rest - (i * temp), index+1, current_count+i, min_count)
        return 



from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or min(coins) > amount:
            return -1
        dp = [float('inf')] * ((amount) + 1)
        dp = dp * len(coins)
        for i in range(len(coins) + 1):
            dp[0][i] == 0
        for i in range(1, amount+1):
            for j in range(len(coins) + 1):
                dp[j][i] =
 















