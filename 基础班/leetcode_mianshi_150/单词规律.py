from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        hash_map = {}
        have = set()
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                if word[i] in have:
                    return False
                else:
                    have.add(word[i])
                    hash_map[pattern[i]] = word[i]
            else:
                if hash_map[pattern[i]] != word[i]:
                    return False
                else:
                    continue
        return True

                