from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            
            while left < right:
                sum_num = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if sum_num == 0:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    # 去重左指针重复值 + 修复问题4：严格判断left < right 避免越界
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    # 去重右指针重复值 + 修复问题4：严格判断left < right 避免越界
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                    # ========== 修复问题3：找到解后，必须移动指针 ==========
                    left += 1
                    right -= 1
                elif sum_num < 0:
                    # ========== 修复问题1：总和偏小，左指针必须右移 ==========
                    left += 1
                else:
                    # ========== 修复问题1：总和偏大，右指针必须左移 ==========
                    right -= 1
        return result







class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if not nums or len(nums) <= 2:
            return [[]]
        results = []
        sorted_nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) -1
            while left < right:
                sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if sum == 0:
                    results.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
                elif sum > 0:
                    right -=1
                else:
                    left += 1
        return results
                
                        


                








