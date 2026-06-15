import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heapq = []
        result = []
        heapq.heappush(min_heapq, (nums1[0]+ nums2[0], 0, 0))
        visit = set()
        visit.add((0,0))
        while min_heapq and len(result) < k:
            sum_val, i, j = heapq.heappop(min_heapq)
            result.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in visit:
                heapq.heappush(min_heapq, (nums1[i+1]+nums2[j], i+1, j))
                visit.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visit:
                heapq.heappush(min_heapq, (nums1[i]+nums2[j+1], i, j+1))
                visit.add((i, j+1))
        return result



import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heapq = []
        len1, len2 = len(nums1), len(nums2)
        result = []
        heapq.heappush(min_heapq, (nums1[0]+nums2[0], 0, 0))
        visit = set()
        visit.add((0,0))
        while min_heapq and len(result) <k:
            sum_val, i ,j = heapq.heappop(min_heapq)
            result.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in visit:
                heapq.heappush(min_heapq, (nums1[i+1]+nums2[j], i+1, j))
                visit.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visit:
                heapq.heappush(min_heapq, (nums1[i]+nums2[j+1], i, j+1))
                visit.add((i,j+1))
        return result