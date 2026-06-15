from typing import List, Optional

from collections import deque
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapp = []
        for num in nums:
            if len(heapp) < k:
                heapq.heappush(heapp, num)
            else:
                heapq.heappushpop(heapp, num)
        return heapp[0]
