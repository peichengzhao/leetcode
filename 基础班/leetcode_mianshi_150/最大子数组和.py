from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 1
        res = nums[0]
        temp = nums[0]
        while right < len(nums):
            if temp < 0 :
                temp = nums[right]
                left = right
                right = left + 1
            else:
                temp += nums[right]
                right += 1
                res = max(res, temp)
        return res




from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_res = 0
        for num in nums:
            if cur_res < 0:
                cur_res = num
            else:
                cur_res += num
            res = max(res, cur_res)
        return res
        