from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ss = list(s)
        for i in range(len(ss)):
            if stack and ss[stack[-1]] == "(" and ss[i] == ")":
                ss[stack[-1]] = "a"
                stack.pop()
                ss[i] = "a"
            else:
                stack.append(i)
        temp = 0
        max_length = 0
        for i in range(len(ss)):
            if ss[i] == "a":
                temp += 1
                max_length = max(max_length, temp)
            else:
                temp = 0
        return max_length