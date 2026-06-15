from typing import List
# 超时解
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pre_sum = 0
        nums = sorted(nums)
        for num in nums:
            pre_sum += num
        if pre_sum % 2 == 1:
            return False
        target = pre_sum // 2
        def process(path: int, index: int):
            if path == target:
                return True
            elif index == len(nums):
                return False
            elif path > target:
                return False
            else:
                # qiudehsi process(path, index)
                return process(path+nums[index], index+1) or process(path, index+1)
        return process(0, 0)



# dp解答
# 能AC但是很笨

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        n = len(nums)
        dp = [[False] * (n+1) for _ in range(target+1)]
        for j in range(n+1):
            dp[target][j] = True
        for i in range(target):
            dp[i][n] = False
        for i in range(target-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+nums[j] <= target:
                    dp[i][j] = dp[i+nums[j]][j+1] or dp[i][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]






from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        n = len(nums)
        # 定义：dp[i][j] = 前i个数字，能否凑出和为j
        dp = [[False]*(target+1) for _ in range(n+1)]
        # 基础条件：0个数字凑和为0，是可行的
        dp[0][0] = True
        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(target+1):
                # 不选当前数字：直接继承上一行
                dp[i][j] = dp[i-1][j]
                # 选当前数字：如果j >= num，看减去num后的状态
                if j >= num:
                    dp[i][j] = dp[i][j] or dp[i-1][j - num]
        
        return dp[n][target]