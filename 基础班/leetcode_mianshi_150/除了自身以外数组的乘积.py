from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_sum_list = [0] * len(nums)
        left_sum = 1
        for i in range(len(nums)):
            left_sum_list[i] = left_sum
            left_sum *= nums[i]
        right_sum_list = [0] * len(nums)
        right_sum = 1
        for j in range(len(nums)-1, -1, -1):
            right_sum_list[j] = right_sum
            right_sum *= nums[j]
        result = [0] * len(nums)
        for i in range(len(result)):
            result[i] = left_sum_list[i] * right_sum_list[i]
        return result