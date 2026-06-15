from typing import List
#超时解

from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def process(index: int, path: int, ):
            if index == len(nums) and path != target:
                return 0
            elif index == len(nums) and path == target:
                return 1
            else:# process(index, path)
                return process(index+1, path+nums[index]) + process(index+1, path-nums[index],)
        return process(0, 0)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * (2 * (abs(target)+1)) for _ in range(n)]
        length = 2 * (abs(target)+1)
        for j in range(target+1):
            dp[n-1][j] = 1 if j == target else 0
        for i in range(n-2, -1, -1):
            for j in range(length):
                dp[i][j] = (dp[i+1][j+nums[i]] if 0 <= j + nums[i] <= target else 0) + (dp[i+1][j-nums[i]] if 0 <= j-nums[i] <= target else 0)
        return dp[0][0]
