from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if nums[left] <= nums[right]:
            return nums[left]
        mid = (left + right) // 2
        n = len(nums)
        while left < right:
            mid_left = (mid-1) % n
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]
