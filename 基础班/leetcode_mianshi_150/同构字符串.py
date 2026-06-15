from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens, lent = len(s), len(t)
        if lens != lent:
            return False
        hash_map = {}
        have = set()
        for i in range(len(s)):
            if s[i] not in hash_map:
                if t[i] in have:
                    return False
                else:
                    hash_map[s[i]] = t[i]
                    have.add(t[i])
            else:
                if hash_map[s[i]] != t[i]:
                    return False
                else:
                    continue
        return True
