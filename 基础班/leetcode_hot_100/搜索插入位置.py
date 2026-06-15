from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        for i in range(1, len(nums)):
            if target == nums[i]:
                return i
            if nums[i-1] < target < nums[i]:
                return i
        return len(nums)

