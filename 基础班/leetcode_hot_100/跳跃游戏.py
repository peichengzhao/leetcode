from typing import List


# 尝试暴力

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if not nums or len(nums) == 0:
#             return False
#         return self.process(nums, 0)
#     def process(self, nums: List[int] ,index: int) -> bool:
#         if index == len(nums) - 1 :
#             return True
#         can_jump = nums[index]
#         for i in range(1, can_jump + 1):
#             if self.process(nums, index + i):
#                 return True
#         return False


# 还是超时
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if not nums or len(nums) == 0:
#             return False
#         if len(nums) == 1:
#             return True

#         help_list = [False] * len(nums)
#         help_list[0] = True
#         for i in range(0, len(nums)):
#             if not help_list[i]:
#                 continue
#             else:
#                 pos = min(nums[i], len(nums) - 1 - i)
#                 for j in range(1, pos + 1):
#                     help_list[i + j] = True
#         return help_list[-1]
            
            
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        max_pos = 0
        for i in range(len(nums)):
            if i < max_pos:
                return False
            else:
                max_pos = max(max_pos, i + nums[i])
        return max_pos >= len(nums) - 1













class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        max_pos = 0
        for i in range(len(nums)):
            if i > max_pos:
                return False
            max_pos = max(max_pos, i+nums[i])
        return max_pos >= len(nums) -1








class Solution:
    def jump(self, nums: List[int]) -> int:
        








