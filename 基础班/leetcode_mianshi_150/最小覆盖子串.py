from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lens, lent = len(s), len(t)
        if lens < lent:
            return ""
        result = ""
        min_length = float("inf")
        hash_t = {}
        num_kind = 0
        for c in t:
            if c not in hash_t:
                num_kind += 1
            hash_t[c] = hash_t.get(c, 0) + 1
        satify = 0
        hash_map = {}
        left, right = 0, 0
        for right in range(lens):
            if s[right] not in hash_t:
                continue
            else:
                hash_map[s[right]] = hash_map.get(s[right], 0) + 1
                if hash_map[s[right]] == hash_t[s[right]]:
                    satify += 1
                while satify == num_kind:
                    if right - left + 1 < min_length:
                        min_length = right - left + 1
                        result = s[left: right+1]
                    if s[left] not in hash_map:
                        left += 1
                        continue
                    else:
                        hash_map[s[left]] -= 1
                        if hash_map[s[left]] < hash_t[s[left]]:
                            satify -= 1
                        left += 1
        return result


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        start = 0
        for c in t:
            need[c] = need.get(c, 0) + 1
        length = len(s)
        left, right = 0, 0
        valid = 0
        min_len = float("inf")
        while right < length:
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        vaild -= 1
                left += 1
            right += 1
        return "" if min_len == float("inf") else s[start: start+ min_len]