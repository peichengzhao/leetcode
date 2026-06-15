from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                left_res, right_res = middle, middle
                while left_res > 0 and nums[left_res] == nums[left_res-1]:
                    left_res -= 1
                while right_res < len(nums) and nums[right_res] == nums[right_res+1]:
                    right_res += 1
                return [left_res, right_res]
            elif nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        return [-1, -1]