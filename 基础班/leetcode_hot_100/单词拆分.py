from asyncio import FastChildWatcher
from typing import List
from unittest import TestResult

from numpy import true_divide

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict) 

        def backtrack(index):
            # 终止条件：走到字符串末尾 → 成功！
            if index == len(s):
                return True
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]  # 截取从 index 到 i 的子串
                if word in word_set:
                    if backtrack(i):
                        return True
            return False

        return backtrack(0)



class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        demo = {}
        def backtrack(index):
            if index == len(s):
                return True
            if index in demo:
                return demo[index]
            for i in range(index + 1, len(s)+1):
                if s[index:i] in word_set:
                    if backtrack(i):
                        demo[i] = True
                        return True
            demo[index] = False
            return False
        return backtrack(0)
        
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]