from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #判断 ransomNote 能不能由 magazine 里面的字符构成
        hash_map = {}
        for s in magazine:
            if s not in hash_map:
                hash_map[s] = 1
            else:
                hash_map[s] += 1
        for c in ransomNote:
            if c not in hash_map or hash_map[c] == 0:
                return False
            else:
                hash_map[c] -= 1
        return True