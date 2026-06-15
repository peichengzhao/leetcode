from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = float("-inf")
        left, right = 0, len(height)-1
        while left < right:
            result = max(result, min(height[left], height[right])*(right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result