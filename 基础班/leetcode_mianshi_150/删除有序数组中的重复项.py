

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res, temp = 0, 1
        while temp < len(nums):
            if nums[temp] == nums[temp-1]:
                temp += 1
            else:
                res += 1
                nums[res] = nums[temp]
                temp += 1
        return res + 1 