
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = []
        if numRows == 0:
            return results
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        results = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [0] * (i+1)
            temp[0], temp[i] = 1, 1
            for j in range(1, i):
                temp[j] = (results[i-1][j-1] + results[i-1][j])
            results.append(temp)
        return results