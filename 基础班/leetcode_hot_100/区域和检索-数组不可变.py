from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.pre_sum.append(self.pre_sum[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left > right or len(self.nums) == 0:
            return 0
        return self.pre_sum[right] - self.pre_sum[left] + self.nums[left]



        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)