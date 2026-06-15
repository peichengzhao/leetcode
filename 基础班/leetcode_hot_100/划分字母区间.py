from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #记录每个字母出现的最后位置
        last_pos = {}
        for idx, char in enumerate(s):
            last_pos[char] = idx
        res = []
        left = 0
        right = 0
        for idx, char in enumerate(s):
            right = max(right, last_pos[char]) #代表前面的所有字符的共同最后出现位置
            
            if idx == right:
                res.append(idx-left+1)
                left = idx + 1
        return res