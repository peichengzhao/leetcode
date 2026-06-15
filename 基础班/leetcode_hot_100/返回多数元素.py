from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        for key, value in hash_map.items():
            if value >= len(nums) / 2:
                return key
        return None        


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[len(nums) // 2]



# 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return None
        candidate = nums[0]
        count = 1
        for num in range(1, len(nums)):
            if nums[num] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[num + 1]
                count = 1
        return candidate
        

        