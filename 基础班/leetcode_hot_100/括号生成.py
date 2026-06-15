import re
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <=0 :
            return []
        result = []
        hash_map = {}
        left, right = 0, 0
        self.process(n, "", hash_map, result, left, right)
        return result


    def process(self, n: int, cur_s: str, hash_map, result, left, right):
        if len(cur_s) == n * 2:
            if self.check_vaild(cur_s) and cur_s not in hash_map:
                hash_map[cur_s] = True
                result.append(cur_s)
                return
            else:
                return 
        # 加入左括号
        if left < n:
            self.process(n, cur_s + "(", hash_map, result, left + 1, right)
        # 加入右括号
        if left > right:
            self.process(n, cur_s + ")", hash_map, result, left, right + 1)
    def check_vaild(self, s: str):
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            if s[i] == ")":
                count -= 1
            if count < 0:
                return False
        return True if count == 0 else False

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = ""
        def process(cur_s: str, left: int, right: int):
            if len(cur_s) == n * 2:
                result.append(cur_s)
            if left < n:
                process(cur_s + "(", left+1, right)
            if left > right:
                process(cur_s + ")", left, right+1)
        process(path, 0, 0)
        return result














