from typing import List

class Solution:
    # 比较 mid 和 mid+1，向大的方向缩小区间
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right: 
            mid = (left+right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid +1
            else:
                right = mid
        return left