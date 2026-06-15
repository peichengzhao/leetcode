from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(s) < len(words) * len(words[0]):
            return []
        hash_map = {}
        result = []
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1
        word_length = len(words) * len(words[0])
        length = len(words[0])
        for begin in range(len(s) - word_length +1):
            substr = s[begin: begin+word_length]
            temp_map = hash_map.copy()
            valid = True
            for i in range(0, word_length, length):
                curr_word = substr[i: i+ length]
                if curr_word not in temp_map or temp_map[curr_word] == 0:
                    valid = False
                else:
                    temp_map[curr_word] -= 1
            if valid == True:
                result.append(begin)
        return result