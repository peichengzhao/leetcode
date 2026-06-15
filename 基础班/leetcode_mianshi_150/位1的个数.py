from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >= 0:
            temp = n & 1
            count += temp
            n = n >> 1
        return count


from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count