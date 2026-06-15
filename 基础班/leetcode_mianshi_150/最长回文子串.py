from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #得考虑是对称轴和需对称轴
        if not s:
            return ""
        max_length = 1
        max_begin, max_end = 0, 0
        for i in range(len(s)):
            #考虑实轴
            begin_1, end_1 = i, i
            while begin_1 >= 0 and end_1 <= len(s)-1 and s[begin_1] == s[end_1]:
                if end_1 - begin_1 +1 > max_length:
                    max_length = end_1 - begin_1 +1
                    max_begin, max_end = begin_1, end_1
                begin_1 -= 1
                end_1 += 1
            begin_2, end_2 = i-1, i
            while begin_2 >= 0 and end_2 <= len(s)-1 and s[begin_2] == s[end_2]:
                if end_2 - begin_2 + 1 > max_length:
                    max_length = end_2 - begin_2 + 1 
                    max_begin, max_end = begin_2, end_2
                begin_2 -= 1
                end_2 += 1
        return s[max_begin: max_end+1]