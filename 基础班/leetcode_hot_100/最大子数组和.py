from typing import List
# 超时
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return float('-inf')
        help_list = []
        help_list.append(nums[0])
        for i in range(1, len(nums)):
            help_list.append(help_list[i-1] + nums[i])
        result = help_list[0]
        for j in range(1, len(help_list)):
            for k in range(-1, j):
                if k == -1:
                    temp = help_list[j]
                else:
                    temp = help_list[j] - help_list[k]
                if temp > result:
                    result = temp
        return result


# ac解  利用前缀和和最小前缀和

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
        pre_sum = 0
        min_pre_sum = 0
        result = nums[0]
        for num in nums:
            pre_sum += num
            result = max(pre_sum - min_pre_sum, result)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return result
        






# 暴力超时解

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_sum = float('-inf')
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                temp += nums[j]
                if temp > max_sum:
                    max_sum = temp
        return max_sum
                 



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        #制造前缀和数组
        presum = [] * len(nums)
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            presum[i] = pre_sum
        min_pre_sum = presum[0]
        result = nums[0]
        for i in range(1, len(presum)):
            temp = presum[i] - min_pre_sum
            if temp > result:
                result = temp
            if presum[i] < min_pre_sum:
                min_pre_sum = presum[i]
        return result
            
            
            
