from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit








class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        low = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - low
            if profit > max_profit:
                max_profit = profit
            if prices[i] < low:
                low = prices[i]
        return max_profit