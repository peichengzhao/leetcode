from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        for c in t:
            if c not in hash_map:
                return False
            elif hash_map[c] == 0:
                return False
            else:
                hash_map[c] -= 1
        for value in hash_map:
            if value > 0:
                return False
        return True

