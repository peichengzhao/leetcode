from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        cur_max_sum = 0
        cur_min_sum = 0
        max_sum = nums[0]
        min_sum = nums[0]
        for num in nums:
            if cur_max_sum < 0:
                cur_max_sum = num
            else:
                cur_max_sum += num
            max_sum = max(cur_max_sum, max_sum)
            if cur_min_sum > 0:
                cur_min_sum = num
            else:
                cur_min_sum += num
            min_sum = min(min_sum, cur_min_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum, sum(nums)-min_sum)
