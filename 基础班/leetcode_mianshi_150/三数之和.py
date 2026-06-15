from typing import List

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hash_map = set()
        nums = sorted(nums)
        result = []
        left, right = 0, len(nums) - 1
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    hash_map.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        for temp in hash_map:
            result.append(list(temp))
        return result
