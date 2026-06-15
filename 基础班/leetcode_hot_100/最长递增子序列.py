from calendar import LocaleTextCalendar
from typing import List


from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            litele = i
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    litele = j
                    break
            dp[i] = dp[litele] + 1 if litele != i else 1
        max_length = 1
        for k in range(len(dp)):
            if dp[k] > max_length:
                max_length = dp[k]
        return max_length -1 


        