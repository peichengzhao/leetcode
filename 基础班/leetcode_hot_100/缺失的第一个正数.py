from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        length = len(nums)
        help_list = [0] * length
        for num in nums:
            if num >= 1 and num <= length:
                help_list[num-1] = 1
        for i in range(len(help_list)):
            if help_list[i] == 0:
                return i+1
        return len(help_list) + 1