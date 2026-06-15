from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        buy = [float("-inf")] * k
        sell = [float("-inf")] * k
        for price in prices:
            for i in range(k):
                if i >0:
                    buy[i] = max(buy[i], -price + sell[i-1])
                else:
                    buy[i] = max(buy[i], -price)
                sell[i] = max(sell[i], buy[i]+price)
        return sell[-1]