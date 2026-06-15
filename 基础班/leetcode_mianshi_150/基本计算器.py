class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res



class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == "+" or c == "-":
                res += num * sign
                num = 0
                sign = 1 if c == "+" else -1
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == ")":
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        res += num * sign
        return res

