from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        end = 0
        temp = 0
        while temp < len(nums)-1:
            step += 1
            jump_length = nums[temp]
            zuiyuan = temp
            for i in range(jump_length):
                if i+temp < len(nums):
                    zuiyuan = max(zuiyuan, temp+nums[i+temp])
                else: 
                    zuiyuan = len(nums)
            temp = zuiyuan
        return steps