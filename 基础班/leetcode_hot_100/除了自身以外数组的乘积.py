from typing import List

from numpy import double



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = []
        temp = 1
        zeros = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                temp *= nums[i]
            else:
                zeros[i] = True
        for i in range(len(nums)):
            if zeros and i not in zeros:
                result.append(0)
            elif not zeros:
                result.append(int(temp/nums[i]))
            else:
                if len(zeros) > 1:
                    result.append(0)
                else:
                    result.append(int(temp))
        return result




# 不使用额外空间  试试看
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = [0] * len(nums)
        zero = False
        double_zero = False
        temp = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                temp *= nums[i]
            if nums[i] == 0 and not zero:
                zero = True
                continue
            if nums[i] == 0 and zero:
                double_zero = True
        if double_zero:
            return result
        if zero:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = temp
                    break
            return result
        for i in range(len(nums)):
            result[i] = int(temp / nums[i])
        return result