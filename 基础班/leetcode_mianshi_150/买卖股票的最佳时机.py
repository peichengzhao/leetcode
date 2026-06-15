from typing import List




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pofit = 0
        min_value = prices[0]
        for price in prices:
            max_pofit = max(max_pofit, price - min_value)
            min_value = min(min_value, price)
        return max_pofit


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        temp = 0
        for num in nums:
            temp += num
            result = max(temp, result)
            if temp <=0:
                temp = 0
        return result




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        pre_price = prices[0]
        for price in prices:
            if price > pre_price:
                result += price - pre_price
            pre_price = price
        return result







class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min1, min2 = prices[0], prices[1]
        n = len(prices)
        if len(prices) < 4:
            max_pofit = 0
            min_value = prices[0]
            for price in prices:
                max_pofit = max(max_pofit, price - min_value)
                min_value = min(min_value, price)
            return max_pofit
        dp = [[0,0,0,0] for _ in range(n)]
        dp[0] = [-prices[0], 0, -prices[0], 0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
            dp[i][2] = max(dp[i-1][2], -prices[i] + dp[i-1][1])
            dp[i][3] = max(dp[i-1][3], prices[i] + dp[i-1][2])
        return dp[-1][-1]