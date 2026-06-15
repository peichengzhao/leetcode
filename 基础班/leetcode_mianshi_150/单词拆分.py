from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length+1)
        dp[0] = True
        for i in range(1, length+1):
            for word in wordDict:
                if i - len(word) < 0:
                    continue
                else:
                    if s[i-len(word): i] == word:
                        dp[i] = dp[i-len(word)] or dp[i]
        return dp[-1]
