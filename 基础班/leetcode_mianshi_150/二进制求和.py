from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena ,lenb = len(a), len(b)
        res = ""
        i, j = lena - 1, lenb - 1
        jinwei = False
        while i >= 0 and j >= 0:
            temp = (1 if jinwei else 0) + int(a[i]) + int(b[j])
            if temp == 1 or temp == 0:
                jinwei = False
                res += str(temp)
            elif temp == 2:
                jinwei = True
                res += str(0)
            else:
                jinwei = True
                res += str(1)
            i -= 1
            j -= 1
        while i >= 0:
            temp = (1 if jinwei else 0) + int(a[i])
            if temp == 1 or temp == 0:
                res += str(temp)
                jinwei = False
            else:
                jinwei = True
                res += str(0)
            i -= 1 
        while j >= 0:
            temp = (1 if jinwei else 0) + int(b[j])
            if temp == 1 or temp == 0:
                res += str(temp)
                jinwei = False
            else:
                jinwei = True
                res += str(0)
            j -= 1
        if jinwei == True:
            res += str(1)
        return res[::-1]

# 优雅解法
# 优雅解法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry: 
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            temp = digit_a + digit_b + carry
            carry = temp // 2
            current = temp % 2
            res.append(str(current))
            i -= 1
            j -= 1
        return "".join(reversed(res))







