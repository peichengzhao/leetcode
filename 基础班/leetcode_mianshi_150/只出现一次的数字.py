from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


# 出现了三次

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            temp = 0
            for num in nums:
                temp += (num>>i) & 1
            if temp % 3 != 0:
                res |= 1 << i
        return res