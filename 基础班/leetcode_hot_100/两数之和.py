from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == temp:
                    return [i , j]
        return [-1, -1]

#进阶写法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        self.quick_sort(nums, 0 ,len(nums)-1)
        # find the target
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [left, right]



    def change_value(self, nums: List[int], i: int, j: int):
        temp_1 = nums[i]
        nums[i] = nums[j]
        nums[j] = temp_1
        return nums

    def partition(self, nums: List[int], left: int, right: int):
        if left >= right:
            return left, right
        temp = nums[left]
        less, more = left, right + 1
        index = left + 1
        while index < more:
            if nums[index] > temp:
                more -= 1
                self.change_value(nums, more, index)
            elif nums[index] < temp:
                less += 1
                self.change_value(nums, less, index)
                index += 1
            else:
                index += 1
        self.change_value(nums, less, left)
        return less, more-1
    def quick_sort(self, nums: List[int] ,left: int, right: int):
        if left >= right:
            return 
        temp = nums[0]
        new_left, new_right = self.partition(nums, 0, len(nums)-1)
        #左边
        self.quick_sort(nums, left, new_left -1)
        self.quick_sort(nums, new_right+1, right)
        
