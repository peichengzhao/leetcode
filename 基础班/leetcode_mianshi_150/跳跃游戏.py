from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_pos = 0
        for i in range(len(nums)):
            if max_pos < i:
                return False
            max_pos = max(max_pos, i+nums[i])
            if max_pos >= len(nums) -1:
                return True
        return False
