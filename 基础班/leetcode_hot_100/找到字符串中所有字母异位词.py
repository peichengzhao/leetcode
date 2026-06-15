from typing import List

# 超时解
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        count_list = [0] * 26
        for i in range(len(p)):
            count_list[ord(p[i]) - ord("a")] += 1
        def check(index: int,):
            if index >= len(s):
                return False
            temp_list = count_list.copy()
            temp = 0
            while index < len(s) and temp < len(p):
                if temp_list[ord(s[index]) - ord("a")] > 0:
                     temp_list[ord(s[index]) - ord("a")] -= 1
                     index += 1
                     temp += 1
                else:
                    return False
            return True if temp == len(p) else False
        result = []
        for i in range(len(s)):
            if check(i):
                result.append(i)
        return result


#利用两个计数窗口和滑动窗口来解决问题

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(p) > len(s):
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        res = []
        for i in range(len(p)):
            p_count[ord(p[i]) - ord("a")] += 1
        for i in range(len(p)):
            s_count[ord(s[i]) - ord("a")] += 1
        if s_count == p_count:
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            left_char = s[i-1]
            right_char = s[i + len(p) - 1]
            s_count[ord(left_char) - ord("a")] -= 1
            s_count[ord(right_char) - ord("a")] += 1
            if s_count == p_count:
                res.append(i)
        return res
