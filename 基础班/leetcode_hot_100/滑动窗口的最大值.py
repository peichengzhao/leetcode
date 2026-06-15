from collections import deque
from typing import List


class Solution:
    # 需要使用单调递减队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        result = []
        queue = deque()
        for temp in range(len(nums)):
            while queue and nums[temp] > nums[queue[-1]]:
                queue.pop()
            queue.append(temp)
            while queue[0] <= temp - k:
                queue.popleft()
            if temp >= k - 1:
                result.append(nums[queue[0]])
        return result