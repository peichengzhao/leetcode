from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        length = len(nums)
        result = []
        left, right = 0, 0
        while right < len(nums):
            if right < len(nums) - 1 and nums[right+1] == nums[right] + 1:
                right += 1
            else:
                if left == right:
                    result.append(str(nums[left]))
                else:
                    temp = str(nums[left]) + "->" + str(nums[right])
                    result.append(temp)
                left = right + 1
                right = left
        return result
            