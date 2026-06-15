from typing import List, Optional

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        result = 1
        for j in range(len(nums)-2, -1):
            if nums[j] < nums[j+1]:
                dp[j] = dp[j+1] + 1
                result = max(dp[j], result)
        return result




class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        result = 1 
        for i in range(0, len(dp)):
            result = max(result, dp[i])
        return result



# Dynamic programming + Dichotomy.
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res
