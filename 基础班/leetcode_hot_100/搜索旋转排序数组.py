from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, left_value = 0, nums[0]
        right, right_value = len(nums) - 1 , nums[len(nums)-1]
        while left <= right:
            temp = (left + right) // 2
            if nums[temp] == target:
                return temp
            temp_value = nums[temp]
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            if nums[left] < nums[right]:
                return self.erfensearch(nums, target, left, right)
            if temp_value > nums[left] and target > nums[left] and target < temp_value:
                return self.erfensearch(nums, target, left, temp-1)
            if temp_value > nums[left]:
                left = temp + 1
                continue
            # 到了右半部分
            if temp_value < nums[left] and target > temp_value and target < nums[right]:
                return self.erfensearch(nums, target, temp+1, right)
            elif temp_value < nums[left]:
                right = temp - 1
                continue 
            else:
                return -1

    def erfensearch(self, nums: List[int], target: int, left: int, right: int):
        if left > right or left >= len(nums) or left < 0 or right < 0 or right >= len(nums):
            return -1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1 
        return -1

# 