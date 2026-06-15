from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        sorted_citations = sorted(citations)
        result = 0
        for i in range(n):
            if n-i <= sorted_citations[i]:
                return n - i
