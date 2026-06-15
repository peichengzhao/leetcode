from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[0] * length1 for _ in range(length2)]
        for i in range(length2):
            if word2[i] == word1[0]:
                dp[i][0] = i
            else:
                if i ==0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = dp[i-1][0] + 1
        for j in range(length1):
            if word1[j] == word2[0]:
                dp[0][j] = j
            else:
                if j ==0:
                    dp[0][j] = 1
                else:
                    dp[0][j] = dp[0][j-1] + 1
        for i in range(1, length2):
            for j in range(1, length1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]




class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)
        if not word2:
            return ""
        dp = [[0] * (length1+1) for _ in range(length2+1)]
        for i in range(length2+1):
            dp[i][0] = i
        for j in range(length1):
            dp[0][j] = j
        for i in range(1, length2+1):
            for j in range(1, length1+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
