from curses import nonl
from unittest import result

#超时

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 4:
            return 0 
        def process(index: int):
            if index == 1:
                return 1
            else:
                return process(index-1) * index
        res = process(n)
        temp = 0
        while res > 0:
            if res % 10 == 0:
                temp += 1
                res = res // 10
            else:
                break
        return temp


# 找到5的个数

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            if n // 5 > 0:
                res += n // 5
                n = n // 5
            else:
                break
        return res



