from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        fushu = False
        if n < 0:
            fushu = True
            n = -n
        result = 1
        if n == 0 or x == 1:
            return 1
        hash_map = {}
        temp = x
        count = 1
        for i in range(32):
            hash_map[count] = temp
            count = count * 2 
            temp *= temp
        while n:
            number = n - (n & (n-1))
            result *= hash_map[number]
            n = n & (n-1)
        return 1 / result if fushu else result




from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        fushu = False
        if n < 0:
            fushu = True
            n = -n 
        result = 1.0
        current = x 
        while n :
            if n & 1:
                result *= current
            current *= current
            n = n >> 1
        return 1 / result if fushu else result
