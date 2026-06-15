from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 
        left, right = -1, len(nums)
        cur = 0
        while cur < right and cur < len(nums):
            if nums[cur] == 0:
                left += 1
                self.swap(nums, cur, left)
                cur += 1
                continue
            elif nums[cur] == 2:
                right -= 1
                self.swap(nums, cur, right)
                continue
            else:
                cur += 1

    def swap(self, nums: List[int], i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return 






class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 
        left, right = -1 ,len(nums)
        def swap(nums: List[int], i: int, j: int):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        index = 0 
        while index < len(nums):
            if nums[index] == 0:
                left += 1
                swap(nums, left, index)
                index += 1
            elif nums[index] == 2:
                right -= 1
                swap(nums, index, right)
            else:
                index += 1
        return 
