from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        index = 0
        length = len(tokens)
        if not tokens or len(tokens) == 1:
            return None if not tokens else int(tokens[0])
        op_map = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*": lambda a,b: a*b, "/": lambda a,b: a/b}
        while index < length:
            if tokens[index] in {"+", "-", "*", "/"}:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(op_map[tokens[index]](num2, num1))
            else:
                stack.append(tokens[index])
            index += 1
        return int(stack.pop())

