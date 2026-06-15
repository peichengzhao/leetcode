from typing import List




class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_1, length_2 = len(text1), len(text2)
        dp = [[0] * length_2 for _ in range(length_1)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, length_2):
            if dp[0][i-1] == 1:
                dp[0][i] = 1
            else:
                dp[0][i] = 1 if text1[0] == text2[i] else 0
        for j in range(1, length_1):
            if dp[j-1][0] == 1:
                dp[j][0] = 1
            else:
                dp[j][0] = 1 if text2[0] == text1[j] else 0
        for i in range(1, length_1):
            for j in range(1, length_2):
                str_1, str_2 = text1[i], text2[j]
                if str_1 == str_2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]