
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        start = 0
        # 统计目标字符串t的字符频次（构建hash_map）
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
                        valid -= 1
                left += 1
            right += 1
        return "" if min_len == float("inf") else s[start: start + min_len]