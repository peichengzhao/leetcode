from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == ")" and stack[-1] != "(":
                    return False
                elif s[i] == "}" and stack[-1] != "{":
                    return False
                elif s[i] == "]" and stack[-1] != "[":
                    return False
                else:
                    stack.pop()
        return False if stack else True