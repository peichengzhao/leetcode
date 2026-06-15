class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length1, lenght2, length3 = len(s1), len(s2), len(s3)
        if length1 == length3 == lenght2 == 0:
            return True
        dp = [[False] * (lenght2+1) for _ in range(length1+1)]
        dp[0][0] = True
        for j in range(1, lenght2+1):
            if s2[:j] == s3[:j]:
                dp[0][j] = True
            else:
                break
        for i in range(1, length1+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
            else:
                break
        for i in range(1, length1+1):
            for j in range(1, lenght2+1):
                # dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
                if dp[i][j-1]:
                    if s2[j-1] == s3[i+j-1]:
                        dp[i][j] = True
                if dp[i-1][j]:
                    if s1[i-1] == s3[i+j-1]:
                        dp[i][j] = True
        return dp[-1][-1]