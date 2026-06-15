from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                middle = nums[i]
                nums[i] = nums[temp]
                nums[temp] = middle
                temp += 1
        return nums






class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        def change(nums: List[int], i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                change(nums, i, temp)
                temp += 1
        return nums