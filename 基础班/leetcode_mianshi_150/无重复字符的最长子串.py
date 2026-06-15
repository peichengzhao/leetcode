from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = set()
        if not s or len(s) == 1:
            return 0 if not s else 1
        max_length = 1
        temp = 1
        left, right = 0, 1
        hash_map.add(s[left])
        while right < len(s):
            if s[right] not in hash_map:
                hash_map.add(s[right])
                temp += 1
                max_length = max(temp, max_length)
                right += 1
            else:
                while s[right] in hash_map:
                    hash_map.remove(s[left])
                    left += 1
                    temp -= 1
                continue  
        return max_length
                    