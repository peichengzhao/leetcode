from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1, length2 = len(haystack), len(needle)
        temp = 0
        for i in range(length1 - length2 + 1):
            j = i 
            while temp < length2 and haystack[j] == needle[temp]:
                j += 1
                temp += 1
            if temp == length2:
                return i
            else:
                temp = 0
        return -1


# Sunday算法实现

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1, length2 = len(haystack), len(needle)
        shift = {}
        for i in needle:
            shift[needle[i]] = length2 - i
        idx = 0 
        while idx <= length1 - length2:
            str_out = haystack[idx: idx+ length2]
            if str_out == needle:
                return idx
            else:
                c_pos = idx + length2
                if c_pos >= length1:
                    break
                c = haystack[c_pos]
                if c in shift:
                    idx += shift[c]
                else:
                    idx += length2
        return -1



# KMP算法


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1, length2 = len(haystack), len(needle)
        def get_next_list(str_1: str):
            if len(str_1) == 1:
                return [-1]
            if len(str_1) == 2:
                return [-1, 0]
            next = [0] * len(str_1)
            next[0], next[1] = -1, 0
            i, j = 2, 0
            while i < len(str_1):
                if str_1[i-1] == str_1[j]:
                    next[i] = j+1
                    i += 1
                    j += 1
                elif j > 0:
                    j = next[j]
                else:
                    next[i] = 0
                    i += 1
            return next
        next = get_next_list(needle)
        i, j = 0, 0
        while i < length1 and j < length2:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i +=1
            else:
                j = next[j]
        return i - j if j == length2 else -1