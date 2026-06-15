from typing import List
import heapq
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第k个最大元素 = 升序排序后第 len(nums)-k 个元素
        target_idx = len(nums) - k
        return self.quick_select(nums, 0, len(nums)-1, target_idx)
    
    def quick_select(self, nums: List[int], left: int, right: int, target_idx: int) -> int:
        # 随机选择基准元素，避免最坏情况
        pivot_idx = random.randint(left, right)
        # 将基准元素交换到右边界，方便分区
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        # 分区操作：小于基准的放左边，大于等于的放右边
        pivot = nums[right]
        i = left  # 记录小于基准的区域边界
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # 将基准元素放到正确位置（i的位置）
        nums[i], nums[right] = nums[right], nums[i]
        
        # 递归/终止条件
        if i == target_idx:
            return nums[i]
        elif i < target_idx:
            # 目标在右半区，递归处理右半部分
            return self.quick_select(nums, i+1, right, target_idx)
        else:
            # 目标在左半区，递归处理左半部分
            return self.quick_select(nums, left, i-1, target_idx)


