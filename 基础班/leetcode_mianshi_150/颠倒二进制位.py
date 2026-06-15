class Solution:
    def reverseBits(self, n: int) -> int:
        res = [0] * 32
        index = 0
        while n:
            res[index] = n & 1 # 按位与的操作
            n = n >> 1
            index += 1
        ans = 0
        for bit in res:
            ans = ans * 2 + bit
        return ans 
