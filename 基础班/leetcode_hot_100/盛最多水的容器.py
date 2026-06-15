from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water




class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        left, right = 0, len(height) - 1
        max_value = 0
        while left < right:
            max_value = max((min(height[left], height[right]) * (right-left)), max_value)
            if height[left] <= height[right]:
                 left += 1
            else:
                right -= 1
        return max_value