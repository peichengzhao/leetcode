from typing import List


# 暴力解法
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return self.process(nums, 0)
    
    def process(self, nums: List[int], index: int):
        if index == len(nums):
            return 0
        #打劫当下
        if index + 2 < len(nums):
            p1 = nums[index] + self.process(nums, index + 2)
        else:
            p1 = nums[index]
        if index + 1 < len(nums):
            p2 = self.process(nums, index + 1)
        else:
            p2 = 0
        return max(p1, p2)

# 使用哈希表

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        hash_map = {}
        hash_map[len(nums)] = 0
        hash_map[len(nums) - 1] = nums[len(nums) - 1]
        hash_map[len(nums) - 2] = max(nums[len(nums) - 1], nums[len(nums) - 2])
        for i in range(len(nums) - 3, -1 ,-1):
            hash_map[i] = max((nums[i] + hash_map[i+2]), (hash_map[i+1]))
        return hash_map[0]
            

# 使用动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums)+1)
        dp[len(nums)] = 0
        dp[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1 ,-1):
            dp[i] = max((nums[i] + dp[i+2]), (dp[i+1]))
        return dp[0]





class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return self.process(nums, 0)

    
    def process(self, nums: List[int], index: int,):
        if index == len(nums):
            return 0
        if index == len(nums) - 1:
            return nums[index]
        # 不偷当前这家
        value_1 = self.process(nums, index+1)
        # 偷了当前这家
        value_2 = self.process(nums, index+2) + nums[index]
        return max(value_1, value_2)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums))
        dp[len(nums)-1] = nums[len(nums)-1]
        dp[len(nums)-2] = max(nums[len(nums)-1], nums[len(nums)-2])
        for k in range(len(nums)-3, -1, -1):
            dp[k] = max(dp[k+1], (dp[k+2] + nums[k])) 
        return dp[0]