from functools import lru_cache
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        result = float("inf")
        length = len(coins)
        @lru_cache
        def process(index: int, temp: int, number: int):
            nonlocal result, length
            if temp == amount:
                result = min(result, number)
                return 
            if index >= length or temp > amount or number >= result:
                return 
            temp_value = coins[index]
            count = (amount - temp) // temp_value
            for i in range(count, -1, -1):
                process(index+1, temp+(i * temp_value), number+i)
        process(0, 0, 0)
        return result if result!=float("inf") else -1




from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_val = amount + 1
        dp = [max_val] * (amount + 1)
        dp[0] = 0 
        #使用动态规划  DP数组
        dp[0] = 0 # 0块钱需要0个硬币
        for i in range(1, amount+1):
            for coin in coins:
                if coin <=i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != max_val else -1