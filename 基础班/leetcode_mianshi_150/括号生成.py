from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left_number, right_number = 0, 0 
        result = []
        temp = []
        def process(index: int):
            nonlocal left_number, right_number, temp, result
            if index == 2 * n:
                result.append("".join(temp.copy()))
                return 
            if left_number > right_number:
                index += 1
                temp.append(")")
                right_number += 1
                process(index)
                temp.pop()
                right_number -= 1
                index -= 1
            if left_number < n:
                index += 1
                temp.append("(")
                left_number += 1
                process(index)
                temp.pop()
                left_number -= 1
                index -= 1
        process(0)
        return result




class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def process(cur_s: int, left, right):
            if len(cur_s) == 2 * n:
                result.append(cur_s)
            if left < n:
                process(cur_s + "(", left+1, right)
            if left > right:
                process(cur_s + ")", left, right+1)
        process("", 0, 0)
        return result