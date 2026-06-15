from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left, right = 0, 0
        temp_sum = nums[0]
        while right < len(nums):
            if temp_sum >= target:
                res = min(res, right - left + 1)
                temp_sum -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    temp_sum += nums[right]
        return res if res != float("inf") else 0