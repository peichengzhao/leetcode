class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if s[i] == ')' and cur == '(':
                    continue 
                elif s[i] == ']' and cur == '[':
                    continue
                elif s[i] == '}' and cur == '{':
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False