from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for _ in range(len(nums))]
        length = len(nums)
        dp[length-1][length-1] = nums[length-1]
        max_value = float("-inf")
        for i in range(length-2, 0, -1):
            dp[i][length-1] = dp[i+1][length-1] * nums[i]
            dp[i][i] = nums[i]
        for j in range(length-2, 0, -1):
            for i in range(j-1, -1, -1):
                dp[i][j] = dp[i+1][j] * nums[i]
                max_value = max(max_value, dp[i][j])
        return max_value



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return []
        result = float("-inf")
        max_pre = min_pre = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_pre, min_pre = min_pre, max_pre
            max_pre = max(max_pre * num, num)
            min_pre = min(min_pre * num, num)
            result = max(result, max_pre)
        return result

