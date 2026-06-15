from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k == 0 or not nums:
            return
        k = k % length
        def reverse_list(nums: List[int], left: int, right: int):
            if left >= right or not nums:
                return 
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return
        reverse_list(nums, 0, length-1)
        reverse_list(nums, 0, k-1)
        reverse_list(nums, k, length-1)
        return 
