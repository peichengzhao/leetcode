from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def process(temp: int):
            if temp == n-1:
                return nums[temp]
            if temp == n:
                return 0
            # 偷当前
            res_1 = nums[temp] + process(temp=temp+2)
            res_2 = process(temp=temp+1)
            return max(res_1 , res_2)
        return process(0)


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        n = len(nums)
        dp[n-1], dp[n] = nums[n-1], 0
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        return dp[0]