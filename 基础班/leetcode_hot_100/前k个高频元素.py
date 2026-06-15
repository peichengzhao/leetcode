from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        hash_map = {}
        my_heapq = []
        for num in range(nums):
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        for key, value in hash_map:
            temp = (-value, key)
            heapq.heappush(my_heapq, temp)
        result = []
        while k:
            result.append(heapq.heappop()[1])
        return result
