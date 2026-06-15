from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        # res 指向有效数组的最后一个位置
        res = 1
        # 从第三个元素开始遍历
        for temp in range(2, n):
            # 核心判断：和有效数组的倒数第二个不相等，就保留
            if nums[temp] != nums[res - 1]:
                res += 1
                nums[res] = nums[temp]
        return res + 1