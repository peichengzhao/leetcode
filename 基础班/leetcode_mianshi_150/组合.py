from typing import List, Optional

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []
        if n == k == 1:
            return [[1]]
        def process(temp: List[int], index: int, count: int):
            if index == k:
                result.append(temp.copy())
                return 
            if n-count < k-index:
                return 
            for i in range(count, n):
                temp.append(i+1)
                process(temp, index+1, i+1)
                temp.pop()
        process(temp, 0, 0)
        return result

            