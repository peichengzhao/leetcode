from typing import List



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = -1
        temp = 0
        while temp < len(nums):
            if nums[temp] == val:
                temp += 1
            else:
                res += 1
                nums[res] = nums[temp]
        return res + 1